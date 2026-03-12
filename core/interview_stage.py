#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026/3/9 15:25
# @Name    : interview_stage.py
# @Author  : mayiming
import os
from typing import List, Any

from src.configs.prompt_template import PROMPT_TEMPLATES
from src.constants.prompt import INTERVIEW_PROMPT
from src.constants.stage import INTERVIEW_STAGE
from src.models.model_client import ModelClient
from src.schema.interview import InterviewResponse, InterviewRequest
from src.utils.cache import caches


class InterviewStage:
    def __init__(self):
        self.model_client = ModelClient(INTERVIEW_STAGE)

    def interview(self, interview_id, interview_request: InterviewRequest):
        cache = caches.get(interview_id)

        interview_prompt = PROMPT_TEMPLATES.get(INTERVIEW_PROMPT).format(
            interview_plan=cache["plan"],
            max_turns=os.getenv("MAX_TURNS"),
        )

        history_id = "messages:" + interview_id
        history = caches.get(history_id)
        if history is None:
            history = []

        interview = self.model_client.invoke(
            interview_prompt,
            history,
            interview_request.last_answer)

        content = interview.get("content")

        history.append({"role": "user", "content": interview_request.last_answer})
        history.append({"role": "assistant", "content": str(content)})
        caches[history_id] = history

        return InterviewResponse(**content)
