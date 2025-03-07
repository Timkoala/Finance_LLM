# -*- coding: utf-8 -*-

import requests
from dotenv import load_dotenv
load_dotenv()
import os
import json

def split_input(input):
    url = "https://api.siliconflow.cn/v1/chat/completions"
    payload = {
        "model": "deepseek-ai/DeepSeek-V3",
        "messages": [
            {
                "role": "user",
                "content": f"请根据以下用户输入拆分出独立的问题，并按以下格式输出：第一个问题，第二个问题，...，第n个问题。 例如：提问：请你查询半导体和电车的新闻我需要判断股价，拆分结果：请你查询半导体的新闻，我需要判断股价，请你查询电车的新闻，我需要判断股价。请模型模仿上面的举例对下面的提问进行拆分：{input}，要求每个问题前面不要带上第几个问题的标识，直接输出问题逗号隔开，同时如果提问中包含时间要加到每个问题里面。"
            }
        ],
        "stream": False,
        "max_tokens": 512,
        "stop": ["null"],
        "temperature": 0.7,
        "top_p": 0.7,
        "top_k": 50,
        "frequency_penalty": 0.5,
        "n": 1,
        "response_format": {"type": "text"},
        "tools": [
            {
                "type": "function",
                "function": {
                    "description": "<string>",
                    "name": "<string>",
                    "parameters": {},
                    "strict": False
                }
            }
        ]
    }
    headers = {
        "Authorization": f"Bearer {os.getenv('split_input')}",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers) # str类型
    data = json.loads(response.text)
    content = data['choices'][0]["message"]['content']
    print(content)
    questions = content.replace("，", ",").split(",")  # 先替换中文逗号为英文逗号
    questions = [question.strip() for question in questions]
    return questions

if __name__ == "__main__":
    split_input("请你告诉我如何查询和阅读过去一年的财务报告，财务报告中哪些指标最重要")