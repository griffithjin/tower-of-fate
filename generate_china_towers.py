#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成中国省份卡通塔图片 - 愤怒的小鸟风格
"""

from PIL import Image, ImageDraw, ImageFilter
import math
import os

OUTPUT_DIR = "/Users/moutai/Desktop/toweroffate_v1.0/assets/towers/states/china/"

def create_gradient_background(width, height):
    """创建天蓝色渐变背景"""
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    
    # 天蓝色渐变: 从浅蓝到稍深的蓝
    for y in range(height):
        ratio = y / height
        r = int(135 + (100 - 135) * ratio)  # 135 -> 100
        g = int(206 + (180 - 206) * ratio)  # 206 -> 180
        b = int(235 + (255 - 235) * ratio)  # 235 -> 255
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    return img

def draw_angry_eyes(draw, cx, cy, eye_radius, pupil_radius, eye_spacing, is_angry=True):
    """绘制愤怒的小鸟风格的眼睛"""
    # 左眼球
    left_eye_x = cx - eye_spacing//2
    draw.ellipse([left_eye_x - eye_radius, cy - eye_radius, 
                  left_eye_x + eye_radius, cy + eye_radius], 
                 fill=(255, 255, 255), outline=(0, 0, 0), width=3)
    # 左瞳孔
    draw.ellipse([left_eye_x - pupil_radius//2 - 3, cy - pupil_radius//2 - 3, 
                  left_eye_x + pupil_radius//2 - 3, cy + pupil_radius//2 - 3], 
                 fill=(0, 0, 0))
    
    # 右眼球
    right_eye_x = cx + eye_spacing//2
    draw.ellipse([right_eye_x - eye_radius, cy - eye_radius, 
                  right_eye_x + eye_radius, cy + eye_radius], 
                 fill=(255, 255, 255), outline=(0, 0, 0), width=3)
    # 右瞳孔
    draw.ellipse([right_eye_x - pupil_radius//2 + 3, cy - pupil_radius//2 - 3, 
                  right_eye_x + pupil_radius//2 + 3, cy + pupil_radius//2 - 3], 
                 fill=(0, 0, 0))
    
    # 愤怒眉毛
    if is_angry:
        brow_y = cy - eye_radius - 5
        # 左眉毛 (向下倾斜)
        draw.polygon([
            (left_eye_x - eye_radius - 5, brow_y - 5),
            (left_eye_x + eye_radius + 5, brow_y + 8),
            (left_eye_x + eye_radius + 10, brow_y + 15),
            (left_eye_x - eye_radius, brow_y + 3)
        ], fill=(50, 30, 20), outline=(0, 0, 0))
        # 右眉毛 (向下倾斜)
        draw.polygon([
            (right_eye_x + eye_radius + 5, brow_y - 5),
            (right_eye_x - eye_radius - 5, brow_y + 8),
            (right_eye_x - eye_radius - 10, brow_y + 15),
            (right_eye_x + eye_radius, brow_y + 3)
        ], fill=(50, 30, 20), outline=(0, 0, 0))

def draw_cute_mouth(draw, cx, cy, size, style="smile"):
    """绘制可爱的嘴巴"""
    if style == "smile":
        draw.arc([cx - size, cy - size//2, cx + size, cy + size], 
                 start=0, end=180, fill=(200, 50, 50), width=4)
    elif style == "open":
        draw.ellipse([cx - size//2, cy, cx + size//2, cy + size], 
                    fill=(200, 80, 80), outline=(150, 40, 40), width=2)
    elif style == "small":
        draw.ellipse([cx - size//3, cy, cx + size//3, cy + size//2], 
                    fill=(200, 80, 80), outline=(150, 40, 40), width=2)

def draw_cheeks(draw, cx, cy, size):
    """绘制腮红"""
    left_cheek_color = (255, 180, 180)
    right_cheek_color = (255, 180, 180)
    draw.ellipse([cx - 60 - size, cy - size//2, cx - 40 + size, cy + size//2], 
                 fill=left_cheek_color)
    draw.ellipse([cx + 40 - size, cy - size//2, cx + 60 + size, cy + size//2], 
                 fill=right_cheek_color)

# ==================== 1. 广东 - 广州塔 ====================
def create_guangdong():
    img = create_gradient_background(800, 1200)
    draw = ImageDraw.Draw(img)
    
    cx, cy = 400, 650
    
    # 广州塔 - 纤细的小蛮腰
    # 塔身颜色
    tower_color = (220, 60, 60)  # 红色
    tower_highlight = (255, 120, 120)
    
    # 塔身 (小蛮腰形状)
    # 上半部分
    draw.polygon([
        (cx - 30, cy - 200), (cx + 30, cy - 200),
        (cx + 80, cy - 50), (cx - 80, cy - 50)
    ], fill=tower_color, outline=(150, 40, 40), width=3)
    # 中间收腰
    draw.polygon([
        (cx - 80, cy - 50), (cx + 80, cy - 50),
        (cx + 50, cy + 100), (cx - 50, cy + 100)
    ], fill=(200, 50, 50), outline=(150, 40, 40), width=3)
    # 下半部分
    draw.polygon([
        (cx - 50, cy + 100), (cx + 50, cy + 100),
        (cx + 100, cy + 300), (cx - 100, cy + 300)
    ], fill=tower_color, outline=(150, 40, 40), width=3)
    
    # 塔顶天线
    draw.line([(cx, cy - 200), (cx, cy - 280)], fill=(100, 100, 100), width=6)
    draw.ellipse([cx - 8, cy - 290, cx + 8, cy - 274], fill=(255, 50, 50))
    
    # 装饰线条
    for i in range(-150, 250, 40):
        y = cy + i
        if cy - 50 < y < cy + 100:
            w = 30 + abs(y - cy + 50) // 3
        else:
            w = 60 + abs(i) // 5
        draw.line([(cx - w, y), (cx + w, y)], fill=(255, 150, 150), width=2)
    
    # 脸部表情
    face_y = cy - 20
    draw_angry_eyes(draw, cx, face_y, 35, 18, 70)
    draw_cute_mouth(draw, cx, face_y + 50, 25, "smile")
    draw_cheeks(draw, cx, face_y + 30, 15)
    
    # 底部云朵装饰
    for i, x in enumerate([150, 400, 650]):
        cloud_y = 1000 + (i % 2) * 30
        draw.ellipse([x - 60, cloud_y, x + 60, cloud_y + 50], fill=(255, 255, 255))
        draw.ellipse([x - 30, cloud_y - 20, x + 30, cloud_y + 30], fill=(255, 255, 255))
    
    return img

# ==================== 2. 江苏 - 苏州园林 ====================
def create_jiangsu():
    img = create_gradient_background(800, 1200)
    draw = ImageDraw.Draw(img)
    
    cx, cy = 400, 600
    
    # 园林亭子
    # 屋顶 (多层飞檐)
    roof_colors = [(180, 60, 60), (160, 50, 50), (140, 40, 40)]
    for i, (y_offset, w, color) in enumerate([(0, 180, roof_colors[0]), 
                                               (-30, 140, roof_colors[1]), 
                                               (-55, 100, roof_colors[2])]):
        y = cy - 100 + y_offset
        # 飞檐形状
        draw.polygon([
            (cx - w - 20, y + 20), (cx - w, y), (cx, y - 30), 
            (cx + w, y), (cx + w + 20, y + 20)
        ], fill=color, outline=(80, 30, 30), width=3)
    
    # 柱子
    pillar_color = (139, 90, 43)
    for x_offset in [-120, -60, 60, 120]:
        draw.rectangle([cx + x_offset - 12, cy - 80, cx + x_offset + 12, cy + 150], 
                      fill=pillar_color, outline=(100, 60, 30), width=2)
    
    # 围栏
    draw.rectangle([cx - 130, cy + 100, cx + 130, cy + 120], 
                  fill=(160, 110, 60), outline=(100, 60, 30), width=2)
    for x in range(cx - 120, cx + 121, 30):
        draw.rectangle([x - 3, cy + 100, x + 3, cy + 140], fill=(160, 110, 60))
    
    # 假山/石头装饰
    stone_color = (140, 140, 130)
    draw.polygon([
        (cx - 180, cy + 180), (cx - 150, cy + 80), 
        (cx - 100, cy + 120), (cx - 80, cy + 180)
    ], fill=stone_color, outline=(100, 100, 90), width=2)
    draw.polygon([
        (cx + 100, cy + 180), (cx + 130, cy + 90), 
        (cx + 170, cy + 130), (cx + 190, cy + 180)
    ], fill=stone_color, outline=(100, 100, 90), width=2)
    
    # 脸部表情 (在亭子上)
    face_y = cy - 140
    draw_angry_eyes(draw, cx, face_y, 30, 15, 60)
    draw_cute_mouth(draw, cx, face_y + 35, 20, "small")
    draw_cheeks(draw, cx, face_y + 20, 12)
    
    # 底部装饰
    for x in [100, 300, 500, 700]:
        draw.ellipse([x - 40, 1000, x + 40, 1040], fill=(100, 180, 100))
        draw.ellipse([x - 20, 980, x + 20, 1020], fill=(120, 200, 120))
    
    return img

# ==================== 3. 山东 - 泰山 ====================
def create_shandong():
    img = create_gradient_background(800, 1200)
    draw = ImageDraw.Draw(img)
    
    cx, cy = 400, 500
    
    # 山峰主体 (泰山)
    mountain_color = (100, 120, 100)
    mountain_highlight = (130, 150, 130)
    
    # 主峰
    draw.polygon([
        (cx, cy - 250), (cx + 150, cy + 100), (cx - 150, cy + 100)
    ], fill=mountain_color, outline=(60, 80, 60), width=4)
    # 山顶积雪
    draw.polygon([
        (cx, cy - 250), (cx + 40, cy - 180), (cx - 40, cy - 180)
    ], fill=(240, 240, 255), outline=(200, 200, 220), width=2)
    
    # 左副峰
    draw.polygon([
        (cx - 100, cy - 150), (cx - 20, cy + 100), (cx - 200, cy + 100)
    ], fill=(120, 140, 120), outline=(80, 100, 80), width=3)
    # 右副峰
    draw.polygon([
        (cx + 100, cy - 130), (cx + 220, cy + 100), (cx + 40, cy + 100)
    ], fill=(90, 110, 90), outline=(60, 80, 60), width=3)
    
    # 南天门 (山顶建筑)
    arch_color = (180, 60, 60)
    draw.rectangle([cx - 40, cy - 80, cx + 40, cy - 40], fill=arch_color, outline=(120, 40, 40), width=2)
    draw.polygon([
        (cx - 50, cy - 80), (cx, cy - 110), (cx + 50, cy - 80)
    ], fill=(200, 80, 80), outline=(120, 40, 40), width=2)
    # 拱门
    draw.arc([cx - 25, cy - 70, cx + 25, cy - 30], start=0, end=180, fill=(80, 30, 30))
    
    # 登山步道
    path_color = (180, 160, 140)
    for i, y in enumerate(range(cy + 100, cy + 350, 30)):
        w = 30 + i * 5
        draw.rectangle([cx - w, y, cx + w, y + 20], fill=path_color, outline=(140, 120, 100), width=1)
    
    # 脸部表情 (在山腰)
    face_y = cy - 30
    draw_angry_eyes(draw, cx, face_y, 35, 18, 70)
    draw_cute_mouth(draw, cx, face_y + 50, 25, "smile")
    draw_cheeks(draw, cx, face_y + 30, 15)
    
    # 松树装饰
    for x in [200, 600]:
        trunk_color = (100, 80, 60)
        draw.rectangle([x - 10, 800, x + 10, 950], fill=trunk_color)
        for y in [780, 820, 860]:
            draw.ellipse([x - 50, y - 30, x + 50, y + 30], fill=(40, 100, 40))
    
    return img

# ==================== 4. 浙江 - 西湖 ====================
def create_zhejiang():
    img = create_gradient_background(800, 1200)
    draw = ImageDraw.Draw(img)
    
    cx, cy = 400, 550
    
    # 西湖水面
    water_color = (100, 180, 220)
    draw.rectangle([0, cy + 100, 800, 1200], fill=water_color)
    # 水波纹
    for y in range(cy + 120, 1200, 40):
        for x in range(0, 801, 150):
            draw.arc([x, y, x + 80, y + 20], start=0, end=180, fill=(120, 200, 240))
    
    # 断桥/拱桥
    bridge_color = (180, 150, 120)
    # 桥拱 - 使用多个弧线模拟
    for i, offset in enumerate([(140, 10), (120, 8), (100, 6), (80, 4), (60, 2)]):
        w, thickness = offset
        color = (180 - i*10, 150 - i*10, 120 - i*10)
        draw.arc([cx - w, cy + 50, cx + w, cy + 150], start=0, end=180, fill=color)
    # 桥面
    draw.rectangle([cx - 150, cy + 95, cx + 150, cy + 105], fill=(160, 130, 100))
    # 桥栏杆
    for x in range(cx - 140, cx + 141, 20):
        draw.line([(x, cy + 80), (x, cy + 60)], fill=(160, 130, 100), width=4)
    draw.line([(cx - 150, cy + 65), (cx + 150, cy + 65)], fill=(160, 130, 100), width=4)
    
    # 三潭印月 (三座石塔)
    tower_color = (160, 160, 150)
    for x_offset in [-200, 0, 200]:
        tx = cx + x_offset
        ty = cy + 180
        # 塔身
        draw.rectangle([tx - 20, ty - 80, tx + 20, ty], fill=tower_color, outline=(120, 120, 110), width=2)
        # 塔顶
        draw.polygon([
            (tx - 25, ty - 80), (tx, ty - 110), (tx + 25, ty - 80)
        ], fill=(140, 140, 130), outline=(100, 100, 90), width=2)
        # 圆形孔洞
        draw.ellipse([tx - 12, ty - 50, tx + 12, ty - 20], fill=(80, 140, 180), outline=(100, 100, 90), width=2)
        # 水中倒影
        draw.ellipse([tx - 15, ty + 20, tx + 15, ty + 50], fill=(80, 160, 200, 128))
    
    # 脸部表情 (在中间石塔上)
    face_y = cy - 50
    draw_angry_eyes(draw, cx, face_y, 25, 12, 50)
    draw_cute_mouth(draw, cx, face_y + 35, 18, "small")
    draw_cheeks(draw, cx, face_y + 20, 10)
    
    # 荷花装饰
    for x in [150, 650]:
        # 荷叶
        draw.ellipse([x - 60, cy + 250, x + 60, cy + 320], fill=(80, 160, 80), outline=(60, 130, 60), width=2)
        # 荷花
        draw.ellipse([x - 20, cy + 230, x + 20, cy + 270], fill=(255, 150, 180), outline=(230, 120, 150), width=2)
    
    return img

# ==================== 5. 河南 - 少林寺 ====================
def create_henan():
    img = create_gradient_background(800, 1200)
    draw = ImageDraw.Draw(img)
    
    cx, cy = 400, 550
    
    # 寺庙主殿
    wall_color = (200, 180, 150)
    roof_color = (170, 60, 60)
    
    # 殿身
    draw.rectangle([cx - 120, cy - 50, cx + 120, cy + 150], 
                  fill=wall_color, outline=(150, 130, 100), width=3)
    
    # 大门
    draw.rectangle([cx - 40, cy + 20, cx + 40, cy + 150], 
                  fill=(120, 80, 60), outline=(80, 50, 40), width=3)
    # 门环
    draw.ellipse([cx - 25, cy + 60, cx - 15, cy + 70], fill=(180, 160, 80))
    draw.ellipse([cx + 15, cy + 60, cx + 25, cy + 70], fill=(180, 160, 80))
    
    # 屋顶
    draw.polygon([
        (cx - 160, cy - 50), (cx - 120, cy - 100), 
        (cx, cy - 140), (cx + 120, cy - 100), (cx + 160, cy - 50)
    ], fill=roof_color, outline=(120, 40, 40), width=4)
    
    # 屋顶装饰
    draw.ellipse([cx - 15, cy - 155, cx + 15, cy - 125], fill=(200, 180, 80))
    
    # 两侧配殿
    for x_offset in [-180, 180]:
        x = cx + x_offset
        draw.rectangle([x - 50, cy - 20, x + 50, cy + 100], 
                      fill=wall_color, outline=(150, 130, 100), width=2)
        draw.polygon([
            (x - 60, cy - 20), (x - 40, cy - 60), 
            (x + 40, cy - 60), (x + 60, cy - 20)
        ], fill=roof_color, outline=(120, 40, 40), width=3)
    
    # 塔林 (前景小塔)
    for i, x in enumerate([150, 250, 550, 650]):
        h = 60 + (i % 2) * 20
        draw.rectangle([x - 15, cy + 150 - h, x + 15, cy + 150], 
                      fill=(160, 150, 140), outline=(130, 120, 110), width=2)
        draw.polygon([
            (x - 20, cy + 150 - h), (x, cy + 150 - h - 20), (x + 20, cy + 150 - h)
        ], fill=(140, 130, 120), outline=(110, 100, 90), width=2)
    
    # 脸部表情 (在主殿上)
    face_y = cy - 80
    draw_angry_eyes(draw, cx, face_y, 30, 15, 60)
    draw_cute_mouth(draw, cx, face_y + 35, 20, "smile")
    draw_cheeks(draw, cx, face_y + 20, 12)
    
    # 底部石板路
    for y in range(cy + 200, cy + 350, 30):
        for x in range(100, 701, 80):
            draw.rectangle([x - 30, y, x + 30, y + 25], 
                          fill=(180, 170, 160), outline=(150, 140, 130), width=1)
    
    return img

# ==================== 6. 四川 - 大熊猫 ====================
def create_sichuan():
    img = create_gradient_background(800, 1200)
    draw = ImageDraw.Draw(img)
    
    cx, cy = 400, 600
    
    # 竹林背景
    bamboo_color = (100, 180, 100)
    for x in [100, 200, 600, 700]:
        # 竹子主干
        draw.rectangle([x - 8, cy - 300, x + 8, cy + 300], fill=bamboo_color, outline=(70, 140, 70), width=2)
        # 竹节
        for y in range(cy - 250, cy + 250, 50):
            draw.line([(x - 10, y), (x + 10, y)], fill=(80, 160, 80), width=3)
        # 竹叶
        for y in [cy - 280, cy - 180, cy - 80]:
            draw.polygon([(x - 30, y), (x, y - 20), (x + 30, y), (x, y + 10)], 
                        fill=(120, 200, 120), outline=(80, 160, 80), width=1)
    
    # 熊猫主体
    panda_white = (240, 240, 240)
    panda_black = (40, 40, 40)
    
    # 身体
    draw.ellipse([cx - 130, cy + 50, cx + 130, cy + 280], fill=panda_black, outline=(20, 20, 20), width=3)
    # 白色肚皮
    draw.ellipse([cx - 80, cy + 80, cx + 80, cy + 240], fill=panda_white, outline=(200, 200, 200), width=2)
    
    # 头
    head_y = cy - 80
    draw.ellipse([cx - 110, head_y - 80, cx + 110, head_y + 80], 
                fill=panda_white, outline=(200, 200, 200), width=3)
    
    # 黑眼圈
    for x_offset in [-45, 45]:
        draw.ellipse([cx + x_offset - 35, head_y - 25, cx + x_offset + 35, head_y + 35], 
                    fill=panda_black)
    
    # 耳朵
    for x_offset in [-90, 90]:
        draw.ellipse([cx + x_offset - 30, head_y - 110, cx + x_offset + 30, head_y - 50], 
                    fill=panda_black, outline=(20, 20, 20), width=2)
    
    # 眼睛
    for x_offset in [-45, 45]:
        # 眼睛白
        draw.ellipse([cx + x_offset - 15, head_y - 5, cx + x_offset + 15, head_y + 20], 
                    fill=panda_white)
        # 瞳孔 (愤怒的小鸟风格)
        draw.ellipse([cx + x_offset - 8, head_y, cx + x_offset + 8, head_y + 15], 
                    fill=(0, 0, 0))
        # 愤怒眉毛
        brow_x = cx + x_offset
        draw.polygon([
            (brow_x - 20, head_y - 35), (brow_x + 20, head_y - 25), 
            (brow_x + 25, head_y - 15), (brow_x - 15, head_y - 25)
        ], fill=panda_black)
    
    # 鼻子
    draw.ellipse([cx - 15, head_y + 30, cx + 15, head_y + 50], fill=panda_black)
    
    # 嘴巴
    draw_cute_mouth(draw, cx, head_y + 60, 15, "small")
    
    # 腮红
    draw_cheeks(draw, cx, head_y + 35, 12)
    
    # 手脚
    # 手
    draw.ellipse([cx - 100, cy + 100, cx - 50, cy + 160], fill=panda_black, outline=(20, 20, 20), width=2)
    draw.ellipse([cx + 50, cy + 100, cx + 100, cy + 160], fill=panda_black, outline=(20, 20, 20), width=2)
    # 脚
    draw.ellipse([cx - 80, cy + 260, cx - 30, cy + 320], fill=panda_black, outline=(20, 20, 20), width=2)
    draw.ellipse([cx + 30, cy + 260, cx + 80, cy + 320], fill=panda_black, outline=(20, 20, 20), width=2)
    
    # 竹子 (手中)
    draw.rectangle([cx - 70, cy + 80, cx - 60, cy + 200], fill=(120, 200, 100), outline=(80, 160, 80), width=2)
    draw.polygon([(cx - 80, cy + 80), (cx - 65, cy + 60), (cx - 50, cy + 80)], fill=(140, 220, 120))
    
    return img

# ==================== 7. 湖北 - 黄鹤楼 ====================
def create_hubei():
    img = create_gradient_background(800, 1200)
    draw = ImageDraw.Draw(img)
    
    cx, cy = 400, 500
    
    # 黄鹤楼 - 多层楼阁
    floor_colors = [(200, 170, 140), (190, 160, 130), (180, 150, 120)]
    roof_colors = [(180, 60, 60), (160, 50, 50), (140, 40, 40), (120, 35, 35)]
    
    floor_heights = [0, -80, -160, -230]
    widths = [140, 110, 85, 60]
    
    # 从底层到顶层
    for i, (fh, w) in enumerate(zip(floor_heights, widths)):
        y = cy + fh
        color = floor_colors[i % len(floor_colors)]
        
        # 楼层
        draw.rectangle([cx - w, y, cx + w, y + 70], 
                      fill=color, outline=(140, 120, 100), width=2)
        
        # 栏杆
        draw.rectangle([cx - w + 10, y + 50, cx + w - 10, y + 65], 
                      fill=(160, 130, 100), outline=(130, 110, 90), width=1)
        for rx in range(int(cx - w + 20), int(cx + w - 10), 15):
            draw.line([(rx, y + 50), (rx, y + 65)], fill=(130, 110, 90), width=2)
        
        # 屋顶
        roof_w = w + 30
        roof_color = roof_colors[i % len(roof_colors)]
        draw.polygon([
            (cx - roof_w, y), (cx - w + 10, y - 30), 
            (cx, y - 45), (cx + w - 10, y - 30), (cx + roof_w, y)
        ], fill=roof_color, outline=(100, 30, 30), width=3)
        
        # 飞檐装饰
        draw.ellipse([cx - 10, y - 35, cx + 10, y - 15], fill=(200, 180, 80))
    
    # 顶层尖顶
    draw.polygon([
        (cx - 30, cy - 230), (cx, cy - 290), (cx + 30, cy - 230)
    ], fill=(180, 160, 80), outline=(140, 120, 60), width=2)
    draw.ellipse([cx - 5, cy - 300, cx + 5, cy - 290], fill=(200, 50, 50))
    
    # 黄鹤 (楼前)
    crane_x, crane_y = cx + 180, cy + 50
    crane_color = (240, 220, 180)
    # 身体
    draw.ellipse([crane_x - 20, crane_y, crane_x + 20, crane_y + 40], fill=crane_color, outline=(180, 160, 120), width=2)
    # 脖子
    draw.line([(crane_x + 15, crane_y + 10), (crane_x + 35, crane_y - 30)], fill=crane_color, width=8)
    # 头
    draw.ellipse([crane_x + 30, crane_y - 40, crane_x + 50, crane_y - 20], fill=crane_color, outline=(180, 160, 120), width=2)
    # 喙
    draw.polygon([
        (crane_x + 50, crane_y - 35), (crane_x + 70, crane_y - 30), (crane_x + 50, crane_y - 25)
    ], fill=(255, 200, 100), outline=(200, 150, 80), width=1)
    # 翅膀
    draw.polygon([
        (crane_x - 10, crane_y + 10), (crane_x - 40, crane_y - 20), 
        (crane_x - 20, crane_y + 20)
    ], fill=(220, 200, 160), outline=(180, 160, 120), width=2)
    # 腿
    draw.line([(crane_x - 5, crane_y + 40), (crane_x - 5, crane_y + 70)], fill=(200, 100, 80), width=3)
    draw.line([(crane_x + 5, crane_y + 40), (crane_x + 5, crane_y + 70)], fill=(200, 100, 80), width=3)
    
    # 脸部表情 (在主楼)
    face_y = cy - 100
    draw_angry_eyes(draw, cx, face_y, 28, 14, 55)
    draw_cute_mouth(draw, cx, face_y + 32, 18, "smile")
    draw_cheeks(draw, cx, face_y + 18, 10)
    
    # 底部云雾
    for x in [200, 400, 600]:
        draw.ellipse([x - 80, 950, x + 80, 1000], fill=(255, 255, 255, 200))
    
    return img

# ==================== 8. 福建 - 土楼 ====================
def create_fujian():
    img = create_gradient_background(800, 1200)
    draw = ImageDraw.Draw(img)
    
    cx, cy = 400, 550
    
    # 圆形土楼
    wall_color = (180, 130, 100)
    roof_color = (120, 100, 80)
    
    # 外圆
    outer_r = 180
    draw.ellipse([cx - outer_r, cy - outer_r - 50, cx + outer_r, cy + outer_r - 50], 
                fill=wall_color, outline=(140, 100, 70), width=4)
    
    # 内圆 (空心)
    inner_r = 80
    draw.ellipse([cx - inner_r, cy - inner_r - 50, cx + inner_r, cy + inner_r - 50], 
                fill=(150, 200, 230), outline=(140, 100, 70), width=3)
    
    # 楼层分隔线
    for y_offset in [-100, -50, 0, 50]:
        y = cy + y_offset - 50
        # 计算椭圆上的宽度
        w = math.sqrt(max(0, outer_r**2 - (y - cy + 50)**2))
        draw.line([(cx - w, y), (cx + w, y)], fill=(140, 100, 70), width=3)
    
    # 窗户
    for angle in range(0, 360, 30):
        rad = math.radians(angle)
        for r in [100, 130, 160]:
            wx = cx + r * math.cos(rad)
            wy = cy - 50 + (r * 0.6) * math.sin(rad)  # 压缩y轴模拟透视
            draw.rectangle([wx - 8, wy - 12, wx + 8, wy + 12], 
                          fill=(80, 60, 50), outline=(60, 40, 30), width=1)
    
    # 屋顶
    # 屋顶弧线
    draw.arc([cx - outer_r - 10, cy - outer_r - 60, cx + outer_r + 10, cy + outer_r - 40],
             start=200, end=340, fill=roof_color)
    
    # 门前广场
    draw.ellipse([cx - 60, cy + 100, cx + 60, cy + 160], fill=(180, 170, 160))
    # 门
    draw.rectangle([cx - 25, cy + 80, cx + 25, cy + 140], 
                  fill=(120, 80, 60), outline=(80, 50, 40), width=3)
    draw.arc([cx - 20, cy + 80, cx + 20, cy + 120], start=0, end=180,
             fill=(80, 50, 40))
    
    # 脸部表情 (在土楼正面)
    face_y = cy - 100
    draw_angry_eyes(draw, cx, face_y, 32, 16, 65)
    draw_cute_mouth(draw, cx, face_y + 40, 22, "smile")
    draw_cheeks(draw, cx, face_y + 25, 13)
    
    # 周围的土楼 (小)
    for x_offset in [-280, 280]:
        sx = cx + x_offset
        sr = 60
        draw.ellipse([sx - sr, cy + 50 - sr, sx + sr, cy + 50 + sr], 
                    fill=(160, 120, 90), outline=(130, 90, 60), width=2)
        draw.ellipse([sx - 30, cy + 50 - 30, sx + 30, cy + 50 + 30], 
                    fill=(150, 200, 230), outline=(130, 90, 60), width=2)
    
    # 地面
    draw.rectangle([0, cy + 150, 800, 1200], fill=(140, 180, 140))
    # 草地纹理
    for _ in range(30):
        import random
        x = random.randint(50, 750)
        y = random.randint(int(cy + 180), 1150)
        draw.line([(x, y), (x + 10, y - 15)], fill=(100, 160, 100), width=2)
    
    return img

# ==================== 9. 湖南 - 张家界 ====================
def create_hunan():
    img = create_gradient_background(800, 1200)
    draw = ImageDraw.Draw(img)
    
    cx, cy = 400, 500
    
    # 张家界石柱山峰
    rock_color = (160, 150, 140)
    rock_highlight = (190, 180, 170)
    rock_shadow = (120, 110, 100)
    
    # 主峰 (哈利路亚山风格)
    # 左柱
    points_left = [
        (cx - 80, cy + 250), (cx - 60, cy + 100), (cx - 70, cy - 50),
        (cx - 50, cy - 150), (cx - 40, cy - 180), (cx - 30, cy - 150),
        (cx - 20, cy + 100), (cx - 10, cy + 250)
    ]
    draw.polygon(points_left, fill=rock_color, outline=(100, 90, 80), width=3)
    # 高光
    draw.polygon([
        (cx - 70, cy + 200), (cx - 60, cy + 100), (cx - 65, cy - 30),
        (cx - 55, cy - 120), (cx - 50, cy - 150), (cx - 45, cy - 120),
        (cx - 40, cy + 100), (cx - 35, cy + 200)
    ], fill=rock_highlight)
    
    # 中柱 (最高)
    points_center = [
        (cx - 20, cy + 250), (cx - 10, cy + 150), (cx, cy), 
        (cx + 10, cy - 200), (cx + 25, cy - 280), (cx + 40, cy - 200),
        (cx + 50, cy), (cx + 60, cy + 150), (cx + 70, cy + 250)
    ]
    draw.polygon(points_center, fill=rock_color, outline=(100, 90, 80), width=3)
    # 高光
    draw.polygon([
        (cx - 5, cy + 200), (cx, cy + 100), (cx + 5, cy),
        (cx + 15, cy - 180), (cx + 25, cy - 260), (cx + 30, cy - 180),
        (cx + 35, cy), (cx + 45, cy + 150), (cx + 50, cy + 200)
    ], fill=rock_highlight)
    
    # 右柱
    points_right = [
        (cx + 60, cy + 250), (cx + 70, cy + 120), (cx + 80, cy - 30),
        (cx + 90, cy - 120), (cx + 100, cy - 150), (cx + 110, cy - 120),
        (cx + 120, cy + 80), (cx + 130, cy + 250)
    ]
    draw.polygon(points_right, fill=rock_shadow, outline=(100, 90, 80), width=3)
    
    # 山顶植被
    for x_offset, y_offset in [(-45, -165), (25, -270), (105, -135)]:
        draw.ellipse([cx + x_offset - 30, cy + y_offset - 15, 
                     cx + x_offset + 30, cy + y_offset + 15], fill=(80, 140, 60))
    
    # 岩层纹理
    for y in range(cy - 200, cy + 250, 40):
        for x_start in [cx - 75, cx - 15, cx + 65]:
            w = 50 if x_start == cx - 15 else 60
            draw.line([(x_start, y), (x_start + w, y)], fill=(130, 120, 110), width=2)
    
    # 脸部表情 (在中柱)
    face_y = cy - 80
    draw_angry_eyes(draw, cx + 25, face_y, 30, 15, 60)
    draw_cute_mouth(draw, cx + 25, face_y + 35, 20, "smile")
    draw_cheeks(draw, cx + 25, face_y + 20, 12)
    
    # 底部云雾
    for i in range(5):
        x = 100 + i * 150
        y = cy + 180 + (i % 2) * 30
        draw.ellipse([x - 60, y, x + 60, y + 40], fill=(255, 255, 255, 200))
    
    # 底部森林
    for x in range(50, 751, 40):
        tree_h = 30 + (x % 3) * 20
        draw.polygon([
            (x, cy + 320), (x - 15, cy + 320 - tree_h), (x + 15, cy + 320 - tree_h)
        ], fill=(60, 120, 50), outline=(40, 90, 30), width=1)
    
    return img

# ==================== 10. 上海 - 外滩 ====================
def create_shanghai():
    img = create_gradient_background(800, 1200)
    draw = ImageDraw.Draw(img)
    
    cx, cy = 400, 500
    
    # 外滩建筑群
    # 东方明珠塔
    pearl_x = cx + 150
    # 下球体
    draw.ellipse([pearl_x - 50, cy + 100, pearl_x + 50, cy + 200], 
                fill=(200, 60, 80), outline=(150, 40, 60), width=3)
    # 中柱
    draw.rectangle([pearl_x - 8, cy - 50, pearl_x + 8, cy + 150], 
                  fill=(180, 180, 180), outline=(140, 140, 140), width=2)
    # 上球体
    draw.ellipse([pearl_x - 35, cy - 100, pearl_x + 35, cy - 30], 
                fill=(200, 60, 80), outline=(150, 40, 60), width=3)
    # 顶部
    draw.ellipse([pearl_x - 15, cy - 140, pearl_x + 15, cy - 100], 
                fill=(200, 60, 80), outline=(150, 40, 60), width=2)
    # 天线
    draw.line([(pearl_x, cy - 140), (pearl_x, cy - 200)], fill=(150, 150, 150), width=4)
    
    # 其他建筑
    buildings = [
        (cx - 200, 120, 250, (180, 160, 140)),  # 古典风格
        (cx - 80, 80, 200, (160, 180, 200)),   # 现代风格
        (cx + 20, 100, 220, (200, 190, 170)),  # 欧式风格
    ]
    
    for bx, bw, bh, color in buildings:
        draw.rectangle([bx - bw//2, cy + 250 - bh, bx + bw//2, cy + 250], 
                      fill=color, outline=(120, 120, 120), width=2)
        # 窗户
        for wx in range(bx - bw//2 + 10, bx + bw//2 - 5, 15):
            for wy in range(cy + 250 - bh + 20, cy + 250 - 10, 25):
                draw.rectangle([wx, wy, wx + 8, wy + 15], fill=(100, 120, 140), outline=(80, 100, 120), width=1)
        # 屋顶
        draw.polygon([
            (bx - bw//2 - 10, cy + 250 - bh), (bx, cy + 250 - bh - 30), (bx + bw//2 + 10, cy + 250 - bh)
        ], fill=(160, 60, 60), outline=(120, 40, 40), width=2)
    
    # 上海中心大厦 (细长)
    center_x = cx - 100
    draw.polygon([
        (center_x - 25, cy + 250), (center_x - 15, cy - 100),
        (center_x, cy - 180), (center_x + 15, cy - 100), (center_x + 25, cy + 250)
    ], fill=(100, 200, 220), outline=(70, 150, 170), width=3)
    # 螺旋纹理
    for y in range(cy - 150, cy + 250, 20):
        offset = ((y - cy) // 20) * 3
        draw.line([(center_x - 15 + offset, y), (center_x + 15 - offset, y)], 
                 fill=(120, 220, 240), width=2)
    
    # 黄浦江
    water_color = (80, 140, 180)
    draw.rectangle([0, cy + 250, 800, 1200], fill=water_color)
    # 波纹
    for y in range(cy + 280, 1200, 50):
        for x in range(0, 801, 200):
            draw.arc([x, y, x + 100, y + 30], start=0, end=180, fill=(100, 170, 210))
    
    # 脸部表情 (在东方明珠上)
    face_y = cy + 150
    draw_angry_eyes(draw, pearl_x, face_y, 28, 14, 55)
    draw_cute_mouth(draw, pearl_x, face_y + 32, 18, "smile")
    draw_cheeks(draw, pearl_x, face_y + 18, 10)
    
    # 船只
    for i, (sx, sy) in enumerate([(200, cy + 350), (600, cy + 400)]):
        boat_color = (200, 180, 160)
        draw.polygon([
            (sx - 40, sy), (sx + 40, sy), (sx + 50, sy - 30), (sx - 50, sy - 30)
        ], fill=boat_color, outline=(160, 140, 120), width=2)
        # 船舱
        draw.rectangle([sx - 20, sy - 50, sx + 20, sy - 30], fill=(180, 160, 140), outline=(140, 120, 100), width=2)
    
    return img

# ==================== 主函数 ====================
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    towers = [
        ("guangdong-canton-tower.png", create_guangdong, "广东 - 广州塔"),
        ("jiangsu-garden.png", create_jiangsu, "江苏 - 苏州园林"),
        ("shandong-taishan.png", create_shandong, "山东 - 泰山"),
        ("zhejiang-xihu.png", create_zhejiang, "浙江 - 西湖"),
        ("henan-shaolin.png", create_henan, "河南 - 少林寺"),
        ("sichuan-panda.png", create_sichuan, "四川 - 大熊猫"),
        ("hubei-yellow-crane.png", create_hubei, "湖北 - 黄鹤楼"),
        ("fujian-tulou.png", create_fujian, "福建 - 土楼"),
        ("hunan-zhangjiajie.png", create_hunan, "湖南 - 张家界"),
        ("shanghai-bund.png", create_shanghai, "上海 - 外滩"),
    ]
    
    for filename, func, name in towers:
        print(f"生成: {name}...")
        img = func()
        filepath = os.path.join(OUTPUT_DIR, filename)
        img.save(filepath, "PNG")
        print(f"  已保存: {filepath}")
    
    print(f"\n✅ 全部完成！共生成 {len(towers)} 张图片")
    print(f"保存位置: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
