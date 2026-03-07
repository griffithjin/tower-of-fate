#!/usr/bin/env python3
"""
生成命运塔游戏所需的卡通世界名塔图片
使用阿里云DashScope通义万相图像生成API
"""

import os
import json
import time
import urllib.request
from urllib.parse import urlencode

# API配置
API_KEY = os.environ.get("OPENAI_API_KEY")
BASE_URL = "https://dashscope.aliyuncs.com/api/v1/services/aigc/text2image/image-synthesis"

# 14个塔的生成配置
TOWERS = [
    {
        "name": "Big Ben",
        "name_cn": "大本钟",
        "country": "英国",
        "filename": "01_big_ben.png"
    },
    {
        "name": "Brandenburg Gate",
        "name_cn": "勃兰登堡门",
        "country": "德国",
        "filename": "02_brandenburg_gate.png"
    },
    {
        "name": "Sagrada Familia",
        "name_cn": "圣家堂",
        "country": "西班牙",
        "filename": "03_sagrada_familia.png"
    },
    {
        "name": "Dutch Windmill",
        "name_cn": "风车",
        "country": "荷兰",
        "filename": "04_dutch_windmill.png"
    },
    {
        "name": "Matterhorn",
        "name_cn": "马特洪峰",
        "country": "瑞士",
        "filename": "05_matterhorn.png"
    },
    {
        "name": "Red Square",
        "name_cn": "红场",
        "country": "俄罗斯",
        "filename": "06_red_square.png"
    },
    {
        "name": "Oriental Pearl Tower",
        "name_cn": "东方明珠",
        "country": "中国",
        "filename": "07_oriental_pearl.png"
    },
    {
        "name": "Taj Mahal",
        "name_cn": "泰姬陵",
        "country": "印度",
        "filename": "08_taj_mahal.png"
    },
    {
        "name": "Grand Palace",
        "name_cn": "大皇宫",
        "country": "泰国",
        "filename": "09_grand_palace.png"
    },
    {
        "name": "N Seoul Tower",
        "name_cn": "N首尔塔",
        "country": "韩国",
        "filename": "10_n_seoul_tower.png"
    },
    {
        "name": "Marina Bay Sands",
        "name_cn": "滨海湾金沙",
        "country": "新加坡",
        "filename": "11_marina_bay_sands.png"
    },
    {
        "name": "Burj Khalifa",
        "name_cn": "哈利法塔",
        "country": "阿联酋",
        "filename": "12_burj_khalifa.png"
    },
    {
        "name": "Blue Mosque",
        "name_cn": "蓝色清真寺",
        "country": "土耳其",
        "filename": "13_blue_mosque.png"
    },
    {
        "name": "CN Tower",
        "name_cn": "CN塔",
        "country": "加拿大",
        "filename": "14_cn_tower.png"
    }
]

def generate_prompt(tower):
    """生成图像提示词"""
    return f"""Angry Birds game style cartoon illustration of {tower['name']} ({tower['country']} famous landmark). 
Cute kawaii character design with big expressive eyes, sweet smile, and pink blush on cheeks. 
Bright vibrant colors, rounded soft shapes. 
The building is personified as a friendly adorable character with facial features. 
Bright blue sky background with exactly 6 fluffy white cartoon clouds. 
Portrait vertical composition, game asset style. 
Playful, whimsical, family-friendly, mobile game aesthetic.
Vivid cheerful color palette like Angry Birds games."""

def generate_image(tower, output_dir):
    """调用API生成单张图片"""
    prompt = generate_prompt(tower)
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
        "X-DashScope-Async": "enable"
    }
    
    payload = {
        "model": "wanx2.1-t2i-turbo",
        "input": {
            "prompt": prompt
        },
        "parameters": {
            "size": "768*1152",  # 竖版比例，使用星号分隔
            "n": 1
        }
    }
    
    data = json.dumps(payload).encode('utf-8')
    
    # 提交任务
    req = urllib.request.Request(
        BASE_URL,
        data=data,
        headers=headers,
        method='POST'
    )
    
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            result = json.loads(resp.read().decode('utf-8'))
            task_id = result.get('output', {}).get('task_id')
            
            if not task_id:
                print(f"❌ {tower['name_cn']}: 未能获取任务ID")
                return False
            
            print(f"🔄 {tower['name_cn']}: 任务已提交 (ID: {task_id})")
            
            # 等待任务完成
            return wait_for_result(task_id, tower, output_dir)
            
    except Exception as e:
        print(f"❌ {tower['name_cn']}: 请求失败 - {e}")
        return False

def wait_for_result(task_id, tower, output_dir, max_retries=30):
    """轮询任务结果"""
    query_url = f"https://dashscope.aliyuncs.com/api/v1/tasks/{task_id}"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    
    for i in range(max_retries):
        time.sleep(3)
        
        req = urllib.request.Request(query_url, headers=headers)
        
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                result = json.loads(resp.read().decode('utf-8'))
                status = result.get('output', {}).get('task_status')
                
                if status == 'SUCCEEDED':
                    # 下载图片
                    image_url = result.get('output', {}).get('results', [{}])[0].get('url')
                    if image_url:
                        return download_image(image_url, tower, output_dir)
                elif status == 'FAILED':
                    msg = result.get('output', {}).get('message', 'Unknown error')
                    print(f"❌ {tower['name_cn']}: 任务失败 - {msg}")
                    return False
                    
        except Exception as e:
            print(f"⚠️ {tower['name_cn']}: 查询失败 - {e}")
            
    print(f"⏱️ {tower['name_cn']}: 等待超时")
    return False

def download_image(url, tower, output_dir):
    """下载图片到本地"""
    filepath = os.path.join(output_dir, tower['filename'])
    
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.0'
        })
        
        with urllib.request.urlopen(req, timeout=60) as resp:
            with open(filepath, 'wb') as f:
                f.write(resp.read())
        
        file_size = os.path.getsize(filepath)
        print(f"✅ {tower['name_cn']}: 已保存 ({file_size//1024}KB) -> {filepath}")
        return True
        
    except Exception as e:
        print(f"❌ {tower['name_cn']}: 下载失败 - {e}")
        return False

def main():
    output_dir = "/Users/moutai/.openclaw/workspace/towers_batch1"
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"🎨 开始生成14个卡通世界名塔图片...")
    print(f"📁 保存目录: {output_dir}\n")
    
    success_count = 0
    
    for i, tower in enumerate(TOWERS, 1):
        print(f"\n[{i}/14] 正在生成: {tower['country']} - {tower['name_cn']} ({tower['name']})")
        
        if generate_image(tower, output_dir):
            success_count += 1
        
        # 每个请求间隔3秒
        if i < len(TOWERS):
            time.sleep(3)
    
    print(f"\n{'='*60}")
    print(f"✨ 生成完成! 成功: {success_count}/{len(TOWERS)}")
    print(f"📂 文件保存在: {output_dir}")
    
    # 列出所有文件
    files = sorted([f for f in os.listdir(output_dir) if f.endswith('.png')])
    if files:
        print(f"\n📋 生成的文件列表:")
        for f in files:
            print(f"   - {f}")
    
    return success_count == len(TOWERS)

if __name__ == '__main__':
    success = main()
    exit(0 if success else 1)
