#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026/3/9 16:08
# @Name    : interview.py
# @Author  : mayiming
from typing import Optional

from pydantic import BaseModel, Field


class InterviewRequest(BaseModel):
    last_answer: str = Field(..., description="候选人答案")


class InterviewResponse(BaseModel):
    current_dimension: str
    score: int
    follow_up: bool
    next_dimension: Optional[str]
    next_question: Optional[str]
