#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026/3/9 15:24
# @Name    : planning_stage.py
# @Author  : mayiming
import hashlib

from configs.prompt_template import PROMPT_TEMPLATES
from constants.prompt import PLANNING_PROMPT
from constants.stage import PLANNING_STAGE
from models.model_client import ModelClient
from schema.prepare import PrepareResponse
from utils.cache import caches


class PlanningStage:
    def __init__(self):
        self.model_client = ModelClient(PLANNING_STAGE)

    def prepare(self, jd: str, resume: str):
        import uuid
        interview_id = str(uuid.uuid4())
        # 这里也可以分布调用，先生成核心要求，再生成亮点风险点，最后计划。
        plan_prompt = PROMPT_TEMPLATES.get(PLANNING_PROMPT).format(
            jd_content=jd,
            resume_content=resume,
        )
        plan = self.model_client.invoke(plan_prompt)

        caches[interview_id] = {
            "jd": jd,
            "resume": resume,
            "plan": plan.get("content"),
        }
        return PrepareResponse(
            conversation_id=interview_id,
            **plan.get("content"))
