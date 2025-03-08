from tavily import TavilyClient
from dotenv import load_dotenv
import os, requests
from utils.scenario_inference_and_keyword_substitution import scenario_inference_and_keyword_substitution
from utils.split_input import split_input
from utils.analyze_question import analyze_question
load_dotenv()

# # 查询
# input = "Who is the most important princi in market economics and the most important indicator in financial sheet?"
# input = scenario_inference_and_keyword_substitution(input)
# questions = split_input(input) # <class 'list'>
# keyword_list, domain_list, time_list = zip(*[analyze_question(question) for question in questions])
# # 将元组转换为列表
# keyword1_list = list(keyword_list) # ['principle', 'indicator']
# domain_list = list(domain_list) # ['market economics', 'financial sheet']
# time_list = list(time_list) # ['past year', 'past year']


url = "https://api.tavily.com/search"

payload = {
    "query": input,
    "topic": "",
    "search_depth": "basic",
    "max_results": 1,
    "time_range": None,
    "days": 3,
    "include_answer": True,
    "include_raw_content": False,
    "include_images": False,
    "include_image_descriptions": False,
    "include_domains": [],
    "exclude_domains": []
}
headers = {
    "Authorization": f"Bearer {os.getenv('TAVILY_API_KEY')}",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)
response = response.json()
print(f"title={response['results'][0]['title']}\n")
print(f"url={response['results'][0]['url']}\n")
print(f"content={response['results'][0]['content']}\n")
print(f"answer={response['answer']}\n")


# 基于哈希和语义的去重
# unique_results = []
# seen = set()
# for result in response['results']:
#     # 将字典转换为元组，以便进行哈希比较
#     result_tuple = tuple(sorted(result.items()))
#     if result_tuple not in seen:
#         seen.add(result_tuple)
#         unique_results.append(result)
# response['results'] = unique_results


# 打印查询结果
# print(response)
# print("\n查询内容:")
# print(response['query'])
# print("\n后续问题:")
# print(response['follow_up_questions'])
# print("\n答案:")
# print(response['answer'])
# print("\n查询结果:")
# for i, result in enumerate(response['results'], start=1):
#     print(f"  结果 {i}:")
#     print(f"    标题: {result['title']}")
#     print(f"    链接: {result['url']}")
#     print(f"    内容: {result['content']}")
#     print(f"    得分: {result['score']}")
#     print(f"    原始内容: {result['raw_content']}")
# print("\n响应时间:")
# print(response['response_time'])