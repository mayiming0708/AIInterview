#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026/3/9 16:09
# @Name    : evaluation.py
# @Author  : mayiming
from typing import List, Any

from pydantic import BaseModel, Field


class EvaluationRequest(BaseModel):
    full_conversation: List[Any] = Field(default_factory=list, description="会话历史")


class DimensionScores(BaseModel):
    technical_depth: int
    problem_solving: int
    communication: int


class EvaluationResponse(BaseModel):
    overall_score: int
    dimension_scores: DimensionScores
    strengths: List[str]
    weaknesses: List[str]
    risk_assessment: str
    hire_recommendation: str
