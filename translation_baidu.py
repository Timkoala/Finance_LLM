# -*- coding: utf-8 -*-
# This code runs on Python 2.7.x and Python 3.x.
# You may install `requests` to run this code: pip install requests
# Please refer to `https://api.fanyi.baidu.com/doc/21` for complete api document
import os
import requests
import random
import json
from hashlib import md5
from dotenv import load_dotenv
load_dotenv()
# Set your own appid/appkey.
appid = os.getenv('Baidu_App_Id')
appkey = os.getenv('Baidu_App_Key')
# For list of language codes, please refer to `https://api.fanyi.baidu.com/doc/21`
from_lang = ''
to_lang =  'zh'

endpoint = 'http://api.fanyi.baidu.com'
path1 = '/api/trans/vip/language' #语种识别
path2 = '/api/trans/vip/translate'#翻译
url = endpoint + path1

input = '悴んだ心 ふるえる眼差し世界で 僕は ひとりぼっちだった'

# Generate salt and sign
def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()

salt = random.randint(32768, 65536)
sign = make_md5(appid + input + str(salt) + appkey)
# Build request
#需要先进行语种识别
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
payload = {'q': input,'appid': appid, 'salt': salt, 'sign': sign}
r = requests.post(url, params=payload, headers=headers)
result = r.json()
from_lang = result['data']['src'] #把识别到的语种存起来


url = endpoint + path2 #开始着手翻译
payload = {'appid': appid, 'q': input, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}

# Send request
r = requests.post(url, params=payload, headers=headers)
result = r.json()
# print(result)
# Show response
# print(f"src={result['trans_result'][0]['src']}\n")
print(f"text={result['trans_result'][0]['dst']}\n")