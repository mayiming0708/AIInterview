#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026/3/10 09:42
# @Name    : cache.py
# @Author  : mayiming
from typing import Dict

caches: Dict[str, any] = {"1": {
    "jd": "这是一个AI智能体构建的岗位，需要可以熟练使用langgraph",
    "resume": "张三，本科学历，计算机专业，有多个智能体构建落地经验",
    "plan": {
        "core_competencies": [
            "AI智能体构建",
            "langgraph使用",
            "项目落地能力"
        ],
        "resume_highlights": [
            "多个智能体构建落地经验",
            "计算机专业背景"
        ],
        "risk_points": [
            "缺少相关工作经验的具体细节",
            "未提及团队合作或领导能力"
        ],
        "interview_strategy": "重点考察候选人在AI智能体构建方面的实际经验和对langgraph的掌握程度，同时评估其项目管理能力和团队合作能力。",
        "question_plan": [
            {
                "dimension": "技术深度",
                "question": "请描述您在智能体构建中使用langgraph的具体案例。",
                "evaluation_points": [
                    "对langgraph的理解",
                    "实际应用能力"
                ]
            },
            {
                "dimension": "项目经验",
                "question": "您参与的智能体构建项目中，遇到过哪些挑战？您是如何解决的？",
                "evaluation_points": [
                    "问题解决能力",
                    "项目管理能力"
                ]
            },
            {
                "dimension": "团队合作",
                "question": "在您的项目中，您是如何与团队成员协作的？",
                "evaluation_points": [
                    "沟通能力",
                    "团队合作精神"
                ]
            }
        ]
    }}}
