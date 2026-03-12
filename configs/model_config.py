#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026/3/9 14:59
# @Name    : model_config.py
# @Author  : mayiming
from typing import Dict

from pydantic import BaseModel

from src.constants.stage import PLANNING_STAGE, EVALUATION_STAGE, INTERVIEW_STAGE


class ModelConfig(BaseModel):
    model_name: str
    api_key: str
    temperature: float
    base_url: str = "https://c-z0-api-01.hash070.com/v1"
    max_turns: int = 5


# 模板管理正常应存数据库或配置文件。这里只为运行就直接存储了。
# 温度策略：在计划和评估应该使用低温度保证稳定性，在面试阶段适当提高温度以保证面试题的多样性
# deterministic模式：可以通过设置温度为0来开启deterministic模式
# 如何避免候选人评分差异过大：通过使用低温度，以及不要更换模型等
# 使用缓存：缓存存储了会话ID，会话记录等内容
MODEL_CONFIGS: Dict[str, ModelConfig] = {
    PLANNING_STAGE: ModelConfig(
        model_name="gpt-4o-mini",
        api_key="sk-zmpvF70MAf87Ce54c528T3BlBKFJ34ac1Dc6241c43E8A599",
        temperature=0.1
    ),
    INTERVIEW_STAGE: ModelConfig(
        model_name="gpt-4o-mini",
        api_key="sk-zmpvF70MAf87Ce54c528T3BlBKFJ34ac1Dc6241c43E8A599",
        temperature=0.5
    ),
    EVALUATION_STAGE: ModelConfig(
        model_name="gpt-4o-mini",
        api_key="sk-zmpvF70MAf87Ce54c528T3BlBKFJ34ac1Dc6241c43E8A599",
        temperature=0.1
    )
}

# 备用模型
FALLBACK_MODEL = ModelConfig(
    model_name="gpt-4o-mini",
    api_key="sk-zmpvF70MAf87Ce54c528T3BlBKFJ34ac1Dc6241c43E8A599",
    temperature=0.1
)
