#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026/3/9 14:47
# @Name    : main.py
# @Author  : mayiming
import uvicorn
from fastapi import FastAPI

from src.core.evaluation_stage import EvaluationStage
from src.core.interview_stage import InterviewStage
from src.core.planning_stage import PlanningStage
from src.schema.interview import InterviewRequest
from src.schema.prepare import PrepareRequest

app = FastAPI()


# 题目示例传参不太符合实际，所以这里做了修改，缓存了部分参数，如jd,resume
# 会话记录也建议存储，避免前端篡改，当前未实现
@app.post("/interview/prepare")
async def prepare(data: PrepareRequest):
    planner = PlanningStage()
    return planner.prepare(data.jd, data.resume)


@app.post("/interview/{interview_id}/next")
async def next(interview_id: str, interview_request: InterviewRequest):
    interviewer = InterviewStage()
    return interviewer.interview(interview_id, interview_request)


@app.post("/interview/{interview_id}/evaluate")
async def evaluate(interview_id: str):
    evaluator = EvaluationStage()
    return evaluator.evaluate(interview_id)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
