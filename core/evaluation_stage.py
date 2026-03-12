#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026/3/9 15:25
# @Name    : evaluation_stage.py
# @Author  : mayiming
from src.configs.prompt_template import PROMPT_TEMPLATES
from src.constants.prompt import EVALUATION_PROMPT
from src.constants.stage import EVALUATION_STAGE
from src.models.model_client import ModelClient
from src.schema.evaluation import EvaluationResponse, EvaluationRequest
from src.utils.cache import caches


class EvaluationStage:
    def __init__(self):
        self.model_client = ModelClient(EVALUATION_STAGE)

    def evaluate(self, interview_id: str):
        cache = caches.get(interview_id)
        evaluation_prompt = PROMPT_TEMPLATES.get(EVALUATION_PROMPT).format(
            jd_content=cache["jd"],
            resume_content=cache["resume"],
        )

        history_id = "messages:" + interview_id
        history = caches.get(history_id)
        evaluation = self.model_client.invoke(evaluation_prompt, history=history)
        return EvaluationResponse(**evaluation.get("content"))
