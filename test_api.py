#!/usr/bin/env python3
"""调试测试阿里云图像生成API"""
import os
import json
import urllib.request

API_KEY = os.environ.get("OPENAI_API_KEY")
BASE_URL = "https://dashscope.aliyuncs.com/api/v1/services/aigc/text2image/image-synthesis"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}",
    "X-DashScope-Async": "enable"
}

payload = {
    "model": "wanx2.1-t2i-turbo",
    "input": {
        "prompt": "Angry Birds style cartoon Big Ben with cute face, blue sky with clouds"
    },
    "parameters": {
        "size": "768x1152",
        "n": 1
    }
}

data = json.dumps(payload).encode('utf-8')
req = urllib.request.Request(BASE_URL, data=data, headers=headers, method='POST')

try:
    with urllib.request.urlopen(req, timeout=60) as resp:
        print(f"Status: {resp.status}")
        result = json.loads(resp.read().decode('utf-8'))
        print(f"Response: {json.dumps(result, indent=2, ensure_ascii=False)}")
except urllib.error.HTTPError as e:
    print(f"HTTP Error {e.code}: {e.reason}")
    print(f"Response: {e.read().decode('utf-8')}")
except Exception as e:
    print(f"Error: {e}")
