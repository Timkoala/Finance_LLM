# -*- coding: utf-8 -*-
import requests
from dotenv import load_dotenv
load_dotenv()
import os
import json

def analyze_question(question):
    url = "https://api.siliconflow.cn/v1/chat/completions"
    payload = {
        "model": "deepseek-ai/DeepSeek-V3",
        "messages": [
            {
                "role": "user",
                "content": f"根据下面句子中的关键词选择一个最重要的两个关键词，一个是问题的核心和一个是涉及的时间范围，同时输出问题查询的时间范围。例如“what factors will affect economic in next year” 中问题的核心是factors，涉及的领域是economic，时间范围是next year。句子：{question} 中的两个关键词和时间要求是什么。要求你的输出只需要答案，输出第一个关键词，第二个关键词和时间范围（没有就默认过去一年）。不需要其他的文字内容，按照下面格式输出：第一个关键词，第二个关键词，时间范围"
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
        "Authorization": f"Bearer {os.getenv('analyze_question')}",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers) # str类型
    data = json.loads(response.text)
    content = data['choices'][0]["message"]['content']
    print(content)
    keywords = content.replace("，", ",").split(",")  # 先替换中文逗号为英文逗号，然后分割
    if len(keywords) == 3:
        keyword1 = keywords[0].strip()  # 去掉多余的空格
        keyword2 = keywords[1].strip()  # 去掉多余的空格
        keyword3 = keywords[2].strip()  # 去掉多余的空格
        print(f"关键词1: {keyword1}")
        print(f"关键词2: {keyword2}")
        print(f"关键词3: {keyword3}")
        return keyword1, keyword2, keyword3
    else:
        print("无法提取三个关键词")

if __name__ == "__main__":
    analyze_question("请你查询半导体的新闻我需要判断股价")