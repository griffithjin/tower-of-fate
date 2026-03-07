#!/usr/bin/env python3
"""
生成巴基斯坦省卡通塔图片
风格：愤怒的小鸟卡通风格，可爱表情
"""

from PIL import Image, ImageDraw, ImageFilter
import math
import os

# 目标目录
OUTPUT_DIR = "/Users/moutai/Desktop/toweroffate_v1.0/assets/towers/states/pakistan/"

# 图片尺寸
WIDTH, HEIGHT = 800, 1200

# 颜色定义 - 愤怒的小鸟风格鲜艳色彩
SKY_TOP = (135, 206, 235)      # 天蓝（上）
SKY_BOTTOM = (200, 230, 255)   # 浅天蓝（下）

def create_gradient_background(width, height):
    """创建天蓝色渐变背景"""
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    
    for y in range(height):
        ratio = y / height
        r = int(SKY_TOP[0] * (1 - ratio) + SKY_BOTTOM[0] * ratio)
        g = int(SKY_TOP[1] * (1 - ratio) + SKY_BOTTOM[1] * ratio)
        b = int(SKY_TOP[2] * (1 - ratio) + SKY_BOTTOM[2] * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    return img

def draw_circle_body(draw, center_x, center_y, radius, color, outline_color=None):
    """绘制圆形身体（愤怒的小鸟风格）"""
    x1, y1 = center_x - radius, center_y - radius
    x2, y2 = center_x + radius, center_y + radius
    
    # 主体渐变效果
    for i in range(radius, 0, -1):
        ratio = i / radius
        r = int(color[0] * (0.7 + 0.3 * ratio))
        g = int(color[1] * (0.7 + 0.3 * ratio))
        b = int(color[2] * (0.7 + 0.3 * ratio))
        draw.ellipse([center_x - i, center_y - i, center_x + i, center_y + i], fill=(r, g, b))
    
    if outline_color:
        draw.ellipse([x1, y1, x2, y2], outline=outline_color, width=4)

def draw_cute_eyes(draw, center_x, center_y, eye_size=25, pupil_size=12):
    """绘制可爱的卡通眼睛"""
    # 左眼白
    draw.ellipse([center_x - 35, center_y - eye_size, center_x - 5, center_y + eye_size], 
                 fill=(255, 255, 255), outline=(0, 0, 0), width=3)
    # 右眼白
    draw.ellipse([center_x + 5, center_y - eye_size, center_x + 35, center_y + eye_size], 
                 fill=(255, 255, 255), outline=(0, 0, 0), width=3)
    
    # 左瞳孔（看向上方，显得可爱）
    draw.ellipse([center_x - 25, center_y - pupil_size - 5, center_x - 15, center_y - 5], 
                 fill=(0, 0, 0))
    # 右瞳孔
    draw.ellipse([center_x + 15, center_y - pupil_size - 5, center_x + 25, center_y - 5], 
                 fill=(0, 0, 0))
    
    # 高光
    draw.ellipse([center_x - 23, center_y - pupil_size - 3, center_x - 18, center_y - 8], 
                 fill=(255, 255, 255))
    draw.ellipse([center_x + 17, center_y - pupil_size - 3, center_x + 22, center_y - 8], 
                 fill=(255, 255, 255))

def draw_cute_mouth(draw, center_x, center_y, size=15):
    """绘制可爱的微笑嘴巴"""
    # 微笑弧线
    draw.arc([center_x - size, center_y - 5, center_x + size, center_y + size], 
             start=0, end=180, fill=(0, 0, 0), width=3)
    # 小舌头
    draw.pieslice([center_x - 8, center_y, center_x + 8, center_y + 12], 
                  start=0, end=180, fill=(255, 100, 100))

def draw_cheeks(draw, center_x, center_y):
    """绘制腮红"""
    draw.ellipse([center_x - 60, center_y + 10, center_x - 30, center_y + 40], 
                 fill=(255, 150, 150, 128))
    draw.ellipse([center_x + 30, center_y + 10, center_x + 60, center_y + 40], 
                 fill=(255, 150, 150, 128))

def draw_clouds(img, draw):
    """绘制装饰云朵"""
    cloud_color = (255, 255, 255, 180)
    clouds = [
        (150, 150, 80), (650, 200, 60), (100, 400, 50),
        (700, 500, 70), (200, 800, 55), (600, 900, 65)
    ]
    for x, y, r in clouds:
        draw.ellipse([x-r, y-r//2, x+r, y+r//2], fill=(255, 255, 255))
        draw.ellipse([x-r//2, y-r, x+r//2, y+r//3], fill=(255, 255, 255))

# ============ 各省份塔绘制函数 ============

def draw_badshahi_mosque():
    """1. 旁遮普 - 巴德夏希清真寺 - 红色圆顶卡通风格"""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    draw_clouds(img, draw)
    
    center_x, center_y = WIDTH // 2, HEIGHT // 2 + 100
    
    # 身体 - 橙红色（清真寺砖色）
    body_color = (210, 105, 30)
    draw_circle_body(draw, center_x, center_y, 200, body_color, (139, 69, 19))
    
    # 三个圆顶（像皇冠）
    dome_color = (255, 215, 0)  # 金色
    # 中间大圆顶
    draw.ellipse([center_x - 80, center_y - 280, center_x + 80, center_y - 120], 
                 fill=dome_color, outline=(218, 165, 32), width=4)
    # 两侧小圆顶
    draw.ellipse([center_x - 160, center_y - 220, center_x - 60, center_y - 130], 
                 fill=dome_color, outline=(218, 165, 32), width=3)
    draw.ellipse([center_x + 60, center_y - 220, center_x + 160, center_y - 130], 
                 fill=dome_color, outline=(218, 165, 32), width=3)
    
    # 尖塔
    tower_color = (210, 105, 30)
    draw.polygon([(center_x - 180, center_y - 50), (center_x - 160, center_y - 250), 
                  (center_x - 140, center_y - 50)], fill=tower_color, outline=(139, 69, 19), width=3)
    draw.polygon([(center_x + 140, center_y - 50), (center_x + 160, center_y - 250), 
                  (center_x + 180, center_y - 50)], fill=tower_color, outline=(139, 69, 19), width=3)
    
    # 面部
    draw_cute_eyes(draw, center_x, center_y - 30)
    draw_cute_mouth(draw, center_x, center_y + 30)
    draw_cheeks(draw, center_x, center_y)
    
    return img

def draw_thatta():
    """2. 信德 - 塔塔古城 - 蓝瓷砖风格"""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    draw_clouds(img, draw)
    
    center_x, center_y = WIDTH // 2, HEIGHT // 2 + 100
    
    # 身体 - 青蓝色（瓷砖色）
    body_color = (0, 150, 200)
    draw_circle_body(draw, center_x, center_y, 190, body_color, (0, 100, 150))
    
    # 蓝瓷砖图案
    for i in range(-150, 151, 30):
        for j in range(-150, 151, 30):
            if i*i + j*j < 180*180:
                tile_color = (0, 180, 220) if (i+j) % 60 == 0 else (0, 120, 180)
                draw.rectangle([center_x + i, center_y + j, center_x + i + 25, center_y + j + 25], 
                              fill=tile_color, outline=(255, 255, 255), width=1)
    
    # 圆顶
    draw.ellipse([center_x - 100, center_y - 300, center_x + 100, center_y - 100], 
                 fill=(0, 200, 255), outline=(0, 150, 200), width=4)
    
    # 面部
    draw_cute_eyes(draw, center_x, center_y - 20)
    draw_cute_mouth(draw, center_x, center_y + 40)
    draw_cheeks(draw, center_x, center_y)
    
    return img

def draw_peshawar():
    """3. 开伯尔-普什图 - 白沙瓦 - 古城门风格"""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    draw_clouds(img, draw)
    
    center_x, center_y = WIDTH // 2, HEIGHT // 2 + 100
    
    # 身体 - 土黄色（古城墙色）
    body_color = (194, 178, 128)
    draw_circle_body(draw, center_x, center_y, 200, body_color, (160, 140, 90))
    
    # 城门造型
    gate_color = (139, 90, 43)
    # 拱形门
    draw.pieslice([center_x - 80, center_y + 50, center_x + 80, center_y + 200], 
                  start=0, end=180, fill=gate_color)
    # 城垛
    for i in range(-180, 181, 40):
        if abs(i) < 170:
            draw.rectangle([center_x + i, center_y - 220, center_x + i + 30, center_y - 180], 
                          fill=gate_color, outline=(100, 70, 30), width=2)
    
    # 面部
    draw_cute_eyes(draw, center_x, center_y - 40, eye_size=22)
    draw_cute_mouth(draw, center_x, center_y + 20)
    draw_cheeks(draw, center_x, center_y - 10)
    
    return img

def draw_gwadar():
    """4. 俾路支 - 瓜达尔港 - 海洋港口风格"""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    draw_clouds(img, draw)
    
    center_x, center_y = WIDTH // 2, HEIGHT // 2 + 100
    
    # 身体 - 海蓝色
    body_color = (0, 119, 190)
    draw_circle_body(draw, center_x, center_y, 195, body_color, (0, 80, 140))
    
    # 起重机/港口元素
    crane_color = (255, 165, 0)  # 橙色
    # 起重机臂
    draw.rectangle([center_x - 20, center_y - 350, center_x + 20, center_y - 150], 
                  fill=crane_color, outline=(200, 130, 0), width=3)
    draw.rectangle([center_x - 20, center_y - 350, center_x + 120, center_y - 310], 
                  fill=crane_color, outline=(200, 130, 0), width=3)
    # 吊钩
    draw.arc([center_x + 100, center_y - 310, center_x + 140, center_y - 250], 
             start=0, end=180, fill=(100, 100, 100), width=4)
    
    # 波浪图案
    for i in range(-170, 171, 35):
        draw.arc([center_x + i, center_y + 80, center_x + i + 35, center_y + 130], 
                start=0, end=180, fill=(0, 200, 255), width=4)
    
    # 面部
    draw_cute_eyes(draw, center_x, center_y - 30)
    draw_cute_mouth(draw, center_x, center_y + 30)
    draw_cheeks(draw, center_x, center_y)
    
    return img

def draw_faisal():
    """5. 伊斯兰堡 - 费萨尔清真寺 - 现代白色风格"""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    draw_clouds(img, draw)
    
    center_x, center_y = WIDTH // 2, HEIGHT // 2 + 100
    
    # 身体 - 纯白色
    body_color = (245, 245, 245)
    draw_circle_body(draw, center_x, center_y, 200, body_color, (200, 200, 200))
    
    # 四个尖塔（费萨尔清真寺特色）
    tower_color = (220, 220, 220)
    positions = [(-160, -200), (160, -200), (-120, -280), (120, -280)]
    for dx, dy in positions:
        # 尖塔
        draw.polygon([
            (center_x + dx - 20, center_y + dy + 100),
            (center_x + dx, center_y + dy - 100),
            (center_x + dx + 20, center_y + dy + 100)
        ], fill=tower_color, outline=(180, 180, 180), width=3)
        # 尖顶
        draw.polygon([
            (center_x + dx, center_y + dy - 100),
            (center_x + dx - 10, center_y + dy - 140),
            (center_x + dx + 10, center_y + dy - 140)
        ], fill=(255, 215, 0), outline=(218, 165, 32), width=2)
    
    # 大圆顶
    draw.ellipse([center_x - 100, center_y - 280, center_x + 100, center_y - 80], 
                 fill=(240, 240, 240), outline=(200, 200, 200), width=4)
    
    # 面部
    draw_cute_eyes(draw, center_x, center_y - 20)
    draw_cute_mouth(draw, center_x, center_y + 40)
    draw_cheeks(draw, center_x, center_y)
    
    return img

def draw_neelum():
    """6. 自由克什米尔 - 尼拉姆山谷 - 绿色山谷风格"""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    draw_clouds(img, draw)
    
    center_x, center_y = WIDTH // 2, HEIGHT // 2 + 100
    
    # 身体 - 绿色（山谷）
    body_color = (34, 139, 34)
    draw_circle_body(draw, center_x, center_y, 200, body_color, (20, 100, 20))
    
    # 山峰（背景）
    mountain_color = (100, 149, 237)
    draw.polygon([
        (center_x - 200, center_y - 100),
        (center_x - 100, center_y - 350),
        (center_x, center_y - 200),
        (center_x + 100, center_y - 380),
        (center_x + 200, center_y - 100)
    ], fill=mountain_color, outline=(70, 130, 180), width=3)
    # 山顶白雪
    draw.polygon([
        (center_x - 80, center_y - 320),
        (center_x - 100, center_y - 350),
        (center_x - 60, center_y - 300)
    ], fill=(255, 255, 255))
    draw.polygon([
        (center_x + 80, center_y - 350),
        (center_x + 100, center_y - 380),
        (center_x + 120, center_y - 330)
    ], fill=(255, 255, 255))
    
    # 河流
    draw.pieslice([center_x - 150, center_y + 50, center_x + 150, center_y + 180], 
                  start=0, end=180, fill=(0, 191, 255))
    
    # 面部
    draw_cute_eyes(draw, center_x, center_y - 10)
    draw_cute_mouth(draw, center_x, center_y + 50)
    draw_cheeks(draw, center_x, center_y + 10)
    
    return img

def draw_k2():
    """7. 吉尔吉特-巴尔蒂斯坦 - 乔戈里峰(K2) - 雪山风格"""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    draw_clouds(img, draw)
    
    center_x, center_y = WIDTH // 2, HEIGHT // 2 + 100
    
    # 身体 - 冰蓝色
    body_color = (176, 196, 222)
    draw_circle_body(draw, center_x, center_y, 200, body_color, (130, 160, 190))
    
    # K2山峰 - 世界第二高峰
    # 主峰
    peak_color = (220, 220, 240)
    snow_color = (255, 255, 255)
    
    # 主峰三角形
    draw.polygon([
        (center_x - 180, center_y - 50),
        (center_x, center_y - 450),
        (center_x + 180, center_y - 50)
    ], fill=peak_color, outline=(180, 180, 200), width=4)
    
    # 山顶积雪
    draw.polygon([
        (center_x - 80, center_y - 280),
        (center_x, center_y - 450),
        (center_x + 80, center_y - 280),
        (center_x + 40, center_y - 250),
        (center_x, center_y - 300),
        (center_x - 40, center_y - 250)
    ], fill=snow_color, outline=(200, 200, 220), width=2)
    
    # 雪线纹理
    for i in range(-120, 121, 40):
        y_pos = center_y - 200 + abs(i) * 0.3
        draw.line([(center_x + i, y_pos), (center_x + i + 30, y_pos - 10)], 
                 fill=(255, 255, 255), width=3)
    
    # 面部
    draw_cute_eyes(draw, center_x, center_y - 20)
    draw_cute_mouth(draw, center_x, center_y + 40)
    draw_cheeks(draw, center_x, center_y)
    
    return img

# ============ 主程序 ============

def main():
    # 确保输出目录存在
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # 定义所有塔
    towers = [
        ("punjab-badshahi.png", draw_badshahi_mosque, "旁遮普 - 巴德夏希清真寺"),
        ("sindh-thatta.png", draw_thatta, "信德 - 塔塔古城"),
        ("kpk-peshawar.png", draw_peshawar, "开伯尔-普什图 - 白沙瓦"),
        ("balochistan-gwadar.png", draw_gwadar, "俾路支 - 瓜达尔港"),
        ("islamabad-faisal.png", draw_faisal, "伊斯兰堡 - 费萨尔清真寺"),
        ("ajk-neelum.png", draw_neelum, "自由克什米尔 - 尼拉姆山谷"),
        ("gilgit-k2.png", draw_k2, "吉尔吉特-巴尔蒂斯坦 - 乔戈里峰"),
    ]
    
    print("🎨 开始生成巴基斯坦省卡通塔图片...")
    print("=" * 50)
    
    for filename, draw_func, name in towers:
        print(f"正在生成: {name}...")
        img = draw_func()
        filepath = os.path.join(OUTPUT_DIR, filename)
        img.save(filepath, "PNG", quality=95)
        print(f"  ✓ 已保存: {filepath}")
    
    print("=" * 50)
    print(f"✅ 全部7个图片生成完成！")
    print(f"📁 保存位置: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
