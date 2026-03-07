#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成德国州卡通塔图片
风格：愤怒的小鸟卡通风格，可爱表情
"""

from PIL import Image, ImageDraw, ImageFilter
import math
import os

# 输出目录
OUTPUT_DIR = "/Users/moutai/Desktop/toweroffate_v1.0/assets/towers/states/germany/"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 画布尺寸
WIDTH, HEIGHT = 800, 1200

def create_gradient_background(width, height):
    """创建天蓝色渐变背景"""
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    
    # 从天蓝色到浅蓝色的渐变
    for y in range(height):
        ratio = y / height
        # 天蓝色 (#87CEEB) 到 浅天蓝色 (#B0E0E6)
        r = int(135 + (176 - 135) * ratio)
        g = int(206 + (224 - 206) * ratio)
        b = int(235 + (230 - 235) * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    return img

def draw_circle(draw, x, y, r, fill, outline=None, width=2):
    """绘制圆形"""
    draw.ellipse([x-r, y-r, x+r, y+r], fill=fill, outline=outline, width=width)

def draw_rounded_rect(draw, x, y, w, h, radius, fill, outline=None, width=2):
    """绘制圆角矩形"""
    draw.rounded_rectangle([x, y, x+w, y+h], radius=radius, fill=fill, outline=outline, width=width)

def draw_cute_eyes(draw, cx, cy, size=15, look_direction=(0, 0)):
    """绘制可爱的卡通眼睛"""
    eye_spacing = size * 1.8
    eye_y_offset = 0
    
    # 左眼白
    lx, ly = cx - eye_spacing/2 + look_direction[0]*3, cy + eye_y_offset + look_direction[1]*3
    draw.ellipse([lx-size, ly-size, lx+size, ly+size], fill="white", outline="black", width=2)
    # 左眼珠
    draw.ellipse([lx-size*0.3, ly-size*0.3, lx+size*0.3, ly+size*0.3], fill="black")
    # 左眼高光
    draw.ellipse([lx-size*0.15-2, ly-size*0.15-2, lx+size*0.1-2, ly+size*0.1-2], fill="white")
    
    # 右眼白
    rx, ry = cx + eye_spacing/2 + look_direction[0]*3, cy + eye_y_offset + look_direction[1]*3
    draw.ellipse([rx-size, ry-size, rx+size, ry+size], fill="white", outline="black", width=2)
    # 右眼珠
    draw.ellipse([rx-size*0.3, ry-size*0.3, rx+size*0.3, ry+size*0.3], fill="black")
    # 右眼高光
    draw.ellipse([rx-size*0.15-2, ry-size*0.15-2, rx+size*0.1-2, ry+size*0.1-2], fill="white")

def draw_cute_mouth(draw, cx, cy, size=10, smile=True):
    """绘制可爱的卡通嘴巴"""
    if smile:
        # 微笑
        draw.arc([cx-size*1.5, cy-size, cx+size*1.5, cy+size], 0, 180, fill="black", width=3)
    else:
        # O型嘴
        draw.ellipse([cx-size*0.5, cy-size*0.5, cx+size*0.5, cy+size*0.5], fill="#FF6B6B", outline="black", width=2)

def draw_blush(draw, x, y, size=12):
    """绘制腮红"""
    draw.ellipse([x-size, y-size, x+size, y+size], fill="#FFB6C1")

def draw_clouds(draw):
    """绘制装饰云朵"""
    clouds = [
        (100, 150, 40),
        (650, 200, 50),
        (150, 400, 35),
        (700, 500, 45),
        (120, 800, 30),
    ]
    for x, y, r in clouds:
        # 半透明白色云朵
        draw.ellipse([x-r, y-r*0.6, x+r, y+r*0.6], fill=(255, 255, 255, 100))
        draw.ellipse([x-r*0.7, y-r, x+r*0.7, y+r], fill=(255, 255, 255, 100))

def create_cologne_tower():
    """1. 北威 - 科隆大教堂"""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    draw_clouds(draw)
    
    cx, cy = WIDTH//2, HEIGHT//2 + 100
    
    # 教堂基座
    draw.rounded_rectangle([cx-120, cy+200, cx+120, cy+350], radius=10, fill="#8B7355", outline="#5D4E37", width=3)
    
    # 主塔楼
    draw.rounded_rectangle([cx-80, cy-100, cx+80, cy+200], radius=5, fill="#D4C4A8", outline="#8B7355", width=3)
    
    # 双尖塔
    # 左尖塔
    points_left = [(cx-60, cy-100), (cx-40, cy-300), (cx-20, cy-100)]
    draw.polygon(points_left, fill="#E8DCC8", outline="#8B7355", width=3)
    # 右尖塔
    points_right = [(cx+20, cy-100), (cx+40, cy-300), (cx+60, cy-100)]
    draw.polygon(points_right, fill="#E8DCC8", outline="#8B7355", width=3)
    
    # 尖塔顶部十字架
    draw.line([(cx-40, cy-300), (cx-40, cy-320)], fill="#5D4E37", width=4)
    draw.line([(cx-50, cy-310), (cx-30, cy-310)], fill="#5D4E37", width=3)
    draw.line([(cx+40, cy-300), (cx+40, cy-320)], fill="#5D4E37", width=4)
    draw.line([(cx+30, cy-310), (cx+50, cy-310)], fill="#5D4E37", width=3)
    
    # 哥特式窗户装饰
    for i in range(-60, 61, 30):
        draw.ellipse([cx+i-10, cy+50, cx+i+10, cy+90], fill="#4A4A4A", outline="#2F2F2F", width=2)
    
    # 可爱的脸
    draw_cute_eyes(draw, cx, cy-20, size=18, look_direction=(0, -0.5))
    draw_cute_mouth(draw, cx, cy+20, size=12, smile=True)
    draw_blush(draw, cx-70, cy)
    draw_blush(draw, cx+70, cy)
    
    return img

def create_neuschwanstein_tower():
    """2. 巴伐利亚 - 新天鹅堡"""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    draw_clouds(draw)
    
    cx, cy = WIDTH//2, HEIGHT//2 + 100
    
    # 山基座
    points_mountain = [(cx-200, cy+350), (cx, cy+100), (cx+200, cy+350)]
    draw.polygon(points_mountain, fill="#8FBC8F", outline="#556B2F", width=3)
    
    # 城堡主体
    draw.rounded_rectangle([cx-100, cy, cx+100, cy+250], radius=10, fill="#F5F5DC", outline="#D2B48C", width=3)
    
    # 主塔楼
    draw.rounded_rectangle([cx-30, cy-150, cx+30, cy], radius=5, fill="#FFF8DC", outline="#D2B48C", width=3)
    
    # 圆锥形屋顶
    points_roof = [(cx-50, cy-150), (cx, cy-280), (cx+50, cy-150)]
    draw.polygon(points_roof, fill="#CD5C5C", outline="#8B4513", width=3)
    
    # 屋顶旗帜
    draw.line([(cx, cy-280), (cx, cy-310)], fill="#8B4513", width=3)
    draw.polygon([(cx, cy-310), (cx+30, cy-300), (cx, cy-290)], fill="#4169E1", outline="#000080", width=2)
    
    # 侧塔
    draw.rounded_rectangle([cx-80, cy-80, cx-50, cy+50], radius=5, fill="#FFF8DC", outline="#D2B48C", width=3)
    points_side_roof = [(cx-85, cy-80), (cx-65, cy-160), (cx-45, cy-80)]
    draw.polygon(points_side_roof, fill="#4682B4", outline="#2F4F4F", width=3)
    
    draw.rounded_rectangle([cx+50, cy-80, cx+80, cy+50], radius=5, fill="#FFF8DC", outline="#D2B48C", width=3)
    points_side_roof2 = [(cx+45, cy-80), (cx+65, cy-160), (cx+85, cy-80)]
    draw.polygon(points_side_roof2, fill="#4682B4", outline="#2F4F4F", width=3)
    
    # 窗户
    draw.ellipse([cx-15, cy-80, cx+15, cy-40], fill="#4A4A4A", outline="#2F2F2F", width=2)
    
    # 可爱的脸
    draw_cute_eyes(draw, cx, cy+100, size=20, look_direction=(0, 0))
    draw_cute_mouth(draw, cx, cy+150, size=15, smile=True)
    draw_blush(draw, cx-60, cy+120)
    draw_blush(draw, cx+60, cy+120)
    
    return img

def create_black_forest_tower():
    """3. 巴登 - 黑森林"""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    
    cx, cy = WIDTH//2, HEIGHT//2 + 100
    
    # 地面
    draw.rounded_rectangle([0, cy+280, WIDTH, HEIGHT], radius=0, fill="#228B22", outline="#006400", width=3)
    
    # 松树1 - 左
    for i in range(3):
        y_base = cy + 250 - i * 80
        points = [(cx-120, y_base), (cx-180, y_base-120), (cx-60, y_base-120)]
        draw.polygon(points, fill="#006400", outline="#004d00", width=2)
    draw.rounded_rectangle([cx-135, cy+250, cx-105, cy+350], radius=0, fill="#8B4513", outline="#5D3A1A", width=2)
    
    # 松树2 - 中（主塔）
    for i in range(4):
        y_base = cy + 200 - i * 100
        w = 140 - i * 20
        points = [(cx, y_base), (cx-w, y_base-150), (cx+w, y_base-150)]
        color = "#228B22" if i % 2 == 0 else "#32CD32"
        draw.polygon(points, fill=color, outline="#006400", width=2)
    draw.rounded_rectangle([cx-20, cy+200, cx+20, cy+350], radius=0, fill="#8B4513", outline="#5D3A1A", width=3)
    
    # 松树3 - 右
    for i in range(3):
        y_base = cy + 250 - i * 80
        points = [(cx+120, y_base), (cx+60, y_base-120), (cx+180, y_base-120)]
        draw.polygon(points, fill="#006400", outline="#004d00", width=2)
    draw.rounded_rectangle([cx+105, cy+250, cx+135, cy+350], radius=0, fill="#8B4513", outline="#5D3A1A", width=2)
    
    # 森林中的小屋
    draw.rounded_rectangle([cx-40, cy+180, cx+40, cy+250], radius=5, fill="#DEB887", outline="#8B7355", width=2)
    points_roof = [(cx-50, cy+180), (cx, cy+130), (cx+50, cy+180)]
    draw.polygon(points_roof, fill="#8B4513", outline="#5D3A1A", width=2)
    
    # 烟囱
    draw.rounded_rectangle([cx+20, cy+140, cx+35, cy+170], radius=0, fill="#696969", outline="#2F4F4F", width=2)
    # 烟雾
    for i, offset in enumerate([(0, -20), (10, -35), (20, -50)]):
        draw.ellipse([cx+25+offset[0]-10-i*3, cy+130+offset[1]-5, cx+25+offset[0]+10+i*3, cy+130+offset[1]+5], fill=(255,255,255,100), outline=None)
    
    # 可爱的脸（在小屋上）
    draw_cute_eyes(draw, cx, cy+200, size=12, look_direction=(0, 0))
    draw_cute_mouth(draw, cx, cy+225, size=8, smile=True)
    draw_blush(draw, cx-25, cy+210)
    draw_blush(draw, cx+25, cy+210)
    
    return img

def create_frankfurt_tower():
    """4. 黑森 - 法兰克福天际线"""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    draw_clouds(draw)
    
    cx, cy = WIDTH//2, HEIGHT//2 + 150
    
    # 地面
    draw.rounded_rectangle([0, cy+200, WIDTH, HEIGHT], radius=0, fill="#A9A9A9", outline="#696969", width=2)
    
    # 建筑群
    buildings = [
        (-150, 150, 60, "#4682B4"),
        (-80, 200, 70, "#5F9EA0"),
        (-10, 250, 80, "#87CEEB"),
        (70, 180, 65, "#6495ED"),
        (140, 220, 70, "#00CED1"),
    ]
    
    for bx, bh, bw, color in buildings:
        # 建筑主体
        draw.rounded_rectangle([cx+bx-bw//2, cy+200-bh, cx+bx+bw//2, cy+200], radius=3, fill=color, outline="#2F4F4F", width=2)
        # 窗户
        for wy in range(cy+200-bh+20, cy+200, 25):
            for wx in range(cx+bx-bw//2+10, cx+bx+bw//2, 15):
                draw.rectangle([wx, wy, wx+8, wy+12], fill="#FFD700", outline="#B8860B", width=1)
    
    # 商业银行塔（主塔）
    # 塔身
    points_tower = [(cx-40, cy-50), (cx-25, cy-300), (cx+25, cy-300), (cx+40, cy-50)]
    draw.polygon(points_tower, fill="#C0C0C0", outline="#696969", width=3)
    
    # 塔顶尖
    draw.polygon([(cx-25, cy-300), (cx, cy-350), (cx+25, cy-300)], fill="#A9A9A9", outline="#696969", width=2)
    
    # 塔顶红色信标灯
    draw.ellipse([cx-10, cy-360, cx+10, cy-340], fill="#FF0000", outline="#8B0000", width=2)
    
    # 天线
    draw.line([(cx, cy-350), (cx, cy-380)], fill="#696969", width=3)
    
    # 可爱的脸（在主塔上）
    draw_cute_eyes(draw, cx, cy-150, size=16, look_direction=(0, 0))
    draw_cute_mouth(draw, cx, cy-110, size=12, smile=True)
    draw_blush(draw, cx-30, cy-130)
    draw_blush(draw, cx+30, cy-130)
    
    return img

def create_bremen_tower():
    """5. 下萨克森 - 不莱梅音乐家"""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    draw_clouds(draw)
    
    cx, cy = WIDTH//2, HEIGHT//2 + 100
    
    # 地面
    draw.rounded_rectangle([0, cy+250, WIDTH, HEIGHT], radius=0, fill="#9ACD32", outline="#6B8E23", width=3)
    
    # 叠罗汉的动物们（从下往上）
    # 驴（底部）
    draw.ellipse([cx-80, cy+150, cx+80, cy+250], fill="#808080", outline="#4A4A4A", width=3)  # 身体
    draw.ellipse([cx-100, cy+120, cx-40, cy+180], fill="#808080", outline="#4A4A4A", width=3)  # 头
    draw.ellipse([cx-110, cy+100, cx-90, cy+130], fill="#808080", outline="#4A4A4A", width=2)  # 耳朵
    draw.ellipse([cx-80, cy+100, cx-60, cy+130], fill="#808080", outline="#4A4A4A", width=2)  # 耳朵
    # 驴的眼睛
    draw_cute_eyes(draw, cx-70, cy+140, size=8, look_direction=(0, 0))
    
    # 狗
    draw.ellipse([cx-60, cy+50, cx+60, cy+150], fill="#8B4513", outline="#5D3A1A", width=3)  # 身体
    draw.ellipse([cx-80, cy+30, cx-30, cy+80], fill="#8B4513", outline="#5D3A1A", width=3)  # 头
    draw.ellipse([cx-85, cy+15, cx-70, cy+35], fill="#8B4513", outline="#5D3A1A", width=2)  # 耳朵
    draw.ellipse([cx-60, cy+10, cx-45, cy+30], fill="#8B4513", outline="#5D3A1A", width=2)  # 耳朵
    draw_cute_eyes(draw, cx-55, cy+50, size=7, look_direction=(0, 0))
    
    # 猫
    draw.ellipse([cx-45, cy-30, cx+45, cy+50], fill="#FFA500", outline="#FF8C00", width=3)  # 身体
    draw.ellipse([cx-60, cy-60, cx-15, cy-20], fill="#FFA500", outline="#FF8C00", width=3)  # 头
    # 猫耳朵
    draw.polygon([(cx-55, cy-55), (cx-45, cy-80), (cx-35, cy-55)], fill="#FFA500", outline="#FF8C00", width=2)
    draw.polygon([(cx-35, cy-50), (cx-25, cy-75), (cx-15, cy-50)], fill="#FFA500", outline="#FF8C00", width=2)
    draw_cute_eyes(draw, cx-38, cy-45, size=6, look_direction=(0, 0))
    
    # 公鸡（顶部 - 主塔）
    # 身体
    draw.ellipse([cx-30, cy-100, cx+30, cy-30], fill="#FFFFFF", outline="#C0C0C0", width=3)
    # 头
    draw.ellipse([cx-25, cy-140, cx+10, cy-100], fill="#FFFFFF", outline="#C0C0C0", width=3)
    # 鸡冠
    draw.ellipse([cx-20, cy-155, cx-5, cy-135], fill="#FF0000", outline="#8B0000", width=2)
    draw.ellipse([cx-10, cy-160, cx+5, cy-140], fill="#FF0000", outline="#8B0000", width=2)
    # 喙
    draw.polygon([(cx+5, cy-125), (cx+20, cy-120), (cx+5, cy-115)], fill="#FFD700", outline="#B8860B", width=2)
    # 尾巴羽毛
    for i, angle in enumerate([-30, -15, 0, 15, 30]):
        tx = cx + 35 + int(25 * math.sin(math.radians(angle)))
        ty = cy - 80 + int(15 * math.cos(math.radians(angle)))
        draw.ellipse([tx-8, ty-15, tx+8, ty+15], fill="#228B22", outline="#006400", width=2)
    
    # 公鸡可爱的脸（主表情）
    draw_cute_eyes(draw, cx-8, cy-115, size=9, look_direction=(0, 0))
    draw_blush(draw, cx-25, cy-110)
    
    return img

def create_berlin_gate_tower():
    """6. 柏林 - 勃兰登堡门"""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    draw_clouds(draw)
    
    cx, cy = WIDTH//2, HEIGHT//2 + 100
    
    # 地面
    draw.rounded_rectangle([0, cy+300, WIDTH, HEIGHT], radius=0, fill="#D3D3D3", outline="#A9A9A9", width=3)
    
    # 门柱
    columns = [-120, -40, 40, 120]
    for col_x in columns:
        # 柱基
        draw.rounded_rectangle([cx+col_x-25, cy+250, cx+col_x+25, cy+300], radius=3, fill="#D4C4A8", outline="#8B7355", width=2)
        # 柱身
        draw.rounded_rectangle([cx+col_x-20, cy, cx+col_x+20, cy+250], radius=3, fill="#E8DCC8", outline="#8B7355", width=3)
        # 柱顶
        draw.rounded_rectangle([cx+col_x-25, cy-30, cx+col_x+25, cy], radius=3, fill="#D4C4A8", outline="#8B7355", width=2)
    
    # 横梁
    draw.rounded_rectangle([cx-160, cy-60, cx+160, cy-30], radius=5, fill="#D4C4A8", outline="#8B7355", width=3)
    
    # 顶部雕塑（简化版四马战车）
    # 基座
    draw.rounded_rectangle([cx-100, cy-120, cx+100, cy-60], radius=5, fill="#E8DCC8", outline="#8B7355", width=3)
    
    # 马车主体（卡通化）
    draw.ellipse([cx-60, cy-150, cx+60, cy-90], fill="#CD853F", outline="#8B4513", width=3)
    
    # 马（简化）
    for i, hx in enumerate([-70, -35, 35, 70]):
        # 马身体
        draw.ellipse([cx+hx-15, cy-160, cx+hx+15, cy-130], fill="#F4A460", outline="#8B4513", width=2)
        # 马头
        draw.ellipse([cx+hx-10, cy-175, cx+hx+5, cy-150], fill="#F4A460", outline="#8B4513", width=2)
    
    # 胜利女神雕像（简化）
    draw.ellipse([cx-20, cy-180, cx+20, cy-140], fill="#FFD700", outline="#B8860B", width=3)
    # 翅膀
    draw.polygon([(cx-20, cy-160), (cx-60, cy-140), (cx-30, cy-150)], fill="#FFD700", outline="#B8860B", width=2)
    draw.polygon([(cx+20, cy-160), (cx+60, cy-140), (cx+30, cy-150)], fill="#FFD700", outline="#B8860B", width=2)
    
    # 可爱的脸（在中间柱子上方）
    draw_cute_eyes(draw, cx, cy-100, size=18, look_direction=(0, 0))
    draw_cute_mouth(draw, cx, cy-65, size=12, smile=True)
    draw_blush(draw, cx-50, cy-80)
    draw_blush(draw, cx+50, cy-80)
    
    return img

def create_hamburg_port_tower():
    """7. 汉堡 - 港口+易北爱乐"""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    draw_clouds(draw)
    
    cx, cy = WIDTH//2, HEIGHT//2 + 150
    
    # 水面
    draw.rounded_rectangle([0, cy+100, WIDTH, HEIGHT], radius=0, fill="#4682B4", outline="#2F4F4F", width=3)
    # 水波纹
    for i in range(5):
        y_wave = cy + 150 + i * 40
        for x in range(0, WIDTH, 100):
            draw.arc([x, y_wave-5, x+50, y_wave+5], 0, 180, fill="#87CEEB", width=2)
    
    # 码头/仓库建筑
    draw.rounded_rectangle([cx-150, cy+50, cx+50, cy+150], radius=5, fill="#CD853F", outline="#8B4513", width=3)
    # 仓库窗户
    for wy in range(cy+70, cy+140, 30):
        for wx in range(cx-130, cx+40, 25):
            draw.rectangle([wx, wy, wx+15, wy+20], fill="#4A4A4A", outline="#2F2F2F", width=1)
    
    # 易北爱乐厅（波浪屋顶建筑）
    # 玻璃波浪屋顶
    wave_points = []
    for x in range(cx-80, cx+81, 10):
        y = cy - 100 + int(30 * math.sin(x * 0.05))
        wave_points.append((cx+x, y))
    wave_points.extend([(cx+80, cy+50), (cx-80, cy+50)])
    draw.polygon(wave_points, fill="#87CEEB", outline="#4682B4", width=3)
    
    # 建筑主体
    draw.rounded_rectangle([cx-60, cy-50, cx+60, cy+50], radius=5, fill="#F5F5DC", outline="#D2B48C", width=3)
    
    # 起重机
    draw.line([(cx+100, cy+150), (cx+100, cy-50)], fill="#FF8C00", width=8)
    draw.line([(cx+100, cy-50), (cx+180, cy-30)], fill="#FF8C00", width=6)
    draw.line([(cx+100, cy-20), (cx+160, cy-10)], fill="#FF8C00", width=4)
    # 吊钩
    draw.arc([cx+155, cy-10, cx+165, cy+10], 0, 180, fill="#696969", width=3)
    
    # 货船
    draw.polygon([(cx-180, cy+80), (cx-180, cy+140), (cx-80, cy+140), (cx-60, cy+80)], fill="#8B4513", outline="#5D3A1A", width=3)
    draw.rectangle([cx-170, cy+60, cx-130, cy+80], fill="#F5F5DC", outline="#D2B48C", width=2)
    draw.rectangle([cx-120, cy+50, cx-90, cy+80], fill="#F5F5DC", outline="#D2B48C", width=2)
    
    # 可爱的脸（在易北爱乐厅上）
    draw_cute_eyes(draw, cx, cy-20, size=16, look_direction=(0, 0))
    draw_cute_mouth(draw, cx, cy+10, size=12, smile=True)
    draw_blush(draw, cx-40, cy)
    draw_blush(draw, cx+40, cy)
    
    return img

def create_rhineland_castle_tower():
    """8. 莱茵兰 - 城堡"""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    draw_clouds(draw)
    
    cx, cy = WIDTH//2, HEIGHT//2 + 100
    
    # 小山基座
    points_hill = [(cx-180, cy+350), (cx-100, cy+200), (cx, cy+150), (cx+100, cy+200), (cx+180, cy+350)]
    draw.polygon(points_hill, fill="#228B22", outline="#006400", width=3)
    
    # 主城堡塔楼
    draw.rounded_rectangle([cx-50, cy-50, cx+50, cy+200], radius=5, fill="#D4C4A8", outline="#8B7355", width=3)
    
    # 塔顶屋顶
    points_roof = [(cx-60, cy-50), (cx, cy-180), (cx+60, cy-50)]
    draw.polygon(points_roof, fill="#B22222", outline="#8B0000", width=3)
    
    # 旗帜
    draw.line([(cx, cy-180), (cx, cy-210)], fill="#8B4513", width=3)
    draw.polygon([(cx, cy-210), (cx+40, cy-200), (cx, cy-190)], fill="#4169E1", outline="#000080", width=2)
    
    # 侧塔
    draw.rounded_rectangle([cx-100, cy+50, cx-60, cy+180], radius=5, fill="#E8DCC8", outline="#8B7355", width=3)
    points_side_roof = [(cx-110, cy+50), (cx-80, cy-20), (cx-50, cy+50)]
    draw.polygon(points_side_roof, fill="#4682B4", outline="#2F4F4F", width=3)
    
    draw.rounded_rectangle([cx+60, cy+50, cx+100, cy+180], radius=5, fill="#E8DCC8", outline="#8B7355", width=3)
    points_side_roof2 = [(cx+50, cy+50), (cx+80, cy-20), (cx+110, cy+50)]
    draw.polygon(points_side_roof2, fill="#4682B4", outline="#2F4F4F", width=3)
    
    # 城墙
    draw.rounded_rectangle([cx-120, cy+180, cx+120, cy+220], radius=3, fill="#A9A9A9", outline="#696969", width=3)
    
    # 垛口
    for i in range(-110, 111, 30):
        draw.rectangle([cx+i, cy+180, cx+i+15, cy+200], fill="#D4C4A8", outline="#8B7355", width=2)
    
    # 主塔窗户
    draw.ellipse([cx-20, cy+80, cx+20, cy+140], fill="#4A4A4A", outline="#2F2F2F", width=2)
    
    # 可爱的脸（在主塔上）
    draw_cute_eyes(draw, cx, cy+20, size=18, look_direction=(0, 0))
    draw_cute_mouth(draw, cx, cy+55, size=12, smile=True)
    draw_blush(draw, cx-35, cy+35)
    draw_blush(draw, cx+35, cy+35)
    
    return img

def create_saxony_dresden_tower():
    """9. 萨克森 - 德累斯顿"""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    draw_clouds(draw)
    
    cx, cy = WIDTH//2, HEIGHT//2 + 100
    
    # 地面（易北河岸）
    draw.rounded_rectangle([0, cy+300, WIDTH, HEIGHT], radius=0, fill="#9ACD32", outline="#6B8E23", width=3)
    
    # 教堂主体（圣母教堂）
    # 圆顶建筑
    draw.ellipse([cx-100, cy-50, cx+100, cy+150], fill="#F5F5DC", outline="#D2B48C", width=3)
    
    # 大圆顶
    draw.ellipse([cx-70, cy-150, cx+70, cy-10], fill="#87CEEB", outline="#4682B4", width=3)
    
    # 圆顶顶部十字架
    draw.line([(cx, cy-150), (cx, cy-180)], fill="#FFD700", width=4)
    draw.line([(cx-15, cy-165), (cx+15, cy-165)], fill="#FFD700", width=3)
    
    # 四个小塔楼
    tower_positions = [(-80, -20), (80, -20), (-80, 100), (80, 100)]
    for tx, ty in tower_positions:
        draw.rounded_rectangle([cx+tx-15, cy+ty-40, cx+tx+15, cy+ty+40], radius=3, fill="#F5F5DC", outline="#D2B48C", width=2)
        draw.polygon([(cx+tx-18, cy+ty-40), (cx+tx, cy+ty-80), (cx+tx+18, cy+ty-40)], fill="#87CEEB", outline="#4682B4", width=2)
        # 小十字架
        draw.line([(cx+tx, cy+ty-80), (cx+tx, cy+ty-95)], fill="#FFD700", width=2)
        draw.line([(cx+tx-5, cy+ty-88), (cx+tx+5, cy+ty-88)], fill="#FFD700", width=2)
    
    # 巴洛克装饰（简化）
    for i in range(-60, 61, 30):
        draw.ellipse([cx+i-8, cy+20, cx+i+8, cy+36], fill="#FFD700", outline="#B8860B", width=1)
    
    # 可爱的脸（在教堂正面）
    draw_cute_eyes(draw, cx, cy+50, size=18, look_direction=(0, 0))
    draw_cute_mouth(draw, cx, cy+90, size=12, smile=True)
    draw_blush(draw, cx-60, cy+70)
    draw_blush(draw, cx+60, cy+70)
    
    return img

def create_thuringen_weimar_tower():
    """10. 图林根 - 魏玛包豪斯"""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    draw_clouds(draw)
    
    cx, cy = WIDTH//2, HEIGHT//2 + 100
    
    # 地面
    draw.rounded_rectangle([0, cy+250, WIDTH, HEIGHT], radius=0, fill="#F5DEB3", outline="#D2B48C", width=3)
    
    # 包豪斯风格建筑 - 简洁的几何形状
    # 主建筑块（白色立方体）
    draw.rounded_rectangle([cx-100, cy, cx+100, cy+250], radius=5, fill="#FFFFFF", outline="#C0C0C0", width=3)
    
    # 大面积玻璃窗（包豪斯特色）
    # 左侧玻璃窗
    draw.rounded_rectangle([cx-80, cy+30, cx-20, cy+150], radius=3, fill="#87CEEB", outline="#4682B4", width=2)
    # 窗户网格
    for i in range(cx-80, cx-10, 20):
        draw.line([(i, cy+30), (i, cy+150)], fill="#4682B4", width=1)
    for j in range(cy+30, cy+160, 30):
        draw.line([(cx-80, j), (cx-20, j)], fill="#4682B4", width=1)
    
    # 右侧阳台
    draw.rounded_rectangle([cx+20, cy+80, cx+80, cy+120], radius=3, fill="#F5F5DC", outline="#D2B48C", width=2)
    # 阳台栏杆
    for i in range(cx+25, cx+76, 10):
        draw.line([(i, cy+80), (i, cy+100)], fill="#696969", width=2)
    draw.line([(cx+20, cy+100), (cx+80, cy+100)], fill="#696969", width=3)
    
    # 悬挑屋顶
    draw.rounded_rectangle([cx-120, cy-30, cx+120, cy], radius=3, fill="#F5F5DC", outline="#D2B48C", width=3)
    
    # 圆形楼梯塔（包豪斯经典元素）
    draw.ellipse([cx+60, cy-100, cx+120, cy-20], fill="#E8E8E8", outline="#A9A9A9", width=3)
    # 螺旋楼梯效果
    for i in range(5):
        y = cy - 90 + i * 15
        draw.arc([cx+65, y, cx+115, y+30], 0, 180, fill="#696969", width=2)
    
    # 几何装饰元素
    # 红黄蓝三原色（包豪斯色彩）
    draw.rectangle([cx-90, cy+180, cx-50, cy+220], fill="#FF0000", outline="#8B0000", width=2)  # 红
    draw.rectangle([cx-40, cy+180, cx, cy+220], fill="#FFD700", outline="#B8860B", width=2)  # 黄
    draw.rectangle([cx+10, cy+180, cx+50, cy+220], fill="#0000FF", outline="#000080", width=2)  # 蓝
    
    # 钢管椅子（包豪斯设计经典）
    # 椅子靠背
    draw.rectangle([cx+60, cy+200, cx+90, cy+240], fill="#87CEEB", outline="#4682B4", width=2)
    # 椅子腿（钢管）
    draw.line([(cx+60, cy+240), (cx+60, cy+250)], fill="#696969", width=3)
    draw.line([(cx+90, cy+240), (cx+90, cy+250)], fill="#696969", width=3)
    
    # 可爱的脸（在建筑正面）
    draw_cute_eyes(draw, cx, cy-100, size=16, look_direction=(0, 0))
    draw_cute_mouth(draw, cx, cy-70, size=12, smile=True)
    draw_blush(draw, cx-60, cy-85)
    draw_blush(draw, cx+60, cy-85)
    
    return img

def main():
    """主函数：生成所有塔图片"""
    towers = [
        ("nrw-cologne.png", create_cologne_tower, "北威 - 科隆大教堂"),
        ("bavaria-neuschwanstein.png", create_neuschwanstein_tower, "巴伐利亚 - 新天鹅堡"),
        ("baden-black-forest.png", create_black_forest_tower, "巴登 - 黑森林"),
        ("hessen-frankfurt.png", create_frankfurt_tower, "黑森 - 法兰克福天际线"),
        ("lower-saxony-bremen.png", create_bremen_tower, "下萨克森 - 不莱梅音乐家"),
        ("berlin-gate.png", create_berlin_gate_tower, "柏林 - 勃兰登堡门"),
        ("hamburg-port.png", create_hamburg_port_tower, "汉堡 - 港口+易北爱乐"),
        ("rhineland-castle.png", create_rhineland_castle_tower, "莱茵兰 - 城堡"),
        ("saxony-dresden.png", create_saxony_dresden_tower, "萨克森 - 德累斯顿"),
        ("thuringen-weimar.png", create_thuringen_weimar_tower, "图林根 - 魏玛包豪斯"),
    ]
    
    print("开始生成德国州卡通塔图片...")
    print("=" * 50)
    
    for filename, create_func, name in towers:
        try:
            print(f"正在生成: {name} -> {filename}")
            img = create_func()
            filepath = os.path.join(OUTPUT_DIR, filename)
            img.save(filepath, "PNG")
            print(f"✓ 已保存: {filepath}")
        except Exception as e:
            print(f"✗ 生成失败 {filename}: {e}")
    
    print("=" * 50)
    print("所有图片生成完成！")

if __name__ == "__main__":
    main()
