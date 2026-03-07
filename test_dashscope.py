#!/usr/bin/env python3
"""
使用阿里云DashScope生成命运塔游戏图片 - 同步调用版本
"""

import os
import json
import urllib.request
import time

# 塔列表
TOWERS = [
    ("01_egypt_pyramid", "埃及金字塔", "Egyptian Pyramid"),
]

def generate_prompt(english_name):
    """生成统一的风格化prompt"""
    return f"Angry Birds game style cartoon illustration of {english_name} as a cute character tower. The building has a kawaii face with big expressive eyes, a sweet smile, and pink blush on cheeks. Bright vibrant colors, rounded soft shapes, playful and cute aesthetic. Bright blue sky background with exactly 6 fluffy white cartoon clouds. Portrait orientation vertical, game asset style, clean vector-like illustration, high quality. No text, no letters, no watermarks."

def generate_image_sync(prompt, api_key):
    """使用DashScope同步生成图片"""
    url = "https://dashscope.aliyuncs.com/api/v1/services/aigc/text2image/image-synthesis"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "wanx2.1-t2i-turbo",
        "input": {
            "prompt": prompt
        },
        "parameters": {
            "size": "1024*1536",
            "n": 1
        }
    }
    
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode('utf-8'),
        headers=headers,
        method='POST'
    )
    
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            result = json.loads(resp.read().decode('utf-8'))
            return result
    except urllib.error.HTTPError as e:
        error_body = e.read().decode('utf-8')
        print(f"HTTP Error {e.code}: {error_body}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        print("Error: OPENAI_API_KEY not set")
        return
    
    output_dir = "/Users/moutai/.openclaw/workspace/towers_batch2"
    os.makedirs(output_dir, exist_ok=True)
    
    # 只测试一个
    filename, chinese_name, english_name = TOWERS[0]
    print(f"测试生成: {chinese_name}")
    prompt = generate_prompt(english_name)
    print(f"Prompt: {prompt[:100]}...")
    
    result = generate_image_sync(prompt, api_key)
    print(f"\n结果:\n{json.dumps(result, indent=2, ensure_ascii=False)}")

if __name__ == "__main__":
    main()
