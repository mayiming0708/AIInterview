#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026/3/9 15:25
# @Name    : evaluation_stage.py
# @Author  : mayiming
from fastapi import HTTPException
from configs.prompt_template import PROMPT_TEMPLATES
from constants.prompt import EVALUATION_PROMPT
from constants.stage import EVALUATION_STAGE
from models.model_client import ModelClient
from schema.evaluation import EvaluationResponse, EvaluationRequest
from utils.cache import caches


class EvaluationStage:
    def __init__(self):
        self.model_client = ModelClient(EVALUATION_STAGE)

    def evaluate(self, interview_id: str):
        cache = caches.get(interview_id)
        if cache is None:
            raise HTTPException(status_code=404, detail="Interview not found")

        evaluation_prompt = PROMPT_TEMPLATES.get(EVALUATION_PROMPT).format(
            jd_content=cache["jd"],
            resume_content=cache["resume"],
        )

        history_id = "messages:" + interview_id
        history = caches.get(history_id)
        evaluation = self.model_client.invoke(evaluation_prompt, history=history)
        return EvaluationResponse(**evaluation.get("content"))
