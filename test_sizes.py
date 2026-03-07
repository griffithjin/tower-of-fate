#!/usr/bin/env python3
"""测试正确的size格式"""
import os
import json
import time
import urllib.request

API_KEY = os.environ.get("OPENAI_API_KEY")
BASE_URL = "https://dashscope.aliyuncs.com/api/v1/services/aigc/text2image/image-synthesis"

# 测试不同的size格式
sizes_to_test = [
    ("768*1152", "星号分隔"),
    ("1152*768", "星号分隔横版"),
    ("1024*1024", "正方形"),
    ("832*1216", "竖版常用"),
    ("1216*832", "横版常用"),
]

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}",
    "X-DashScope-Async": "enable"
}

for size, desc in sizes_to_test:
    print(f"\n{'='*50}")
    print(f"测试: {desc} -> {size}")
    
    payload = {
        "model": "wanx2.1-t2i-turbo",
        "input": {
            "prompt": "A cute cartoon tower with face, Angry Birds style, blue sky"
        },
        "parameters": {
            "size": size,
            "n": 1
        }
    }
    
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(BASE_URL, data=data, headers=headers, method='POST')
    
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            result = json.loads(resp.read().decode('utf-8'))
            task_id = result.get('output', {}).get('task_id')
            print(f"✅ 提交成功，任务ID: {task_id}")
            
            # 等待结果
            time.sleep(8)
            query_url = f"https://dashscope.aliyuncs.com/api/v1/tasks/{task_id}"
            req2 = urllib.request.Request(query_url, headers={"Authorization": f"Bearer {API_KEY}"})
            
            with urllib.request.urlopen(req2, timeout=30) as resp2:
                result2 = json.loads(resp2.read().decode('utf-8'))
                status = result2.get('output', {}).get('task_status')
                print(f"📊 状态: {status}")
                if status == 'FAILED':
                    msg = result2.get('output', {}).get('message')
                    print(f"❌ 失败原因: {msg}")
                elif status == 'SUCCEEDED':
                    print(f"✨ 成功! {size} 可用")
                    
    except Exception as e:
        print(f"❌ 错误: {e}")
    
    time.sleep(2)
