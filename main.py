#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026/3/9 14:47
# @Name    : main.py
# @Author  : mayiming
import logging

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv(override=True)

from core.evaluation_stage import EvaluationStage
from core.interview_stage import InterviewStage
from core.planning_stage import PlanningStage
from schema.interview import InterviewRequest
from schema.prepare import PrepareRequest

app = FastAPI()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


# 题目示例传参不太符合实际，所以这里做了修改，缓存了部分参数，如jd,resume
@app.post("/interview/prepare")
def prepare(data: PrepareRequest):
    planner = PlanningStage()
    return planner.prepare(data.jd, data.resume)


@app.post("/interview/{interview_id}/next")
def next(interview_id: str, interview_request: InterviewRequest):
    interviewer = InterviewStage()
    return interviewer.interview(interview_id, interview_request)


@app.post("/interview/{interview_id}/evaluate")
def evaluate(interview_id: str):
    evaluator = EvaluationStage()
    return evaluator.evaluate(interview_id)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
