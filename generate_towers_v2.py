#!/usr/bin/env python3
"""
使用阿里云DashScope生成命运塔游戏图片 - 正确异步版本
"""

import os
import json
import urllib.request
import time

# 塔列表
TOWERS = [
    ("01_egypt_pyramid", "埃及金字塔", "Egyptian Pyramid"),
    ("02_new_zealand_sky_tower", "新西兰天空塔", "Auckland Sky Tower"),
    ("03_brazil_christ_redeemer", "巴西基督像", "Christ the Redeemer statue"),
    ("04_mexico_chichen_itza", "墨西哥奇琴伊察", "Chichen Itza pyramid"),
    ("05_argentina_obelisk", "阿根廷方尖碑", "Obelisco de Buenos Aires"),
    ("06_peru_machu_picchu", "秘鲁马丘比丘", "Machu Picchu ancient citadel"),
    ("07_cuba_capitolio", "古巴国会大厦", "El Capitolio Havana"),
    ("08_south_africa_table_mountain", "南非桌山", "Table Mountain"),
    ("09_kenya_kilimanjaro", "肯尼亚乞力马扎罗", "Mount Kilimanjaro view"),
    ("10_morocco_hassan_mosque", "摩洛哥哈桑二世清真寺", "Hassan II Mosque"),
    ("11_norway_fjords", "挪威峡湾", "Norwegian Fjords"),
    ("12_greece_parthenon", "希腊帕特农神庙", "Parthenon temple"),
    ("13_czech_prague_old_town", "捷克布拉格广场", "Prague Old Town Square"),
    ("14_hungary_parliament", "匈牙利国会大厦", "Hungarian Parliament Building"),
    ("15_poland_warsaw_old_town", "波兰华沙老城", "Warsaw Old Town"),
    ("16_ukraine_sophia_cathedral", "乌克兰圣索菲亚大教堂", "Saint Sophia's Cathedral Kiev"),
]

def generate_prompt(english_name):
    """生成统一的风格化prompt"""
    return f"Angry Birds game style cartoon illustration of {english_name} as a cute character tower. The building has a kawaii face with big expressive eyes, a sweet smile, and pink blush on cheeks. Bright vibrant colors, rounded soft shapes, playful and cute aesthetic. Bright blue sky background with exactly 6 fluffy white cartoon clouds. Portrait orientation vertical, game asset style, clean vector-like illustration, high quality. No text, no letters, no watermarks."

def submit_task(prompt, api_key):
    """提交异步任务"""
    url = "https://dashscope.aliyuncs.com/api/v1/services/aigc/text2image/image-synthesis"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "X-DashScope-Async": "enable"
    }
    
    payload = {
        "model": "wanx2.1-t2i-turbo",
        "input": {
            "prompt": prompt
        },
        "parameters": {
            "size": "768*1344",
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
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        error_body = e.read().decode('utf-8')
        print(f"  HTTP Error {e.code}: {error_body}")
        return None
    except Exception as e:
        print(f"  Error: {e}")
        return None

def check_task(task_id, api_key):
    """查询任务状态"""
    url = f"https://dashscope.aliyuncs.com/api/v1/tasks/{task_id}"
    headers = {"Authorization": f"Bearer {api_key}"}
    
    req = urllib.request.Request(url, headers=headers)
    
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except Exception as e:
        print(f"  Error checking task: {e}")
        return None

def download_image(url, output_path):
    """下载图片"""
    try:
        urllib.request.urlretrieve(url, output_path)
        return True
    except Exception as e:
        print(f"  Download error: {e}")
        return False

def main():
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        print("Error: OPENAI_API_KEY not set")
        return
    
    output_dir = "/Users/moutai/.openclaw/workspace/towers_batch2"
    os.makedirs(output_dir, exist_ok=True)
    
    print("="*70)
    print("🗼 命运塔第二批图片生成 - 阿里云DashScope")
    print("="*70)
    
    # 提交所有任务
    tasks = []
    for filename, chinese_name, english_name in TOWERS:
        print(f"\n📤 提交: {chinese_name}")
        prompt = generate_prompt(english_name)
        result = submit_task(prompt, api_key)
        
        if result:
            task_id = result.get('output', {}).get('task_id')
            if task_id:
                print(f"   任务ID: {task_id}")
                tasks.append({
                    'task_id': task_id,
                    'filename': filename,
                    'chinese_name': chinese_name
                })
            else:
                print(f"   错误: 无task_id - {result}")
        else:
            print(f"   错误: 提交失败")
        
        time.sleep(0.5)  # 避免请求过快
    
    print(f"\n{'='*70}")
    print(f"✅ 已提交 {len(tasks)}/{len(TOWERS)} 个任务")
    print(f"⏳ 等待任务完成...")
    print("="*70)
    
    # 轮询等待任务完成
    completed = []
    failed = []
    max_wait = 600  # 最多等待10分钟
    waited = 0
    
    while tasks and waited < max_wait:
        for task in tasks[:]:
            result = check_task(task['task_id'], api_key)
            if not result:
                continue
            
            status = result.get('output', {}).get('task_status', 'UNKNOWN')
            
            if status == 'SUCCEEDED':
                results = result.get('output', {}).get('results', [])
                if results:
                    img_url = results[0].get('url')
                    if img_url:
                        output_path = os.path.join(output_dir, f"{task['filename']}.png")
                        if download_image(img_url, output_path):
                            print(f"✅ {task['chinese_name']} -> {task['filename']}.png")
                            completed.append(output_path)
                        else:
                            print(f"❌ 下载失败: {task['chinese_name']}")
                            failed.append(task['chinese_name'])
                    else:
                        print(f"❌ 无图片URL: {task['chinese_name']}")
                        failed.append(task['chinese_name'])
                tasks.remove(task)
                
            elif status == 'FAILED':
                error_msg = result.get('output', {}).get('message', 'Unknown error')
                print(f"❌ 失败: {task['chinese_name']} - {error_msg}")
                failed.append(task['chinese_name'])
                tasks.remove(task)
                
            elif status == 'CANCELLED':
                print(f"❌ 取消: {task['chinese_name']}")
                failed.append(task['chinese_name'])
                tasks.remove(task)
        
        if tasks:
            print(f"   等待中... {len(tasks)} 个任务未完成 (已等待 {waited}s)")
            time.sleep(10)
            waited += 10
    
    print("\n" + "="*70)
    print(f"🎉 完成！成功: {len(completed)} | 失败: {len(failed)}")
    print("="*70)
    
    if completed:
        print("\n✅ 成功文件列表:")
        for f in sorted(completed):
            print(f"   - {f}")
    
    if failed:
        print("\n❌ 失败列表:")
        for name in failed:
            print(f"   - {name}")

if __name__ == "__main__":
    main()
