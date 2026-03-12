#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026/3/9 16:02
# @Name    : response_schema.py
# @Author  : mayiming
from typing import List

from pydantic import BaseModel, Field

class PrepareRequest(BaseModel):
    jd: str = Field(..., description="岗位简介")
    resume: str = Field(..., description="候选人简历")


class Question(BaseModel):
    dimension: str
    question: str
    evaluation_points: List[str]


class PrepareResponse(BaseModel):
    conversation_id: str
    core_competencies: List[str]
    resume_highlights: List[str]
    risk_points: List[str]
    interview_strategy: str
    question_plan: List[Question]
