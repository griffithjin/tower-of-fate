#!/usr/bin/env python3
"""
生成命运塔游戏第二批世界名塔图片
愤怒的小鸟风格，竖版800x1200
"""

import os
import subprocess
import json

# 塔列表
TOWERS = [
    ("egypt_pyramid", "埃及金字塔", "Egyptian Pyramid"),
    ("new_zealand_sky_tower", "新西兰天空塔", "Auckland Sky Tower"),
    ("brazil_christ_redeemer", "巴西基督像", "Christ the Redeemer statue"),
    ("mexico_chichen_itza", "墨西哥奇琴伊察", "Chichen Itza pyramid"),
    ("argentina_obelisk", "阿根廷方尖碑", "Obelisco de Buenos Aires"),
    ("peru_machu_picchu", "秘鲁马丘比丘", "Machu Picchu ancient citadel"),
    ("cuba_capitolio", "古巴国会大厦", "El Capitolio Havana"),
    ("south_africa_table_mountain", "南非桌山", "Table Mountain"),
    ("kenya_kilimanjaro", "肯尼亚乞力马扎罗", "Mount Kilimanjaro view"),
    ("morocco_hassan_mosque", "摩洛哥哈桑二世清真寺", "Hassan II Mosque"),
    ("norway_fjords", "挪威峡湾", "Norwegian Fjords"),
    ("greece_parthenon", "希腊帕特农神庙", "Parthenon temple"),
    ("czech_prague_old_town", "捷克布拉格广场", "Prague Old Town Square"),
    ("hungary_parliament", "匈牙利国会大厦", "Hungarian Parliament Building"),
    ("poland_warsaw_old_town", "波兰华沙老城", "Warsaw Old Town"),
    ("ukraine_sophia_cathedral", "乌克兰圣索菲亚大教堂", "Saint Sophia's Cathedral Kiev"),
]

def generate_prompt(english_name):
    """生成统一的风格化prompt"""
    return f"""Angry Birds game style cartoon illustration of {english_name} as a cute character tower.
The building has a kawaii face with big expressive eyes, a sweet smile, and pink blush on cheeks.
Bright vibrant colors, rounded soft shapes, playful and cute aesthetic.
Bright blue sky background with exactly 6 fluffy white cartoon clouds.
Portrait orientation (tall), game asset style, clean vector-like illustration.
No text, no letters, no watermarks."""

def main():
    output_dir = "/Users/moutai/.openclaw/workspace/towers_batch2"
    os.makedirs(output_dir, exist_ok=True)
    
    # 获取脚本路径
    script_path = os.path.expanduser("~/.npm/_npx/8718c3904bb5fece/node_modules/openclaw/skills/openai-image-gen/scripts/gen.py")
    
    generated_files = []
    
    for filename, chinese_name, english_name in TOWERS:
        print(f"\n🗼 正在生成: {chinese_name} ({english_name})")
        
        prompt = generate_prompt(english_name)
        file_prefix = f"{filename}"
        
        cmd = [
            "python3", script_path,
            "--prompt", prompt,
            "--count", "1",
            "--model", "gpt-image-1",
            "--size", "1024x1536",  # 竖版，接近800x1200比例
            "--quality", "high",
            "--out-dir", output_dir,
        ]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            
            if result.returncode == 0:
                print(f"   ✅ 成功生成: {chinese_name}")
                # 查找生成的文件
                for f in os.listdir(output_dir):
                    if f.startswith(file_prefix) or f.endswith('.png') or f.endswith('.webp'):
                        full_path = os.path.join(output_dir, f)
                        if full_path not in generated_files:
                            generated_files.append(full_path)
                            break
            else:
                print(f"   ❌ 失败: {chinese_name}")
                print(f"   错误: {result.stderr}")
                
        except Exception as e:
            print(f"   ❌ 异常: {chinese_name} - {e}")
    
    print(f"\n{'='*60}")
    print(f"🎉 批量生成完成！共生成 {len(generated_files)} 张图片")
    print(f"{'='*60}")
    print("\n生成的文件列表:")
    for f in sorted(generated_files):
        print(f"  - {f}")

if __name__ == "__main__":
    main()
