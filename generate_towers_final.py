#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成8个卡通化世界名塔图片
风格：愤怒的小鸟卡通风格，可爱表情
"""

from PIL import Image, ImageDraw, ImageFont
import math
import os

# 配置
WIDTH, HEIGHT = 800, 1200
OUTPUT_DIR = "/Users/moutai/Desktop/toweroffate_v1.0/assets/towers/"

# 颜色定义
SKY_TOP = (135, 206, 250)      # 天蓝色
SKY_BOTTOM = (224, 247, 250)   # 浅天蓝色
WHITE = (255, 255, 255)
BLACK = (30, 30, 30)
DARK_BROWN = (101, 67, 33)
LIGHT_BROWN = (139, 90, 43)
RED = (220, 50, 50)
GREEN = (50, 150, 50)
BLUE = (50, 100, 200)
YELLOW = (255, 220, 50)
ORANGE = (255, 150, 50)
GRAY = (120, 120, 120)
LIGHT_GRAY = (180, 180, 180)
DARK_GRAY = (80, 80, 80)
GOLD = (255, 215, 0)
CREAM = (255, 248, 220)
PINK = (255, 182, 193)

def create_gradient_background():
    """创建天蓝色渐变背景"""
    img = Image.new('RGB', (WIDTH, HEIGHT), SKY_TOP)
    draw = ImageDraw.Draw(img)
    
    for y in range(HEIGHT):
        ratio = y / HEIGHT
        r = int(SKY_TOP[0] * (1 - ratio) + SKY_BOTTOM[0] * ratio)
        g = int(SKY_TOP[1] * (1 - ratio) + SKY_BOTTOM[1] * ratio)
        b = int(SKY_TOP[2] * (1 - ratio) + SKY_BOTTOM[2] * ratio)
        draw.line([(0, y), (WIDTH, y)], fill=(r, g, b))
    
    return img

def draw_cloud(draw, x, y, size=1.0):
    """绘制卡通云朵"""
    s = size
    draw.ellipse([x-30*s, y-20*s, x+30*s, y+20*s], fill=WHITE, outline=BLACK, width=2)
    draw.ellipse([x-15*s, y-25*s, x+15*s, y+10*s], fill=WHITE, outline=BLACK, width=2)
    draw.ellipse([x-45*s, y-15*s, x-10*s, y+15*s], fill=WHITE, outline=BLACK, width=2)
    draw.ellipse([x+10*s, y-15*s, x+45*s, y+15*s], fill=WHITE, outline=BLACK, width=2)

def draw_eyes(draw, x, y, size=1.0, expression="happy"):
    """绘制卡通眼睛"""
    s = size
    # 左眼白
    draw.ellipse([x-25*s, y-15*s, x-5*s, y+15*s], fill=WHITE, outline=BLACK, width=2)
    # 右眼白
    draw.ellipse([x+5*s, y-15*s, x+25*s, y+15*s], fill=WHITE, outline=BLACK, width=2)
    
    # 瞳孔
    draw.ellipse([x-18*s, y-5*s, x-10*s, y+8*s], fill=BLACK)
    draw.ellipse([x+10*s, y-5*s, x+18*s, y+8*s], fill=BLACK)
    
    # 高光
    draw.ellipse([x-16*s, y-3*s, x-12*s, y+3*s], fill=WHITE)
    draw.ellipse([x+12*s, y-3*s, x+16*s, y+3*s], fill=WHITE)
    
    # 表情
    if expression == "happy":
        draw.arc([x-20*s, y-5*s, x-8*s, y+12*s], start=0, end=180, fill=BLACK, width=2)
        draw.arc([x+8*s, y-5*s, x+20*s, y+12*s], start=0, end=180, fill=BLACK, width=2)
    elif expression == "wink":
        draw.arc([x-20*s, y-5*s, x-8*s, y+12*s], start=0, end=180, fill=BLACK, width=2)
        draw.line([x+8*s, y, x+20*s, y+5*s], fill=BLACK, width=2)

def draw_smile(draw, x, y, size=1.0):
    """绘制微笑"""
    s = size
    draw.arc([x-20*s, y-10*s, x+20*s, y+20*s], start=0, end=180, fill=BLACK, width=3)
    # 腮红
    draw.ellipse([x-35*s, y+5*s, x-20*s, y+20*s], fill=PINK)
    draw.ellipse([x+20*s, y+5*s, x+35*s, y+20*s], fill=PINK)

def draw_santa_village():
    """1. 芬兰 - 圣诞老人村"""
    img = create_gradient_background()
    draw = ImageDraw.Draw(img)
    
    # 云朵
    draw_cloud(draw, 150, 150, 0.8)
    draw_cloud(draw, 600, 200, 1.0)
    draw_cloud(draw, 400, 100, 0.6)
    
    # 雪地
    draw.ellipse([0, 800, WIDTH, HEIGHT+200], fill=WHITE, outline=BLACK, width=2)
    
    # 圣诞树
    for tx in [150, 650]:
        # 树干
        draw.rectangle([tx-15, 750, tx+15, 850], fill=DARK_BROWN, outline=BLACK, width=2)
        # 树叶层
        draw.polygon([tx, 550, tx-60, 700, tx+60, 700], fill=GREEN, outline=BLACK, width=2)
        draw.polygon([tx, 620, tx-50, 750, tx+50, 750], fill=GREEN, outline=BLACK, width=2)
        # 装饰
        for dx, dy in [(-20, 600), (20, 620), (0, 650), (-25, 680), (25, 690)]:
            draw.ellipse([tx+dx-8, dy-8, tx+dx+8, dy+8], fill=RED)
    
    # 圣诞老人小屋
    cx, cy = 400, 700
    # 主体
    draw.rectangle([cx-120, cy-50, cx+120, cy+150], fill=RED, outline=BLACK, width=3)
    # 屋顶
    draw.polygon([cx-140, cy-50, cx, cy-180, cx+140, cy-50], fill=WHITE, outline=BLACK, width=3)
    # 门
    draw.rounded_rectangle([cx-30, cy+30, cx+30, cy+150], radius=15, fill=DARK_BROWN, outline=BLACK, width=2)
    draw.ellipse([cx-15, cy+50, cx+15, cy+80], fill=BLACK)  # 眼睛
    draw.arc([cx-10, cy+70, cx+10, cy+95], start=0, end=180, fill=BLACK, width=3)  # 微笑
    # 窗户
    draw.rectangle([cx-90, cy, cx-50, cy+50], fill=YELLOW, outline=BLACK, width=2)
    draw.rectangle([cx+50, cy, cx+90, cy+50], fill=YELLOW, outline=BLACK, width=2)
    # 烟囱
    draw.rectangle([cx+80, cy-140, cx+110, cy-80], fill=DARK_BROWN, outline=BLACK, width=2)
    # 烟雾
    draw.ellipse([cx+85, cy-170, cx+105, cy-145], fill=LIGHT_GRAY, outline=BLACK, width=1)
    draw.ellipse([cx+90, cy-200, cx+115, cy-175], fill=LIGHT_GRAY, outline=BLACK, width=1)
    
    return img

def draw_cliffs_of_moher():
    """2. 爱尔兰 - 莫赫悬崖"""
    img = create_gradient_background()
    draw = ImageDraw.Draw(img)
    
    # 云朵
    draw_cloud(draw, 200, 120, 0.9)
    draw_cloud(draw, 550, 180, 0.7)
    
    # 海洋
    draw.rectangle([0, 700, WIDTH, HEIGHT], fill=(50, 100, 150), outline=BLACK, width=2)
    # 波浪
    for i in range(8):
        x = 100 * i
        draw.arc([x, 680, x+80, 720], start=0, end=180, fill=WHITE, width=2)
    
    # 悬崖左峰
    cliff_points = [(100, 900), (150, 400), (280, 380), (320, 900)]
    draw.polygon(cliff_points, fill=DARK_GRAY, outline=BLACK, width=3)
    # 悬崖纹理
    draw.line([180, 450, 180, 850], fill=GRAY, width=2)
    draw.line([220, 430, 220, 800], fill=GRAY, width=2)
    
    # 悬崖右峰
    cliff2_points = [(480, 900), (520, 350), (650, 380), (700, 900)]
    draw.polygon(cliff2_points, fill=LIGHT_GRAY, outline=BLACK, width=3)
    # 纹理
    draw.line([560, 400, 560, 850], fill=GRAY, width=2)
    draw.line([600, 420, 600, 800], fill=GRAY, width=2)
    
    # 悬崖脸 - 左
    draw_eyes(draw, 215, 500, 0.8, "happy")
    draw_smile(draw, 215, 540, 0.8)
    
    # 悬崖脸 - 右
    draw_eyes(draw, 590, 480, 0.8, "wink")
    draw_smile(draw, 590, 520, 0.8)
    
    # 草地顶部
    draw.ellipse([120, 360, 300, 400], fill=GREEN, outline=BLACK, width=2)
    draw.ellipse([500, 320, 680, 380], fill=GREEN, outline=BLACK, width=2)
    
    # 奥布莱恩塔
    tx, ty = 600, 280
    draw.rectangle([tx-25, ty-80, tx+25, ty+40], fill=DARK_GRAY, outline=BLACK, width=2)
    draw.polygon([tx-30, ty-80, tx, ty-120, tx+30, ty-80], fill=DARK_GRAY, outline=BLACK, width=2)
    draw.rectangle([tx-5, ty-100, tx+5, ty-60], fill=BLACK)  # 窗户
    
    return img

def draw_dubrovnik():
    """3. 克罗地亚 - 杜布罗夫尼克"""
    img = create_gradient_background()
    draw = ImageDraw.Draw(img)
    
    # 云朵
    draw_cloud(draw, 150, 100, 0.7)
    draw_cloud(draw, 650, 150, 0.8)
    
    # 海水
    draw.rectangle([0, 750, WIDTH, HEIGHT], fill=(70, 130, 180), outline=BLACK, width=2)
    
    # 城墙基础
    draw.rectangle([50, 600, 750, 800], fill=CREAM, outline=BLACK, width=3)
    
    # 城墙垛口
    for x in range(60, 750, 40):
        draw.rectangle([x, 560, x+25, 600], fill=CREAM, outline=BLACK, width=2)
    
    # 主塔楼
    towers = [150, 400, 650]
    for tx in towers:
        # 塔身
        draw.rectangle([tx-50, 350, tx+50, 560], fill=ORANGE, outline=BLACK, width=3)
        # 塔顶
        draw.polygon([tx-60, 350, tx, 250, tx+60, 350], fill=RED, outline=BLACK, width=3)
        # 窗户
        draw.rectangle([tx-15, 400, tx+15, 450], fill=BLACK, outline=BLACK, width=2)
        # 窗户眼睛效果
        draw.ellipse([tx-10, 405, tx-2, 420], fill=YELLOW)
        draw.ellipse([tx+2, 405, tx+10, 420], fill=YELLOW)
        draw.ellipse([tx-8, 408, tx-4, 415], fill=BLACK)
        draw.ellipse([tx+4, 408, tx+8, 415], fill=BLACK)
    
    # 中央塔楼脸
    draw_eyes(draw, 400, 480, 1.0, "happy")
    draw_smile(draw, 400, 520, 1.0)
    
    # 红色屋顶建筑群
    for i, rx in enumerate([120, 220, 320, 480, 580, 680]):
        ry = 680 + (i % 3) * 20
        draw.polygon([rx-30, ry, rx, ry-40, rx+30, ry], fill=RED, outline=BLACK, width=2)
        draw.rectangle([rx-25, ry, rx+25, ry+50], fill=ORANGE, outline=BLACK, width=1)
    
    return img

def draw_bratislava_castle():
    """4. 斯洛伐克 - 布拉迪斯拉发城堡"""
    img = create_gradient_background()
    draw = ImageDraw.Draw(img)
    
    # 云朵
    draw_cloud(draw, 200, 100, 0.8)
    draw_cloud(draw, 600, 180, 0.9)
    
    # 山坡
    draw.polygon([0, 900, 400, 600, 800, 900, 800, 1200, 0, 1200], fill=GREEN, outline=BLACK, width=2)
    
    # 城堡主体建筑
    cx, cy = 400, 550
    # 主殿
    draw.rectangle([cx-150, cy, cx+150, cy+200], fill=WHITE, outline=BLACK, width=3)
    
    # 四角塔楼
    tower_offset = 130
    for dx in [-tower_offset, tower_offset]:
        for dy in [0, 200]:
            tx, ty = cx + dx, cy + dy
            # 塔身
            draw.rectangle([tx-40, ty-80, tx+40, ty], fill=WHITE, outline=BLACK, width=3)
            # 红色塔顶
            draw.polygon([tx-50, ty-80, tx, ty-160, tx+50, ty-80], fill=RED, outline=BLACK, width=3)
            # 塔顶旗帜
            draw.line([tx, ty-160, tx, ty-200], fill=DARK_BROWN, width=3)
            draw.polygon([tx, ty-200, tx+30, ty-190, tx, ty-180], fill=RED, outline=BLACK, width=1)
    
    # 中央拱门 - 变成笑脸
    draw.arc([cx-80, cy+50, cx+80, cy+150], start=0, end=180, fill=BLACK, width=5)
    # 眼睛
    draw_eyes(draw, cx, cy-30, 1.2, "happy")
    
    # 屋顶装饰
    draw.rectangle([cx-150, cy-20, cx+150, cy], fill=RED, outline=BLACK, width=2)
    
    # 窗户
    for wx in [cx-100, cx, cx+100]:
        draw.rectangle([wx-15, cy+30, wx+15, cy+70], fill=BLACK, outline=BLACK, width=2)
    
    return img

def draw_bran_castle():
    """5. 罗马尼亚 - 布兰城堡 (德古拉城堡)"""
    img = create_gradient_background()
    draw = ImageDraw.Draw(img)
    
    # 深色渐变背景
    for y in range(HEIGHT):
        ratio = y / HEIGHT
        r = int(100 * (1 - ratio) + 80 * ratio)
        g = int(150 * (1 - ratio) + 100 * ratio)
        b = int(200 * (1 - ratio) + 150 * ratio)
        draw.line([(0, y), (WIDTH, y)], fill=(r, g, b))
    
    # 云朵
    draw_cloud(draw, 150, 120, 0.7)
    draw_cloud(draw, 650, 100, 0.6)
    
    # 悬崖基座
    draw.polygon([0, 1000, 200, 600, 600, 550, 800, 900, 800, 1200, 0, 1200], 
                 fill=DARK_GRAY, outline=BLACK, width=3)
    
    # 城堡主楼
    cx, cy = 400, 500
    # 主塔
    draw.rectangle([cx-60, cy-100, cx+60, cy+150], fill=CREAM, outline=BLACK, width=3)
    draw.polygon([cx-70, cy-100, cx, cy-200, cx+70, cy-100], fill=DARK_BROWN, outline=BLACK, width=3)
    
    # 侧塔
    draw.rectangle([cx-140, cy-50, cx-80, cy+100], fill=CREAM, outline=BLACK, width=3)
    draw.polygon([cx-150, cy-50, cx-110, cy-130, cx-70, cy-50], fill=DARK_BROWN, outline=BLACK, width=3)
    
    draw.rectangle([cx+80, cy-50, cx+140, cy+100], fill=CREAM, outline=BLACK, width=3)
    draw.polygon([cx+70, cy-50, cx+110, cy-130, cx+150, cy-50], fill=DARK_BROWN, outline=BLACK, width=3)
    
    # 德古拉脸 - 中央塔
    draw_eyes(draw, cx, cy+20, 1.0, "happy")
    # 尖牙微笑
    draw.arc([cx-30, cy+30, cx+30, cy+80], start=0, end=180, fill=BLACK, width=3)
    draw.polygon([cx-15, cy+60, cx-10, cy+75, cx-5, cy+60], fill=WHITE, outline=BLACK, width=1)
    draw.polygon([cx+5, cy+60, cx+10, cy+75, cx+15, cy+60], fill=WHITE, outline=BLACK, width=1)
    
    # 蝙蝠
    for bx, by in [(200, 200), (600, 250), (150, 350)]:
        draw.polygon([bx, by, bx-20, by-15, bx-10, by, bx-30, by+10, bx, by+5, 
                     bx+30, by+10, bx+10, by, bx+20, by-15], fill=BLACK)
    
    # 连接走廊
    draw.rectangle([cx-80, cy+50, cx+80, cy+80], fill=DARK_BROWN, outline=BLACK, width=2)
    
    return img

def draw_rila_monastery():
    """6. 保加利亚 - 里拉修道院"""
    img = create_gradient_background()
    draw = ImageDraw.Draw(img)
    
    # 云朵
    draw_cloud(draw, 180, 100, 0.8)
    draw_cloud(draw, 620, 150, 0.9)
    
    # 山背景
    draw.polygon([0, 800, 250, 300, 500, 500, 750, 250, 800, 800], 
                 fill=(100, 150, 100), outline=BLACK, width=2)
    draw.polygon([0, 900, 200, 600, 400, 700, 600, 550, 800, 800, 800, 1200, 0, 1200], 
                 fill=GREEN, outline=BLACK, width=2)
    
    # 主教堂
    cx, cy = 400, 550
    
    # 中央主塔
    draw.rectangle([cx-60, cy-50, cx+60, cy+150], fill=CREAM, outline=BLACK, width=3)
    draw.polygon([cx-70, cy-50, cx, cy-150, cx+70, cy-50], fill=DARK_BROWN, outline=BLACK, width=3)
    # 金色洋葱顶
    draw.ellipse([cx-50, cy-200, cx+50, cy-120], fill=GOLD, outline=BLACK, width=3)
    draw.line([cx, cy-200, cx, cy-240], fill=GOLD, width=3)
    
    # 侧塔
    for dx in [-120, 120]:
        draw.rectangle([cx+dx-35, cy, cx+dx+35, cy+100], fill=CREAM, outline=BLACK, width=3)
        draw.polygon([cx+dx-40, cy, cx+dx, cy-80, cx+dx+40, cy], fill=DARK_BROWN, outline=BLACK, width=3)
        draw.ellipse([cx+dx-30, cy-120, cx+dx+30, cy-70], fill=GOLD, outline=BLACK, width=3)
    
    # 主塔脸
    draw_eyes(draw, cx, cy+50, 1.0, "happy")
    draw_smile(draw, cx, cy+90, 1.0)
    
    # 拱形门廊
    draw.arc([cx-40, cy+80, cx+40, cy+160], start=0, end=180, fill=BLACK, width=4)
    
    # 黑白条纹装饰
    stripe_y = cy + 20
    for i, sx in enumerate(range(cx-55, cx+56, 15)):
        color = BLACK if i % 2 == 0 else WHITE
        draw.rectangle([sx, stripe_y, sx+15, stripe_y+20], fill=color, outline=BLACK, width=1)
    
    return img

def draw_sava_temple():
    """7. 塞尔维亚 - 圣萨瓦教堂"""
    img = create_gradient_background()
    draw = ImageDraw.Draw(img)
    
    # 云朵
    draw_cloud(draw, 200, 120, 0.7)
    draw_cloud(draw, 600, 100, 0.8)
    
    # 中央巨大洋葱顶
    cx, cy = 400, 450
    
    # 基座
    draw.rectangle([cx-100, cy+150, cx+100, cy+350], fill=WHITE, outline=BLACK, width=3)
    
    # 巨大洋葱顶
    draw.ellipse([cx-130, cy-80, cx+130, cy+180], fill=WHITE, outline=BLACK, width=4)
    # 金色十字架
    draw.line([cx, cy-150, cx, cy-220], fill=GOLD, width=6)
    draw.line([cx-25, cy-185, cx+25, cy-185], fill=GOLD, width=5)
    
    # 小洋葱顶 - 四角
    for angle in [45, 135, 225, 315]:
        rad = math.radians(angle)
        tx = cx + math.cos(rad) * 140
        ty = cy + math.sin(rad) * 80
        draw.ellipse([tx-35, ty-40, tx+35, ty+40], fill=WHITE, outline=BLACK, width=3)
        draw.line([tx, ty-40, tx, ty-70], fill=GOLD, width=3)
    
    # 正面脸 - 在基座上
    draw_eyes(draw, cx, cy+220, 1.2, "happy")
    draw_smile(draw, cx, cy+260, 1.2)
    
    # 入口拱门
    draw.arc([cx-50, cy+250, cx+50, cy+350], start=0, end=180, fill=BLACK, width=4)
    
    # 装饰图案
    for i in range(4):
        x = cx - 70 + i * 50
        draw.ellipse([x-10, cy+180, x+10, cy+200], fill=GOLD, outline=BLACK, width=1)
    
    # 两侧建筑
    draw.rectangle([cx-180, cy+200, cx-100, cy+350], fill=WHITE, outline=BLACK, width=3)
    draw.rectangle([cx+100, cy+200, cx+180, cy+350], fill=WHITE, outline=BLACK, width=3)
    
    return img

def draw_doha_museum():
    """8. 卡塔尔 - 伊斯兰艺术博物馆"""
    img = create_gradient_background()
    draw = ImageDraw.Draw(img)
    
    # 云朵
    draw_cloud(draw, 150, 100, 0.6)
    draw_cloud(draw, 650, 180, 0.7)
    
    # 沙漠/水岸
    draw.polygon([0, 850, 300, 750, 500, 780, 800, 700, 800, 1200, 0, 1200], 
                 fill=(240, 220, 180), outline=BLACK, width=2)
    
    # 海水
    draw.rectangle([0, 750, WIDTH, 850], fill=(100, 150, 200), outline=BLACK, width=2)
    
    # 主建筑 - 几何立方体堆叠
    cx, cy = 400, 500
    
    # 基座
    draw.rectangle([cx-200, cy+100, cx+200, cy+300], fill=CREAM, outline=BLACK, width=3)
    
    # 中间层
    draw.rectangle([cx-150, cy-50, cx+150, cy+100], fill=CREAM, outline=BLACK, width=3)
    
    # 上层
    draw.rectangle([cx-100, cy-150, cx+100, cy-50], fill=CREAM, outline=BLACK, width=3)
    
    # 顶部
    draw.rectangle([cx-60, cy-220, cx+60, cy-150], fill=CREAM, outline=BLACK, width=3)
    
    # 眼睛 - 在每层
    draw_eyes(draw, cx, cy+180, 0.8, "happy")
    draw_eyes(draw, cx, cy+20, 0.7, "wink")
    draw_eyes(draw, cx, cy-100, 0.6, "happy")
    
    # 伊斯兰风格拱门窗户
    for layer_y in [cy+50, cy-80]:
        for wx in [cx-80, cx, cx+80]:
            draw.arc([wx-25, layer_y-30, wx+25, layer_y+30], start=0, end=180, fill=BLACK, width=3)
            draw.line([wx-25, layer_y, wx+25, layer_y], fill=BLACK, width=2)
    
    # 装饰性几何图案
    for i, px in enumerate([cx-150, cx-50, cx+50, cx+150]):
        draw.polygon([px, cy+120, px-15, cy+140, px, cy+160, px+15, cy+140], 
                    fill=(200, 170, 130), outline=BLACK, width=2)
    
    # 倒影
    for i in range(5):
        alpha = 100 - i * 15
        y = 760 + i * 20
        draw.rectangle([cx-180+i*10, y, cx+180-i*10, y+15], fill=(150, 180, 210), outline=None)
    
    return img

def main():
    """主函数 - 生成所有8个图片"""
    towers = [
        ("rovaniemi.png", draw_santa_village, "芬兰 - 圣诞老人村"),
        ("cliffs-of-moher.png", draw_cliffs_of_moher, "爱尔兰 - 莫赫悬崖"),
        ("dubrovnik.png", draw_dubrovnik, "克罗地亚 - 杜布罗夫尼克"),
        ("bratislava.png", draw_bratislava_castle, "斯洛伐克 - 布拉迪斯拉发城堡"),
        ("bran-castle.png", draw_bran_castle, "罗马尼亚 - 布兰城堡"),
        ("rila.png", draw_rila_monastery, "保加利亚 - 里拉修道院"),
        ("sava-temple.png", draw_sava_temple, "塞尔维亚 - 圣萨瓦教堂"),
        ("doha-museum.png", draw_doha_museum, "卡塔尔 - 伊斯兰艺术博物馆"),
    ]
    
    # 确保输出目录存在
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # 生成每个塔的图片
    for filename, draw_func, name in towers:
        filepath = os.path.join(OUTPUT_DIR, filename)
        try:
            img = draw_func()
            img.save(filepath, "PNG")
            print(f"✓ 已生成: {filename} - {name}")
        except Exception as e:
            print(f"✗ 失败: {filename} - {name}: {e}")
    
    print(f"\n所有图片已保存到: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
