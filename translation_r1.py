import requests
import os
from dotenv import load_dotenv
load_dotenv()
url = "https://api.siliconflow.cn/v1/chat/completions"
input = "悴んだ心 ふるえる眼差し世界で 僕は ひとりぼっちだった. Why play Haruhikage?"
payload = {
    "model": "Qwen/Qwen2.5-7B-Instruct", #先用个免费模型，之后记得改
    "messages": [
        {
            "role": "user",
            "content": "请将以下内容翻译成中文输出:"+input
        }
    ],
    "stream": False,
    "max_tokens": 512,
    "stop": None,
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
    "Authorization": "Bearer "+os.getenv('Deepseek_r1'),
    "Content-Type": "application/json"
}
response = requests.request("POST", url, json=payload, headers=headers)
result=response.json()
print(result['choices'][0]['message']['content'])