#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026/3/9 14:59
# @Name    : model_config.py
# @Author  : mayiming
import os
from typing import Dict

from constants.stage import PLANNING_STAGE, EVALUATION_STAGE, INTERVIEW_STAGE
from pydantic import BaseModel

api_key = os.getenv("OPENAI_KEY", "")
base_url = os.getenv("BASE_URL")


class ModelConfig(BaseModel):
    model_name: str
    api_key: str
    temperature: float
    base_url: str = base_url


# 模板管理正常应存数据库或配置文件。这里只为运行就直接存储了。
# 温度策略：在计划和评估应该使用低温度保证稳定性，在面试阶段适当提高温度以保证面试题的多样性
# deterministic模式：可以通过设置温度为0或者固定seed来开启deterministic模式
# 如何避免候选人评分差异过大：通过使用低温度，以及不要更换模型等
# 使用缓存：缓存存储了会话ID，会话记录等内容
MODEL_CONFIGS: Dict[str, ModelConfig] = {
    PLANNING_STAGE: ModelConfig(
        model_name="gpt-4o-mini",
        api_key=api_key,
        temperature=0.1
    ),
    INTERVIEW_STAGE: ModelConfig(
        model_name="gpt-4o-mini",
        api_key=api_key,
        temperature=0.5
    ),
    EVALUATION_STAGE: ModelConfig(
        model_name="gpt-4o",
        api_key=api_key,
        temperature=0.1
    )
}

# 备用模型
FALLBACK_MODEL = ModelConfig(
    model_name="gpt-4o-mini",
    api_key=api_key,
    temperature=0.1
)

PRICE : Dict[str, float] = {
    "gpt-4o-mini": 0.00015,
    "gpt-4o": 0.0006,
}
