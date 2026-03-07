#!/usr/bin/env python3
"""
生成7张卡通化世界名塔图片 - 愤怒的小鸟风格
使用 DeepAI API (免费层)
"""

import os
import json
import requests
from pathlib import Path
import time

# 配置
OUTPUT_DIR = Path("/Users/moutai/Desktop/toweroffate_v1.0/assets/towers")
DEEPAI_API_KEY = os.environ.get("DEEPAI_API_KEY")

# 7个地标的配置
TOWERS = [
    {
        "filename": "sagrada-familia.png",
        "name": "Sagrada Familia",
        "display_name": "圣家堂",
        "description": "西班牙巴塞罗那圣家堂，独特的哥特式高塔，彩色玻璃窗"
    },
    {
        "filename": "windmill.png",
        "name": "Dutch Windmill",
        "display_name": "风车",
        "description": "荷兰传统风车，四片大叶片，茅草屋顶"
    },
    {
        "filename": "matterhorn.png",
        "name": "Matterhorn",
        "display_name": "马特洪峰",
        "description": "瑞士马特洪峰，金字塔形状雪山，标志性的尖顶"
    },
    {
        "filename": "red-square.png",
        "name": "Red Square",
        "display_name": "红场",
        "description": "俄罗斯莫斯科红场，圣瓦西里大教堂，彩色洋葱头圆顶"
    },
    {
        "filename": "n-tower.png",
        "name": "N Seoul Tower",
        "display_name": "N塔",
        "description": "韩国首尔N塔，山顶上的高塔，爱心锁"
    },
    {
        "filename": "marina-bay.png",
        "name": "Marina Bay Sands",
        "display_name": "滨海湾金沙",
        "description": "新加坡滨海湾金沙酒店，三塔结构，顶部有船型空中花园"
    },
    {
        "filename": "blue-mosque.png",
        "name": "Blue Mosque",
        "display_name": "蓝色清真寺",
        "description": "土耳其伊斯坦布尔蓝色清真寺，六个宣礼塔，蓝色瓷砖圆顶"
    }
]

def generate_prompt(tower):
    """生成提示词"""
    return f"""Cute cartoon illustration of {tower['name']} ({tower['description']}) in Angry Birds mobile game style. 

Art style: Angry Birds game aesthetic - vibrant colors, rounded shapes, playful and bouncy, cheerful cartoon style. 

Character design: The landmark building has a cute anthropomorphized face with big expressive eyes, cheerful smile, pink blush on cheeks, looking alive and friendly.

Background: Bright blue sky (clear vibrant azure), exactly 6 fluffy white cartoon clouds scattered in the sky.

Text banner at bottom: "Cartoon {tower['name']} / Angry Birds Style / Game Background"

Portrait orientation, tall composition, mobile game asset style, clean vector-like graphics, colorful and cheerful."""

def generate_image_deepai(prompt, output_path, api_key=None):
    """使用DeepAI生成图片"""
    # DeepAI 提供免费的文本到图像 API (有速率限制)
    url = "https://api.deepai.org/api/text2img"
    
    headers = {}
    if api_key:
        headers["api-key"] = api_key
    
    data = {
        "text": prompt,
        "image_generator": "hd"  # 高清模式
    }
    
    response = requests.post(url, headers=headers, data=data, timeout=120)
    
    if response.status_code == 200:
        result = response.json()
        if "output_url" in result:
            # 下载图片
            img_response = requests.get(result["output_url"], timeout=60)
            if img_response.status_code == 200:
                with open(output_path, "wb") as f:
                    f.write(img_response.content)
                return True
    else:
        print(f"Error: HTTP {response.status_code} - {response.text[:300]}")
    return False

def main():
    print("🎨 开始生成7张卡通世界名塔图片...")
    print(f"📁 输出目录: {OUTPUT_DIR}")
    print()
    
    # DeepAI 可以不用 API key (有限制)
    if DEEPAI_API_KEY:
        print("✅ 找到 DeepAI API Key")
    else:
        print("⚠️  未找到 DeepAI API Key，将使用免费模式（可能受限）")
    
    print()
    
    # 确保输出目录存在
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    results = []
    
    for i, tower in enumerate(TOWERS, 1):
        print(f"[{i}/7] 正在生成: {tower['display_name']} ({tower['filename']})")
        
        prompt = generate_prompt(tower)
        output_path = OUTPUT_DIR / tower["filename"]
        
        try:
            success = generate_image_deepai(prompt, output_path, DEEPAI_API_KEY)
            if success:
                file_size = output_path.stat().st_size
                print(f"   ✅ 成功保存: {output_path} ({file_size/1024:.1f} KB)")
                results.append({"tower": tower["name"], "status": "success", "file": str(output_path)})
            else:
                print(f"   ❌ 生成失败")
                results.append({"tower": tower["name"], "status": "failed"})
        except Exception as e:
            print(f"   ❌ 错误: {e}")
            results.append({"tower": tower["name"], "status": "error", "error": str(e)})
        
        # 添加延迟以避免请求过快 (免费模式需要等待)
        if i < len(TOWERS):
            time.sleep(10)  # DeepAI 免费模式需要较长的延迟
        print()
    
    # 输出总结
    print("=" * 50)
    print("📊 生成结果总结:")
    success_count = sum(1 for r in results if r["status"] == "success")
    print(f"   成功: {success_count}/{len(TOWERS)}")
    
    for r in results:
        icon = "✅" if r["status"] == "success" else "❌"
        print(f"   {icon} {r['tower']}")
    
    # 保存结果记录
    results_file = OUTPUT_DIR / "generation_results.json"
    with open(results_file, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\n📝 结果已保存到: {results_file}")

if __name__ == "__main__":
    main()
