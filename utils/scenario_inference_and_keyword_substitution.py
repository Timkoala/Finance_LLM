# -*- coding: utf-8 -*-
import requests
from dotenv import load_dotenv
load_dotenv()
import os
import json

def scenario_inference_and_keyword_substitution(input):
    url = "https://api.siliconflow.cn/v1/chat/completions"
    payload = {
        "model": "deepseek-ai/DeepSeek-V3",
        "messages": [
            {
                "role": "user",
                "content": f"  请你从金融、经济和财务等相关领域去理解下面句子的含义，然后对错别字或词或句进行替换，最后返回输入。例如请你查询今年半导体公司的谷瓢信息，你的返回是请你查询今年半导体公司的股票信息。请你模仿上面的距离推断并修正下面的句子：{input}，要求只输出修正后的句子不输出额外的信息。同时，如果句子中不包含时间则加上时间，默认为过去一年，组成一个完整的句子。"
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
    return content

if __name__ == "__main__":
    scenario_inference_and_keyword_substitution("请你搜索财务处的保镖")