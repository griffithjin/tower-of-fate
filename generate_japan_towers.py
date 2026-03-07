#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成日本各县卡通塔图片 - 愤怒的小鸟风格
"""

from PIL import Image, ImageDraw, ImageFont
import math
import os

# 输出目录
OUTPUT_DIR = "/Users/moutai/Desktop/toweroffate_v1.0/assets/towers/states/japan/"

# 图片尺寸
WIDTH, HEIGHT = 800, 1200

def create_sky_gradient(width, height):
    """创建天蓝色渐变背景"""
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    
    # 从天蓝色渐变到浅蓝色
    top_color = (135, 206, 235)  # 天蓝色
    bottom_color = (224, 246, 255)  # 浅蓝色
    
    for y in range(height):
        ratio = y / height
        r = int(top_color[0] + (bottom_color[0] - top_color[0]) * ratio)
        g = int(top_color[1] + (bottom_color[1] - top_color[1]) * ratio)
        b = int(top_color[2] + (bottom_color[2] - top_color[2]) * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    return img

def draw_circle(draw, x, y, radius, color, outline_color=None, outline_width=2):
    """绘制圆形"""
    draw.ellipse([x-radius, y-radius, x+radius, y+radius], fill=color, outline=outline_color, width=outline_width)

def draw_oval(draw, x, y, width, height, color, outline_color=None, outline_width=2):
    """绘制椭圆形"""
    draw.ellipse([x-width//2, y-height//2, x+width//2, y+height//2], fill=color, outline=outline_color, width=outline_width)

def draw_rounded_rect(draw, x, y, width, height, radius, color, outline_color=None, outline_width=2):
    """绘制圆角矩形"""
    draw.rounded_rectangle([x, y, x+width, y+height], radius=radius, fill=color, outline=outline_color, width=outline_width)

def draw_cute_eyes(draw, x, y, eye_size=20):
    """绘制愤怒的小鸟风格的可爱大眼睛"""
    # 眼白
    draw_circle(draw, x-15, y, eye_size, (255, 255, 255), (0, 0, 0), 2)
    draw_circle(draw, x+15, y, eye_size, (255, 255, 255), (0, 0, 0), 2)
    # 瞳孔
    draw_circle(draw, x-12, y+2, eye_size//2.5, (0, 0, 0))
    draw_circle(draw, x+12, y+2, eye_size//2.5, (0, 0, 0))
    # 高光
    draw_circle(draw, x-15, y-3, 6, (255, 255, 255))
    draw_circle(draw, x+12, y-3, 6, (255, 255, 255))

def draw_cute_mouth(draw, x, y, mouth_type='happy'):
    """绘制可爱的嘴巴"""
    if mouth_type == 'happy':
        # 开心的微笑
        draw.arc([x-15, y-5, x+15, y+15], start=0, end=180, fill=(0, 0, 0), width=3)
        # 舌头
        draw.pieslice([x-8, y+2, x+8, y+12], start=0, end=180, fill=(255, 100, 100))
    elif mouth_type == 'o':
        # O型嘴
        draw.ellipse([x-8, y-3, x+8, y+13], fill=(255, 100, 100), outline=(0, 0, 0), width=2)
    elif mouth_type == 'small_smile':
        draw.arc([x-10, y-3, x+10, y+10], start=0, end=180, fill=(0, 0, 0), width=2)

def draw_blush(draw, x, y):
    """绘制腮红"""
    draw.ellipse([x-12, y-8, x+12, y+8], fill=(255, 180, 180, 128))

def add_clouds(draw, count=5):
    """添加卡通云朵"""
    import random
    random.seed(42)
    for _ in range(count):
        cx = random.randint(50, 750)
        cy = random.randint(50, 300)
        size = random.randint(30, 60)
        # 画云朵 - 多个圆组成
        draw.ellipse([cx-size, cy-size//2, cx+size, cy+size//2], fill=(255, 255, 255, 200))
        draw.ellipse([cx-size*1.5, cy, cx-size*0.5, cy+size], fill=(255, 255, 255, 200))
        draw.ellipse([cx+size*0.5, cy, cx+size*1.5, cy+size], fill=(255, 255, 255, 200))

def add_ground(draw, y_position, width, height):
    """添加地面"""
    # 草地
    draw.rectangle([0, y_position, width, height], fill=(100, 200, 100))
    # 草地波浪
    for i in range(0, width, 30):
        draw.pieslice([i, y_position-10, i+30, y_position+20], start=0, end=180, fill=(120, 220, 120))

# ============ 各个县的塔绘制函数 ============

def draw_tokyo_skytree():
    """东京 - 晴空塔"""
    img = create_sky_gradient(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    add_clouds(draw, 6)
    add_ground(draw, 1050, WIDTH, HEIGHT)
    
    center_x, base_y = 400, 1050
    
    # 塔身 - 紫色渐变风格
    colors = [(147, 112, 219), (138, 43, 226), (75, 0, 130)]
    
    # 底座
    draw.polygon([(center_x-80, base_y), (center_x+80, base_y), 
                  (center_x+60, base_y-100), (center_x-60, base_y-100)], 
                 fill=(100, 50, 150), outline=(0, 0, 0), width=2)
    
    # 塔身 - 分段
    for i, (y1, y2, w1, w2, color) in enumerate([
        (base_y-100, base_y-250, 120, 80, colors[0]),
        (base_y-250, base_y-400, 80, 50, colors[1]),
        (base_y-400, base_y-550, 50, 30, colors[2]),
    ]):
        draw.polygon([(center_x-w1//2, y1), (center_x+w1//2, y1),
                      (center_x+w2//2, y2), (center_x-w2//2, y2)],
                     fill=color, outline=(0, 0, 0), width=2)
        # 添加装饰线
        draw.line([(center_x-w1//2, y1), (center_x+w1//2, y1)], fill=(200, 150, 255), width=3)
    
    # 塔尖
    draw.polygon([(center_x-15, base_y-550), (center_x+15, base_y-550),
                  (center_x, base_y-750)], fill=(200, 100, 255), outline=(0, 0, 0), width=2)
    
    # 瞭望台 (眼睛)
    draw_rounded_rect(draw, center_x-40, base_y-380, 80, 60, 20, (255, 255, 255), (0, 0, 0), 2)
    draw_cute_eyes(draw, center_x, base_y-350, 18)
    draw_cute_mouth(draw, center_x, base_y-320, 'happy')
    
    # 腮红
    draw.ellipse([center_x-55, base_y-360, center_x-35, base_y-340], fill=(255, 150, 150))
    draw.ellipse([center_x+35, base_y-360, center_x+55, base_y-340], fill=(255, 150, 150))
    
    return img

def draw_osaka_castle():
    """大阪 - 大阪城"""
    img = create_sky_gradient(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    add_clouds(draw, 5)
    add_ground(draw, 1050, WIDTH, HEIGHT)
    
    center_x, base_y = 400, 1050
    
    # 石基座
    draw.polygon([(center_x-120, base_y), (center_x+120, base_y),
                  (center_x+100, base_y-80), (center_x-100, base_y-80)],
                 fill=(150, 150, 160), outline=(0, 0, 0), width=2)
    
    # 城堡主体 - 白色墙体
    draw.polygon([(center_x-100, base_y-80), (center_x+100, base_y-80),
                  (center_x+90, base_y-200), (center_x-90, base_y-200)],
                 fill=(250, 250, 240), outline=(0, 0, 0), width=2)
    
    # 黑色装饰线
    for y in [base_y-120, base_y-160]:
        draw.polygon([(center_x-95, y), (center_x+95, y),
                      (center_x+93, y-15), (center_x-93, y-15)],
                     fill=(50, 50, 50), outline=(0, 0, 0), width=1)
    
    # 绿色屋顶层
    roof_colors = [(34, 139, 34), (50, 160, 50), (70, 180, 70)]
    roof_positions = [
        (base_y-200, base_y-280, 200, 140),
        (base_y-280, base_y-350, 140, 100),
        (base_y-350, base_y-420, 100, 60),
    ]
    
    for i, (y1, y2, w1, w2) in enumerate(roof_positions):
        # 屋顶
        draw.polygon([(center_x-w1//2, y1), (center_x+w1//2, y1),
                      (center_x+w2//2, y2), (center_x-w2//2, y2)],
                     fill=roof_colors[i], outline=(0, 0, 0), width=2)
        # 金色装饰
        draw.polygon([(center_x-5, y2-10), (center_x+5, y2-10),
                      (center_x, y2-35)], fill=(255, 215, 0), outline=(0, 0, 0), width=1)
    
    # 塔尖
    draw.polygon([(center_x-30, base_y-420), (center_x+30, base_y-420),
                  (center_x, base_y-550)], fill=(255, 215, 0), outline=(0, 0, 0), width=2)
    
    # 脸部
    draw_cute_eyes(draw, center_x, base_y-250, 22)
    draw_cute_mouth(draw, center_x, base_y-210, 'happy')
    draw.ellipse([center_x-70, base_y-260, center_x-45, base_y-235], fill=(255, 150, 150))
    draw.ellipse([center_x+45, base_y-260, center_x+70, base_y-235], fill=(255, 150, 150))
    
    return img

def draw_aichi_nagoya():
    """爱知 - 名古屋城"""
    img = create_sky_gradient(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    add_clouds(draw, 5)
    add_ground(draw, 1050, WIDTH, HEIGHT)
    
    center_x, base_y = 400, 1050
    
    # 石基座
    draw.polygon([(center_x-100, base_y), (center_x+100, base_y),
                  (center_x+85, base_y-70), (center_x-85, base_y-70)],
                 fill=(160, 160, 170), outline=(0, 0, 0), width=2)
    
    # 白色墙体
    draw.polygon([(center_x-85, base_y-70), (center_x+85, base_y-70),
                  (center_x+75, base_y-180), (center_x-75, base_y-180)],
                 fill=(255, 255, 250), outline=(0, 0, 0), width=2)
    
    # 绿色金𩾇屋顶
    roof_positions = [
        (base_y-180, base_y-260, 170, 120),
        (base_y-260, base_y-330, 120, 80),
        (base_y-330, base_y-400, 80, 50),
    ]
    
    for y1, y2, w1, w2 in roof_positions:
        # 绿色屋顶
        draw.polygon([(center_x-w1//2, y1), (center_x+w1//2, y1),
                      (center_x+w2//2, y2), (center_x-w2//2, y2)],
                     fill=(0, 128, 0), outline=(0, 0, 0), width=2)
        # 金色金𩾇装饰
        draw.polygon([(center_x, y2-5), (center_x-8, y2+10), (center_x+8, y2+10)],
                     fill=(255, 215, 0), outline=(0, 0, 0), width=1)
    
    # 塔尖
    draw.polygon([(center_x-25, base_y-400), (center_x+25, base_y-400),
                  (center_x, base_y-520)], fill=(255, 215, 0), outline=(0, 0, 0), width=2)
    
    # 脸部
    draw_cute_eyes(draw, center_x, base_y-230, 20)
    draw_cute_mouth(draw, center_x, base_y-195, 'happy')
    draw.ellipse([center_x-60, base_y-240, center_x-40, base_y-220], fill=(255, 150, 150))
    draw.ellipse([center_x+40, base_y-240, center_x+60, base_y-220], fill=(255, 150, 150))
    
    return img

def draw_kanagawa_fuji():
    """神奈川 - 富士山+横滨"""
    img = create_sky_gradient(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    add_clouds(draw, 7)
    add_ground(draw, 1050, WIDTH, HEIGHT)
    
    center_x, base_y = 400, 1050
    
    # 富士山主体
    mountain_base = 950
    # 山体 - 蓝色渐变
    draw.polygon([(center_x-200, mountain_base), (center_x+200, mountain_base),
                  (center_x, mountain_base-450)], fill=(70, 130, 180), outline=(0, 0, 0), width=2)
    
    # 山顶积雪
    draw.polygon([(center_x-60, mountain_base-330), (center_x+60, mountain_base-330),
                  (center_x, mountain_base-450)], fill=(255, 255, 255), outline=(0, 0, 0), width=2)
    
    # 雪地纹理
    for i in range(3):
        y = mountain_base - 360 - i*20
        w = 50 - i*10
        draw.polygon([(center_x-w, y), (center_x+w, y),
                      (center_x+w-10, y-15), (center_x-w+10, y-15)], fill=(255, 255, 255))
    
    # 横滨港 - 右侧港口建筑
    port_x = center_x + 180
    # 红色仓库风格建筑
    draw.polygon([(port_x-50, base_y), (port_x+50, base_y),
                  (port_x+40, base_y-80), (port_x-40, base_y-80)],
                 fill=(180, 80, 80), outline=(0, 0, 0), width=2)
    # 屋顶
    draw.polygon([(port_x-45, base_y-80), (port_x+45, base_y-80),
                  (port_x, base_y-120)], fill=(100, 50, 50), outline=(0, 0, 0), width=2)
    
    # 脸部 - 在山体上
    draw_cute_eyes(draw, center_x, mountain_base-250, 25)
    draw_cute_mouth(draw, center_x, mountain_base-200, 'happy')
    draw.ellipse([center_x-80, mountain_base-260, center_x-50, mountain_base-230], fill=(255, 150, 150))
    draw.ellipse([center_x+50, mountain_base-260, center_x+80, mountain_base-230], fill=(255, 150, 150))
    
    # 樱花装饰
    for i in range(5):
        sx = 100 + i*150
        sy = 900
        draw.ellipse([sx-15, sy-15, sx+15, sy+15], fill=(255, 183, 197))
        draw.ellipse([sx-10, sy-25, sx+10, sy-5], fill=(255, 183, 197))
        draw.ellipse([sx-25, sy-10, sx-5, sy+10], fill=(255, 183, 197))
        draw.ellipse([sx+5, sy-10, sx+25, sy+10], fill=(255, 183, 197))
        draw.ellipse([sx-10, sy+5, sx+10, sy+25], fill=(255, 183, 197))
    
    return img

def draw_hokkaido_snow():
    """北海道 - 雪景+薰衣草"""
    img = create_sky_gradient(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    add_clouds(draw, 6)
    
    # 雪地背景
    draw.rectangle([0, 700, WIDTH, HEIGHT], fill=(240, 248, 255))
    # 雪地波浪
    for i in range(0, WIDTH, 50):
        draw.pieslice([i, 680, i+60, 740], start=0, end=180, fill=(250, 250, 255))
    
    center_x, base_y = 400, 1050
    
    # 薰衣草花田 - 紫色渐变背景
    for y in range(750, 850, 10):
        for x in range(0, WIDTH, 20):
            purple = (150 + (x % 40), 100, 180 + (y % 30))
            draw.ellipse([x, y, x+8, y+15], fill=purple)
    
    # 薰衣草塔 - 由薰衣草组成的塔形
    tower_colors = [(180, 130, 210), (160, 110, 190), (140, 90, 170)]
    
    # 塔底 - 薰衣草丛
    for layer, (y1, y2, w1, w2, color) in enumerate([
        (base_y-50, base_y-150, 200, 160, tower_colors[0]),
        (base_y-150, base_y-280, 160, 120, tower_colors[1]),
        (base_y-280, base_y-400, 120, 80, tower_colors[2]),
    ]):
        draw.polygon([(center_x-w1//2, y1), (center_x+w1//2, y1),
                      (center_x+w2//2, y2), (center_x-w2//2, y2)],
                     fill=color, outline=(0, 0, 0), width=2)
        # 薰衣草花朵点缀
        for i in range(w1//20):
            fx = center_x - w1//2 + i*20 + 10
            fy = y1 - 10
            draw.ellipse([fx-5, fy-8, fx+5, fy+8], fill=(200, 150, 230))
            draw.ellipse([fx-3, fy-12, fx+3, fy-4], fill=(220, 170, 250))
    
    # 塔尖
    draw.polygon([(center_x-40, base_y-400), (center_x+40, base_y-400),
                  (center_x, base_y-550)], fill=(120, 70, 150), outline=(0, 0, 0), width=2)
    
    # 脸部
    draw_cute_eyes(draw, center_x, base_y-250, 22)
    draw_cute_mouth(draw, center_x, base_y-210, 'happy')
    draw.ellipse([center_x-70, base_y-260, center_x-45, base_y-235], fill=(255, 150, 150))
    draw.ellipse([center_x+45, base_y-260, center_x+70, base_y-235], fill=(255, 150, 150))
    
    # 雪花装饰
    for i in range(20):
        import random
        random.seed(i)
        sx = random.randint(50, 750)
        sy = random.randint(50, 600)
        size = random.randint(3, 8)
        draw.polygon([(sx, sy-size), (sx+size*0.3, sy-size*0.3),
                      (sx+size, sy), (sx+size*0.3, sy+size*0.3),
                      (sx, sy+size), (sx-size*0.3, sy+size*0.3),
                      (sx-size, sy), (sx-size*0.3, sy-size*0.3)],
                     fill=(255, 255, 255))
    
    return img

def draw_fukuoka_dazaifu():
    """福冈 - 太宰府天满宫"""
    img = create_sky_gradient(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    add_clouds(draw, 5)
    add_ground(draw, 1050, WIDTH, HEIGHT)
    
    center_x, base_y = 400, 1050
    
    # 石基座
    draw.polygon([(center_x-90, base_y), (center_x+90, base_y),
                  (center_x+75, base_y-60), (center_x-75, base_y-60)],
                 fill=(160, 160, 170), outline=(0, 0, 0), width=2)
    
    # 红色墙体
    draw.polygon([(center_x-75, base_y-60), (center_x+75, base_y-60),
                  (center_x+65, base_y-160), (center_x-65, base_y-160)],
                 fill=(180, 60, 60), outline=(0, 0, 0), width=2)
    
    # 白色装饰条
    draw.polygon([(center_x-70, base_y-100), (center_x+70, base_y-100),
                  (center_x+68, base_y-115), (center_x-68, base_y-115)],
                 fill=(255, 255, 255), outline=(0, 0, 0), width=1)
    
    # 绿色屋顶
    roof_positions = [
        (base_y-160, base_y-230, 150, 110),
        (base_y-230, base_y-300, 110, 70),
    ]
    
    for y1, y2, w1, w2 in roof_positions:
        draw.polygon([(center_x-w1//2, y1), (center_x+w1//2, y1),
                      (center_x+w2//2, y2), (center_x-w2//2, y2)],
                     fill=(0, 120, 0), outline=(0, 0, 0), width=2)
    
    # 金色装饰
    draw.polygon([(center_x-5, base_y-300), (center_x+5, base_y-300),
                  (center_x, base_y-400)], fill=(255, 215, 0), outline=(0, 0, 0), width=2)
    
    # 脸部
    draw_cute_eyes(draw, center_x, base_y-200, 20)
    draw_cute_mouth(draw, center_x, base_y-165, 'happy')
    draw.ellipse([center_x-55, base_y-210, center_x-35, base_y-190], fill=(255, 150, 150))
    draw.ellipse([center_x+35, base_y-210, center_x+55, base_y-190], fill=(255, 150, 150))
    
    # 梅花装饰
    for i in range(8):
        import random
        random.seed(i * 100)
        mx = random.randint(50, 750)
        my = random.randint(600, 900)
        # 梅花
        for angle in range(0, 360, 72):
            rad = math.radians(angle)
            px = mx + 12 * math.cos(rad)
            py = my + 12 * math.sin(rad)
            draw.ellipse([px-6, py-6, px+6, py+6], fill=(255, 200, 220))
        draw.ellipse([mx-4, my-4, mx+4, my+4], fill=(255, 255, 0))
    
    return img

def draw_hyogo_himeji():
    """兵库 - 姬路城 (白鹭城)"""
    img = create_sky_gradient(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    add_clouds(draw, 5)
    add_ground(draw, 1050, WIDTH, HEIGHT)
    
    center_x, base_y = 400, 1050
    
    # 石基座
    draw.polygon([(center_x-110, base_y), (center_x+110, base_y),
                  (center_x+95, base_y-70), (center_x-95, base_y-70)],
                 fill=(170, 170, 180), outline=(0, 0, 0), width=2)
    
    # 纯白色墙体 - 白鹭城特色
    draw.polygon([(center_x-95, base_y-70), (center_x+95, base_y-70),
                  (center_x+85, base_y-180), (center_x-85, base_y-180)],
                 fill=(255, 255, 255), outline=(0, 0, 0), width=2)
    
    # 灰色屋顶瓦片
    roof_positions = [
        (base_y-180, base_y-250, 190, 150),
        (base_y-250, base_y-320, 150, 110),
        (base_y-320, base_y-390, 110, 70),
    ]
    
    for y1, y2, w1, w2 in roof_positions:
        draw.polygon([(center_x-w1//2, y1), (center_x+w1//2, y1),
                      (center_x+w2//2, y2), (center_x-w2//2, y2)],
                     fill=(100, 100, 110), outline=(0, 0, 0), width=2)
        # 屋顶装饰
        draw.polygon([(center_x-3, y2-3), (center_x+3, y2-3),
                      (center_x, y2-15)], fill=(255, 255, 255), outline=(0, 0, 0), width=1)
    
    # 尖顶
    draw.polygon([(center_x-20, base_y-390), (center_x+20, base_y-390),
                  (center_x, base_y-500)], fill=(100, 100, 110), outline=(0, 0, 0), width=2)
    
    # 脸部
    draw_cute_eyes(draw, center_x, base_y-240, 22)
    draw_cute_mouth(draw, center_x, base_y-200, 'happy')
    draw.ellipse([center_x-65, base_y-250, center_x-40, base_y-225], fill=(255, 150, 150))
    draw.ellipse([center_x+40, base_y-250, center_x+65, base_y-225], fill=(255, 150, 150))
    
    # 樱花
    for i in range(10):
        import random
        random.seed(i * 50)
        sx = random.randint(30, 770)
        sy = random.randint(500, 900)
        # 樱花花瓣
        for angle in range(0, 360, 60):
            rad = math.radians(angle)
            px = sx + 10 * math.cos(rad)
            py = sy + 10 * math.sin(rad)
            draw.ellipse([px-5, py-5, px+5, py+5], fill=(255, 192, 203))
    
    return img

def draw_kyoto_kinkaku():
    """京都 - 金阁寺"""
    img = create_sky_gradient(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    add_clouds(draw, 5)
    add_ground(draw, 1050, WIDTH, HEIGHT)
    
    center_x, base_y = 400, 1050
    
    # 池塘
    draw.ellipse([center_x-250, base_y-100, center_x+250, base_y+50], fill=(135, 206, 235))
    
    # 基座
    draw.polygon([(center_x-80, base_y), (center_x+80, base_y),
                  (center_x+70, base_y-50), (center_x-70, base_y-50)],
                 fill=(150, 150, 160), outline=(0, 0, 0), width=2)
    
    # 金阁三层 - 金色!
    gold_colors = [(255, 215, 100), (255, 200, 80), (255, 180, 60)]
    
    positions = [
        (base_y-50, base_y-150, 160, 130),
        (base_y-150, base_y-260, 130, 100),
        (base_y-260, base_y-380, 100, 60),
    ]
    
    for i, (y1, y2, w1, w2) in enumerate(positions):
        # 金色墙体
        draw.polygon([(center_x-w1//2, y1), (center_x+w1//2, y1),
                      (center_x+w2//2, y2), (center_x-w2//2, y2)],
                     fill=gold_colors[i], outline=(0, 0, 0), width=2)
        
        # 金色屋顶
        roof_y = y2 - 30
        draw.polygon([(center_x-w2//2-10, y2), (center_x+w2//2+10, y2),
                      (center_x+w2//2, roof_y), (center_x-w2//2, roof_y)],
                     fill=(255, 223, 0), outline=(0, 0, 0), width=2)
    
    # 最顶层尖顶
    draw.polygon([(center_x-5, base_y-380), (center_x+5, base_y-380),
                  (center_x, base_y-480)], fill=(255, 223, 0), outline=(0, 0, 0), width=2)
    
    # 凤凰装饰
    draw.ellipse([center_x-15, base_y-400, center_x+15, base_y-370], fill=(255, 100, 100))
    
    # 脸部 - 在二层
    draw_cute_eyes(draw, center_x, base_y-220, 20)
    draw_cute_mouth(draw, center_x, base_y-185, 'happy')
    draw.ellipse([center_x-55, base_y-230, center_x-35, base_y-210], fill=(255, 150, 150))
    draw.ellipse([center_x+35, base_y-230, center_x+55, base_y-210], fill=(255, 150, 150))
    
    # 松树装饰
    for i in range(3):
        tx = 100 + i * 300
        ty = base_y - 50
        # 树干
        draw.rectangle([tx-10, ty-100, tx+10, ty], fill=(139, 90, 43))
        # 树冠
        draw.ellipse([tx-40, ty-150, tx+40, ty-80], fill=(34, 139, 34))
        draw.ellipse([tx-30, ty-180, tx+30, ty-120], fill=(50, 160, 50))
    
    return img

def draw_okinawa_beach():
    """冲绳 - 海滩+狮子 (Shisa)"""
    img = create_sky_gradient(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    add_clouds(draw, 6)
    
    # 海滩渐变
    for y in range(700, 1050):
        ratio = (y - 700) / 350
        r = int(255 - 30 * ratio)
        g = int(230 - 20 * ratio)
        b = int(200 - 30 * ratio)
        draw.line([(0, y), (WIDTH, y)], fill=(r, g, b))
    
    # 海水
    for y in range(550, 700):
        ratio = (y - 550) / 150
        r = int(100 + 50 * ratio)
        g = int(150 + 50 * ratio)
        b = int(200 + 30 * ratio)
        draw.line([(0, y), (WIDTH, y)], fill=(r, g, b))
    
    add_ground(draw, 1050, WIDTH, HEIGHT)
    
    center_x, base_y = 400, 950
    
    # 石狮子塔 (Shisa塔)
    # 底部 - 石头基座
    draw.polygon([(center_x-100, base_y), (center_x+100, base_y),
                  (center_x+85, base_y-70), (center_x-85, base_y-70)],
                 fill=(160, 150, 140), outline=(0, 0, 0), width=2)
    
    # 塔身 - 珊瑚红色
    coral_colors = [(255, 127, 80), (255, 99, 71), (220, 80, 60)]
    
    positions = [
        (base_y-70, base_y-180, 170, 130),
        (base_y-180, base_y-280, 130, 90),
        (base_y-280, base_y-380, 90, 50),
    ]
    
    for i, (y1, y2, w1, w2) in enumerate(positions):
        draw.polygon([(center_x-w1//2, y1), (center_x+w1//2, y1),
                      (center_x+w2//2, y2), (center_x-w2//2, y2)],
                     fill=coral_colors[i], outline=(0, 0, 0), width=2)
        # 窗户装饰
        draw.rounded_rectangle([center_x-15, (y1+y2)//2-20, center_x+15, (y1+y2)//2+20],
                               radius=10, fill=(100, 60, 50), outline=(0, 0, 0), width=1)
    
    # 狮子头装饰
    head_y = base_y - 320
    # 狮子脸轮廓
    draw.ellipse([center_x-45, head_y-45, center_x+45, head_y+45], fill=(255, 200, 100), outline=(0, 0, 0), width=2)
    # 耳朵
    draw.polygon([(center_x-40, head_y-30), (center_x-55, head_y-60), (center_x-25, head_y-45)], fill=(255, 180, 80), outline=(0, 0, 0), width=2)
    draw.polygon([(center_x+40, head_y-30), (center_x+55, head_y-60), (center_x+25, head_y-45)], fill=(255, 180, 80), outline=(0, 0, 0), width=2)
    # 眼睛
    draw_cute_eyes(draw, center_x, head_y-10, 12)
    # 鼻子
    draw.ellipse([center_x-8, head_y+5, center_x+8, head_y+20], fill=(255, 100, 100), outline=(0, 0, 0), width=1)
    # 嘴巴
    draw.arc([center_x-15, head_y+15, center_x+15, head_y+35], start=0, end=180, fill=(0, 0, 0), width=2)
    
    # 塔尖
    draw.polygon([(center_x-30, base_y-380), (center_x+30, base_y-380),
                  (center_x, base_y-500)], fill=(255, 200, 100), outline=(0, 0, 0), width=2)
    
    # 脸部在塔身上
    draw_cute_eyes(draw, center_x, base_y-220, 20)
    draw_cute_mouth(draw, center_x, base_y-185, 'happy')
    draw.ellipse([center_x-55, base_y-230, center_x-35, base_y-210], fill=(255, 150, 150))
    draw.ellipse([center_x+35, base_y-230, center_x+55, base_y-210], fill=(255, 150, 150))
    
    # 棕榈树
    for px in [100, 700]:
        # 树干
        draw.polygon([(px-15, base_y), (px+15, base_y),
                      (px+10, base_y-200), (px-10, base_y-200)], fill=(139, 90, 43))
        # 叶子
        for angle in [30, 60, 90, 120, 150]:
            rad = math.radians(angle)
            leaf_x = px + 80 * math.cos(rad)
            leaf_y = base_y - 200 + 80 * math.sin(rad) * 0.3
            draw.polygon([(px, base_y-200), (leaf_x, leaf_y), (leaf_x+10, leaf_y-10)], fill=(34, 139, 34))
    
    return img

def draw_shizuoka_tea():
    """静冈 - 茶园+富士山"""
    img = create_sky_gradient(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    add_clouds(draw, 5)
    
    # 远处的富士山
    fuji_x, fuji_base = 600, 600
    draw.polygon([(fuji_x-150, fuji_base), (fuji_x+150, fuji_base),
                  (fuji_x, fuji_base-300)], fill=(100, 150, 180), outline=(0, 0, 0), width=1)
    draw.polygon([(fuji_x-50, fuji_base-200), (fuji_x+50, fuji_base-200),
                  (fuji_x, fuji_base-300)], fill=(255, 255, 255), outline=(0, 0, 0), width=1)
    
    # 茶园梯田 - 绿色渐变
    for i, y in enumerate(range(800, 1050, 30)):
        green_val = 100 + i * 8
        draw.polygon([(0, y), (WIDTH, y), (WIDTH, y+30), (0, y+30)], fill=(50, green_val, 50))
        # 茶叶灌木
        for x in range(0, WIDTH, 25):
            draw.ellipse([x, y-5, x+15, y+15], fill=(60, green_val+20, 60))
    
    center_x, base_y = 250, 900
    
    # 茶塔 - 绿色风格
    tea_colors = [(107, 142, 35), (85, 107, 47), (60, 80, 35)]
    
    # 基座
    draw.polygon([(center_x-80, base_y), (center_x+80, base_y),
                  (center_x+65, base_y-60), (center_x-65, base_y-60)],
                 fill=(139, 119, 101), outline=(0, 0, 0), width=2)
    
    positions = [
        (base_y-60, base_y-160, 130, 100),
        (base_y-160, base_y-260, 100, 70),
        (base_y-260, base_y-360, 70, 40),
    ]
    
    for i, (y1, y2, w1, w2) in enumerate(positions):
        draw.polygon([(center_x-w1//2, y1), (center_x+w1//2, y1),
                      (center_x+w2//2, y2), (center_x-w2//2, y2)],
                     fill=tea_colors[i], outline=(0, 0, 0), width=2)
        # 茶叶装饰
        for j in range(w1//15):
            lx = center_x - w1//2 + j*15 + 7
            ly = y1 - 5
            draw.ellipse([lx-4, ly-8, lx+4, ly+2], fill=(150, 200, 100))
    
    # 塔尖
    draw.polygon([(center_x-25, base_y-360), (center_x+25, base_y-360),
                  (center_x, base_y-480)], fill=(50, 70, 30), outline=(0, 0, 0), width=2)
    
    # 脸部
    draw_cute_eyes(draw, center_x, base_y-220, 18)
    draw_cute_mouth(draw, center_x, base_y-190, 'happy')
    draw.ellipse([center_x-50, base_y-230, center_x-30, base_y-210], fill=(255, 150, 150))
    draw.ellipse([center_x+30, base_y-230, center_x+50, base_y-210], fill=(255, 150, 150))
    
    # 茶壶装饰
    pot_x, pot_y = 550, 850
    # 壶身
    draw.ellipse([pot_x-40, pot_y-30, pot_x+40, pot_y+40], fill=(200, 80, 80), outline=(0, 0, 0), width=2)
    # 壶嘴
    draw.polygon([(pot_x+35, pot_y), (pot_x+60, pot_y-15), (pot_x+35, pot_y+10)], fill=(200, 80, 80), outline=(0, 0, 0), width=2)
    # 壶把
    draw.arc([pot_x-60, pot_y-20, pot_x-35, pot_y+25], start=90, end=270, fill=(200, 80, 80), width=8)
    # 壶盖
    draw.ellipse([pot_x-20, pot_y-45, pot_x+20, pot_y-25], fill=(180, 70, 70), outline=(0, 0, 0), width=2)
    
    return img

# ============ 主程序 ============

def main():
    """生成所有日本县塔图片"""
    
    towers = [
        ("tokyo-skytree.png", draw_tokyo_skytree, "东京 - 晴空塔"),
        ("osaka-castle.png", draw_osaka_castle, "大阪 - 大阪城"),
        ("aichi-nagoya.png", draw_aichi_nagoya, "爱知 - 名古屋城"),
        ("kanagawa-fuji.png", draw_kanagawa_fuji, "神奈川 - 富士山+横滨"),
        ("hokkaido-snow.png", draw_hokkaido_snow, "北海道 - 雪景+薰衣草"),
        ("fukuoka-dazaifu.png", draw_fukuoka_dazaifu, "福冈 - 太宰府"),
        ("hyogo-himeji.png", draw_hyogo_himeji, "兵库 - 姬路城"),
        ("kyoto-kinkaku.png", draw_kyoto_kinkaku, "京都 - 金阁寺"),
        ("okinawa-beach.png", draw_okinawa_beach, "冲绳 - 海滩+狮子"),
        ("shizuoka-tea.png", draw_shizuoka_tea, "静冈 - 茶园+富士山"),
    ]
    
    print("🗼 开始生成日本县卡通塔图片...\n")
    
    for filename, draw_func, name in towers:
        print(f"正在生成: {name} -> {filename}")
        try:
            img = draw_func()
            filepath = os.path.join(OUTPUT_DIR, filename)
            img.save(filepath, "PNG")
            print(f"  ✓ 已保存: {filepath}")
        except Exception as e:
            print(f"  ✗ 错误: {e}")
    
    print(f"\n🎉 完成! 所有图片已保存到: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
