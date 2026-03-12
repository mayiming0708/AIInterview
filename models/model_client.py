#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026/3/9 15:37
# @Name    : model_client.py
# @Author  : mayiming
import json
import logging

from configs.model_config import MODEL_CONFIGS, FALLBACK_MODEL, PRICE
from openai import OpenAI
from openai.types.shared_params import ResponseFormatJSONObject

logger = logging.getLogger(__file__)


# token统计：当前使用的大模型返回token计算，只是做了提取，未使用，若多个不同种类模型，可以使用tiktoken库计算
# 面试成本：根据模型不同成本可能不同，以当前配置计算。
#   假设面试5轮，每轮消耗token500输入，200token输出，计算时，输出token比较固定，输入token不断叠加。
#   合计大约一共6500输入token，输出1000，成本约6500/1000*0.00015+1000/1000*0.0006=0.001575
#   最后评估，使用4o,输入约2500token，输出200token，2500/1000*0.0025+200/1000*0.010=0.00825
#   合计：0.001575+0.00825=0.009825
# 面试轮数：限制10轮，避免消耗太多token
# 模型封层策略：计划和面试阶段可使用4o-mini,评估为了准确性使用4o
class ModelClient:
    def __init__(self, stage: str):
        self.model_config = MODEL_CONFIGS.get(stage)
        self.client = OpenAI(
            api_key=self.model_config.api_key,
            base_url=self.model_config.base_url
        )

    def invoke(self, system_prompt, history=None, user_prompt=None):
        logger.info(f"start call model {self.model_config.model_name}")
        system_message = {
            "role": "system",
            "content": system_prompt,
        }
        user_message = {
            "role": "user",
            "content": user_prompt,
        }
        messages = [system_message]
        if history:
            messages.extend(history)
        if user_prompt:
            messages.append(user_message)
        from openai import OpenAIError
        try:
            response = self.client.chat.completions.create(
                model=self.model_config.model_name,
                messages=messages,
                temperature=self.model_config.temperature,
                response_format=ResponseFormatJSONObject(type="json_object"),
            )
        except OpenAIError as e:
            logger.warning(f"{self.model_config.model_name} failed: {e}, trying fallback model")
            self.model_config = FALLBACK_MODEL
            self.client = OpenAI(
                api_key=self.model_config.api_key,
                base_url=self.model_config.base_url
            )
            response = self.client.chat.completions.create(
                model=self.model_config.model_name,
                messages=messages,
                temperature=self.model_config.temperature,
                response_format=ResponseFormatJSONObject(type="json_object"),
            )

        content = json.loads(response.choices[0].message.content)
        # 不同模型tokens统计方法可采用tiktoken组件计算，当前只使用了接口调用返回的token计算
        usage_info = response.usage
        logger.info(f"end call model {self.model_config.model_name}, cost token {usage_info.total_tokens}")

        # 总成本可以分开算输入和输出，价格不一样, 这里只是假设一致简单计算了
        # 若需计算每个面试所消耗可以缓存cost，使用interview_id做key，做累计。时间原因未实现
        cost = usage_info.total_tokens * PRICE[self.model_config.model_name] / 1000
        return {
            "content": content,
            "total_tokens": usage_info.total_tokens,
            "cost": cost,
        }
