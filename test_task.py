#!/usr/bin/env python3
"""测试任务状态查询"""
import os
import json
import time
import urllib.request

API_KEY = os.environ.get("OPENAI_API_KEY")
task_id = "b5110a05-ea23-4b5a-91e0-87e1b4bb226a"

query_url = f"https://dashscope.aliyuncs.com/api/v1/tasks/{task_id}"
headers = {"Authorization": f"Bearer {API_KEY}"}

print(f"查询任务: {task_id}")
for i in range(10):
    time.sleep(3)
    req = urllib.request.Request(query_url, headers=headers)
    
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            result = json.loads(resp.read().decode('utf-8'))
            status = result.get('output', {}).get('task_status')
            print(f"[{i+1}] Status: {status}")
            print(f"    Full response: {json.dumps(result, indent=2, ensure_ascii=False)[:500]}")
            
            if status in ['SUCCEEDED', 'FAILED']:
                print(f"\n最终结果: {json.dumps(result, indent=2, ensure_ascii=False)}")
                break
    except Exception as e:
        print(f"[{i+1}] Error: {e}")
