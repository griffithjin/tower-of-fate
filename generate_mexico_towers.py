#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
墨西哥州卡通塔生成器 - 愤怒的小鸟风格
"""

from PIL import Image, ImageDraw, ImageFilter
import os
import math

# 输出目录
OUTPUT_DIR = "/Users/moutai/Desktop/toweroffate_v1.0/assets/towers/states/mexico"

# 图片尺寸
WIDTH, HEIGHT = 800, 1200

# 颜色定义 - 愤怒的小鸟风格（明亮、饱和）
COLORS = {
    'sky_top': (135, 206, 235),      # 天蓝色顶部
    'sky_bottom': (176, 224, 230),   # 天蓝色底部
    'skin': (255, 220, 180),         # 肤色
    'red': (255, 80, 60),            # 愤怒红
    'yellow': (255, 220, 50),        # 明亮黄
    'green': (100, 200, 80),         # 草绿
    'blue': (70, 150, 220),          # 天空蓝
    'brown': (160, 100, 60),         # 棕色
    'dark_brown': (120, 70, 40),     # 深棕色
    'white': (255, 255, 255),        # 白色
    'black': (40, 40, 40),           # 黑色
    'orange': (255, 150, 50),        # 橙色
    'pink': (255, 150, 180),         # 粉色
    'purple': (180, 100, 200),       # 紫色
    'sand': (230, 200, 150),         # 沙色
    'copper': (184, 115, 51),        # 铜色
    'gold': (255, 215, 0),           # 金色
    'gray': (150, 150, 150),         # 灰色
    'stone': (160, 160, 160),        # 石灰色
}

def create_gradient_background(width, height, color_top, color_bottom):
    """创建天蓝色渐变背景"""
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    
    for y in range(height):
        ratio = y / height
        r = int(color_top[0] * (1 - ratio) + color_bottom[0] * ratio)
        g = int(color_top[1] * (1 - ratio) + color_bottom[1] * ratio)
        b = int(color_top[2] * (1 - ratio) + color_bottom[2] * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    return img

def draw_angry_eyes(draw, cx, cy, size=30, expression='angry'):
    """绘制愤怒的小鸟风格眼睛"""
    eye_offset = size * 0.6
    eye_size = size * 0.35
    
    # 白眼珠
    draw.ellipse([cx - eye_offset - eye_size, cy - eye_size, 
                  cx - eye_offset + eye_size, cy + eye_size], 
                 fill=COLORS['white'], outline=COLORS['black'], width=2)
    draw.ellipse([cx + eye_offset - eye_size, cy - eye_size, 
                  cx + eye_offset + eye_size, cy + eye_size], 
                 fill=COLORS['white'], outline=COLORS['black'], width=2)
    
    # 黑眼珠（稍微向内看，显得愤怒）
    pupil_offset = eye_size * 0.3
    pupil_size = eye_size * 0.5
    draw.ellipse([cx - eye_offset + pupil_offset - pupil_size, cy - pupil_size, 
                  cx - eye_offset + pupil_size, cy + pupil_size], 
                 fill=COLORS['black'])
    draw.ellipse([cx + eye_offset - pupil_offset - pupil_size, cy - pupil_size, 
                  cx + eye_offset - pupil_size, cy + pupil_size], 
                 fill=COLORS['black'])
    
    # 愤怒眉毛
    brow_y = cy - eye_size - 10
    draw.polygon([
        (cx - eye_offset - eye_size - 5, brow_y + 15),
        (cx - eye_offset + 5, brow_y - 5),
        (cx - eye_offset + eye_size + 10, brow_y - 5),
        (cx - eye_offset + eye_size + 5, brow_y + 10),
    ], fill=COLORS['black'])
    
    draw.polygon([
        (cx + eye_offset - eye_size - 10, brow_y - 5),
        (cx + eye_offset - 5, brow_y - 5),
        (cx + eye_offset + eye_size + 5, brow_y + 15),
        (cx + eye_offset + eye_size - 5, brow_y + 10),
    ], fill=COLORS['black'])

def draw_cute_beak(draw, cx, cy, size=25):
    """绘制可爱鸟嘴"""
    beak_points = [
        (cx - size, cy),
        (cx, cy + size * 0.8),
        (cx + size, cy),
        (cx, cy - size * 0.3),
    ]
    draw.polygon(beak_points, fill=COLORS['orange'], outline=COLORS['black'], width=2)

def draw_cute_mouth(draw, cx, cy, size=20, smile=True):
    """绘制可爱嘴巴"""
    if smile:
        # 微笑
        draw.arc([cx - size, cy - size//2, cx + size, cy + size], 
                 start=0, end=180, fill=COLORS['black'], width=3)
    else:
        # 圆形小嘴
        draw.ellipse([cx - size//2, cy - size//3, cx + size//2, cy + size//3], 
                     fill=COLORS['pink'], outline=COLORS['black'], width=2)

def draw_clouds(img_draw, width, height):
    """绘制背景云朵"""
    cloud_positions = [
        (150, 150, 80),
        (600, 200, 100),
        (450, 100, 60),
        (700, 350, 70),
        (100, 400, 65),
    ]
    
    for cx, cy, size in cloud_positions:
        # 云朵由多个圆组成
        circles = [
            (cx - size//2, cy),
            (cx + size//2, cy),
            (cx, cy - size//3),
            (cx - size//3, cy + size//4),
            (cx + size//3, cy + size//4),
        ]
        for x, y in circles:
            img_draw.ellipse([x - size//2, y - size//2, x + size//2, y + size//2], 
                             fill=(255, 255, 255, 180))

def draw_base_platform(draw, cx, cy, width, height):
    """绘制塔底座平台"""
    # 主平台
    draw.ellipse([cx - width//2, cy - height//3, cx + width//2, cy + height//3], 
                 fill=COLORS['green'], outline=COLORS['black'], width=3)
    # 草地纹理
    for i in range(5):
        x = cx - width//3 + i * (width//6)
        draw.polygon([
            (x, cy - height//4),
            (x + 15, cy - height//4 - 20),
            (x + 30, cy - height//4),
        ], fill=COLORS['green'], outline=COLORS['black'], width=1)

# ==================== 1. 墨西哥城 - 宪法广场 ====================
def create_mexico_city_zocalo():
    """墨西哥城宪法广场塔 - 墨西哥国旗风格"""
    img = create_gradient_background(WIDTH, HEIGHT, COLORS['sky_top'], COLORS['sky_bottom'])
    draw = ImageDraw.Draw(img)
    
    cx, cy = WIDTH // 2, HEIGHT - 250
    
    # 底座
    draw_base_platform(draw, cx, cy + 100, 400, 100)
    
    # 塔身 - 圆柱形，墨西哥国旗绿白红三色
    tower_width = 250
    tower_height = 500
    base_y = cy + 50
    
    # 绿色条纹
    draw.polygon([
        (cx - tower_width//2, base_y),
        (cx - tower_width//3, base_y - tower_height),
        (cx - tower_width//3 + 20, base_y - tower_height),
        (cx - tower_width//2 + 30, base_y),
    ], fill=COLORS['green'], outline=COLORS['black'], width=3)
    
    # 白色条纹（中间带脸）
    draw.polygon([
        (cx - tower_width//3, base_y),
        (cx - tower_width//3, base_y - tower_height),
        (cx + tower_width//3, base_y - tower_height),
        (cx + tower_width//3, base_y),
    ], fill=COLORS['white'], outline=COLORS['black'], width=3)
    
    # 红色条纹
    draw.polygon([
        (cx + tower_width//3, base_y),
        (cx + tower_width//3, base_y - tower_height),
        (cx + tower_width//2, base_y - tower_height),
        (cx + tower_width//2 - 30, base_y),
    ], fill=COLORS['red'], outline=COLORS['black'], width=3)
    
    # 顶部圆顶
    draw.ellipse([cx - tower_width//3 - 10, base_y - tower_height - 60, 
                  cx + tower_width//3 + 10, base_y - tower_height + 20], 
                 fill=COLORS['red'], outline=COLORS['black'], width=3)
    
    # 脸部 - 在白色区域
    face_y = base_y - tower_height // 2
    draw_angry_eyes(draw, cx, face_y - 30, size=40)
    draw_cute_beak(draw, cx, face_y + 10, size=30)
    
    # 墨西哥徽章（简化）
    emblem_y = base_y - tower_height - 30
    draw.ellipse([cx - 25, emblem_y - 25, cx + 25, emblem_y + 25], 
                 fill=COLORS['gold'], outline=COLORS['black'], width=2)
    
    return img

# ==================== 2. 哈利斯科 - 龙舌兰 ====================
def create_jalisco_tequila():
    """哈利斯科龙舌兰塔 - 龙舌兰植物风格"""
    img = create_gradient_background(WIDTH, HEIGHT, COLORS['sky_top'], COLORS['sky_bottom'])
    draw = ImageDraw.Draw(img)
    
    cx, cy = WIDTH // 2, HEIGHT - 250
    
    # 底座
    draw_base_platform(draw, cx, cy + 100, 380, 90)
    
    # 龙舌兰植物形状塔身
    base_y = cy + 50
    
    # 叶片形状 - 多层
    leaf_colors = [COLORS['green'], (80, 180, 60), (60, 160, 40)]
    
    for layer in range(3):
        offset = layer * 30
        color = leaf_colors[layer % len(leaf_colors)]
        
        # 左叶片
        points_left = [
            (cx - 20 - offset, base_y - 100 - offset * 3),
            (cx - 80 - offset, base_y - 50),
            (cx - 60 - offset, base_y + 20),
            (cx - 10, base_y),
        ]
        draw.polygon(points_left, fill=color, outline=COLORS['black'], width=3)
        
        # 右叶片
        points_right = [
            (cx + 20 + offset, base_y - 100 - offset * 3),
            (cx + 80 + offset, base_y - 50),
            (cx + 60 + offset, base_y + 20),
            (cx + 10, base_y),
        ]
        draw.polygon(points_right, fill=color, outline=COLORS['black'], width=3)
        
        # 中心叶片
        points_center = [
            (cx, base_y - 150 - offset * 4),
            (cx - 40, base_y - 80 - offset * 2),
            (cx, base_y + 10),
            (cx + 40, base_y - 80 - offset * 2),
        ]
        draw.polygon(points_center, fill=color, outline=COLORS['black'], width=3)
    
    # 脸部 - 中心区域
    face_y = base_y - 200
    draw_angry_eyes(draw, cx, face_y, size=35)
    draw_cute_beak(draw, cx, face_y + 35, size=25)
    
    # 龙舌兰花（顶部）
    flower_y = base_y - 350
    for angle in range(0, 360, 45):
        rad = math.radians(angle)
        px = cx + int(40 * math.cos(rad))
        py = flower_y + int(40 * math.sin(rad))
        draw.ellipse([px - 20, py - 20, px + 20, py + 20], 
                     fill=COLORS['yellow'], outline=COLORS['black'], width=2)
    draw.ellipse([cx - 25, flower_y - 25, cx + 25, flower_y + 25], 
                 fill=COLORS['orange'], outline=COLORS['black'], width=2)
    
    return img

# ==================== 3. 韦拉克鲁斯 - 港口 ====================
def create_veracruz_port():
    """韦拉克鲁斯港口塔 - 灯塔风格"""
    img = create_gradient_background(WIDTH, HEIGHT, COLORS['sky_top'], COLORS['sky_bottom'])
    draw = ImageDraw.Draw(img)
    
    cx, cy = WIDTH // 2, HEIGHT - 250
    
    # 底座（港口平台）
    draw.rectangle([cx - 180, cy + 50, cx + 180, cy + 100], 
                   fill=COLORS['gray'], outline=COLORS['black'], width=3)
    
    # 灯塔塔身 - 红白条纹
    tower_base = cy + 50
    tower_height = 450
    sections = 5
    section_height = tower_height // sections
    
    for i in range(sections):
        y1 = tower_base - i * section_height
        y2 = tower_base - (i + 1) * section_height
        color = COLORS['white'] if i % 2 == 0 else COLORS['red']
        width = 120 - i * 8
        
        draw.polygon([
            (cx - width//2, y1),
            (cx - width//2 + 10, y2),
            (cx + width//2 - 10, y2),
            (cx + width//2, y1),
        ], fill=color, outline=COLORS['black'], width=3)
    
    # 灯塔顶部
    top_y = tower_base - tower_height
    draw.polygon([
        (cx - 50, top_y),
        (cx, top_y - 60),
        (cx + 50, top_y),
    ], fill=COLORS['red'], outline=COLORS['black'], width=3)
    
    # 灯室
    draw.rectangle([cx - 35, top_y - 30, cx + 35, top_y + 20], 
                   fill=COLORS['yellow'], outline=COLORS['black'], width=3)
    # 光束
    draw.polygon([
        (cx, top_y - 5),
        (cx - 200, top_y - 100),
        (cx - 150, top_y - 20),
    ], fill=(255, 255, 200, 100))
    draw.polygon([
        (cx, top_y - 5),
        (cx + 200, top_y - 100),
        (cx + 150, top_y - 20),
    ], fill=(255, 255, 200, 100))
    
    # 脸部 - 中间位置
    face_y = tower_base - tower_height // 2
    draw_angry_eyes(draw, cx, face_y, size=38)
    draw_cute_beak(draw, cx, face_y + 35, size=28)
    
    # 波浪装饰
    for i in range(5):
        wx = cx - 150 + i * 75
        draw.arc([wx, cy + 100, wx + 50, cy + 140], start=0, end=180, 
                 fill=COLORS['blue'], width=4)
    
    return img

# ==================== 4. 普埃布拉 - 金字塔 ====================
def create_puebla_pyramid():
    """普埃布拉金字塔塔 - 乔鲁拉大金字塔风格"""
    img = create_gradient_background(WIDTH, HEIGHT, COLORS['sky_top'], COLORS['sky_bottom'])
    draw = ImageDraw.Draw(img)
    
    cx, cy = WIDTH // 2, HEIGHT - 200
    
    # 底座（大金字塔基座）
    base_width = 400
    base_height = 150
    
    # 金字塔阶梯（3层）
    layers = [
        (400, 150, COLORS['sand']),
        (300, 120, (210, 180, 130)),
        (200, 100, COLORS['sand']),
    ]
    
    current_y = cy + 50
    for width, height, color in layers:
        # 左侧面
        draw.polygon([
            (cx - width//2, current_y),
            (cx, current_y - height//2),
            (cx, current_y - height),
            (cx - width//3, current_y - height),
        ], fill=color, outline=COLORS['black'], width=3)
        
        # 正面
        draw.polygon([
            (cx - width//2, current_y),
            (cx + width//2, current_y),
            (cx + width//3, current_y - height),
            (cx - width//3, current_y - height),
        ], fill=color, outline=COLORS['black'], width=3)
        
        # 右侧面
        draw.polygon([
            (cx + width//2, current_y),
            (cx + width//3, current_y - height),
            (cx, current_y - height),
            (cx, current_y - height//2),
        ], fill=(color[0] - 20, color[1] - 15, color[2] - 20), 
                  outline=COLORS['black'], width=3)
        
        current_y -= height
    
    # 顶部神庙
    temple_y = current_y
    draw.polygon([
        (cx - 60, temple_y),
        (cx + 60, temple_y),
        (cx + 50, temple_y - 80),
        (cx - 50, temple_y - 80),
    ], fill=COLORS['brown'], outline=COLORS['black'], width=3)
    
    # 神庙屋顶
    draw.polygon([
        (cx - 70, temple_y - 80),
        (cx + 70, temple_y - 80),
        (cx, temple_y - 140),
    ], fill=COLORS['red'], outline=COLORS['black'], width=3)
    
    # 脸部 - 在金字塔中部
    face_y = cy - 50
    draw_angry_eyes(draw, cx, face_y, size=42)
    draw_cute_beak(draw, cx, face_y + 40, size=32)
    
    # 顶部装饰
    draw.ellipse([cx - 15, temple_y - 170, cx + 15, temple_y - 140], 
                 fill=COLORS['gold'], outline=COLORS['black'], width=2)
    
    return img

# ==================== 5. 瓜纳华托 - 彩色小镇 ====================
def create_guanajuato_colorful():
    """瓜纳华托彩色小镇塔 - 彩色房屋风格"""
    img = create_gradient_background(WIDTH, HEIGHT, COLORS['sky_top'], COLORS['sky_bottom'])
    draw = ImageDraw.Draw(img)
    
    cx, cy = WIDTH // 2, HEIGHT - 220
    
    # 山坡底座
    draw.polygon([
        (cx - 250, cy + 100),
        (cx + 250, cy + 100),
        (cx + 200, cy - 50),
        (cx - 200, cy - 50),
    ], fill=COLORS['green'], outline=COLORS['black'], width=3)
    
    # 彩色房屋堆叠
    houses = [
        # (x_offset, y_offset, width, height, color)
        (0, -100, 120, 100, COLORS['red']),
        (-80, -80, 90, 80, COLORS['blue']),
        (80, -90, 100, 90, COLORS['yellow']),
        (-40, -180, 110, 80, COLORS['orange']),
        (50, -170, 95, 70, COLORS['purple']),
        (0, -260, 130, 80, COLORS['pink']),
    ]
    
    for hx, hy, hw, hh, color in houses:
        x = cx + hx
        y = cy + hy
        # 房屋主体
        draw.rectangle([x - hw//2, y - hh, x + hw//2, y], 
                       fill=color, outline=COLORS['black'], width=3)
        # 屋顶
        draw.polygon([
            (x - hw//2 - 10, y - hh),
            (x + hw//2 + 10, y - hh),
            (x, y - hh - 25),
        ], fill=COLORS['brown'], outline=COLORS['black'], width=2)
        # 窗户
        draw.rectangle([x - hw//4, y - hh//1.5, x - hw//8, y - hh//2], 
                       fill=COLORS['white'], outline=COLORS['black'], width=1)
        draw.rectangle([x + hw//8, y - hh//1.5, x + hw//4, y - hh//2], 
                       fill=COLORS['white'], outline=COLORS['black'], width=1)
    
    # 脸部 - 在主房屋上
    face_y = cy - 220
    draw_angry_eyes(draw, cx, face_y, size=35)
    draw_cute_beak(draw, cx, face_y + 30, size=25)
    
    # 顶部教堂尖塔
    steeple_y = cy - 340
    draw.rectangle([cx - 20, steeple_y, cx + 20, steeple_y + 80], 
                   fill=COLORS['white'], outline=COLORS['black'], width=3)
    draw.polygon([
        (cx - 25, steeple_y),
        (cx + 25, steeple_y),
        (cx, steeple_y - 40),
    ], fill=COLORS['red'], outline=COLORS['black'], width=2)
    
    return img

# ==================== 6. 新莱昂 - Monterrey山 ====================
def create_nuevo_leon_monterrey():
    """新莱昂Monterrey山塔 - 山脉风格"""
    img = create_gradient_background(WIDTH, HEIGHT, COLORS['sky_top'], COLORS['sky_bottom'])
    draw = ImageDraw.Draw(img)
    
    cx, cy = WIDTH // 2, HEIGHT - 200
    
    # 远山（背景）
    draw.polygon([
        (0, cy),
        (200, cy - 200),
        (400, cy - 150),
        (600, cy - 250),
        (WIDTH, cy - 100),
        (WIDTH, cy),
    ], fill=(180, 180, 200), outline=COLORS['black'], width=2)
    
    # 主峰（Cerro de la Silla风格）
    draw.polygon([
        (cx - 200, cy + 50),
        (cx - 100, cy - 300),
        (cx, cy - 200),
        (cx + 80, cy - 350),
        (cx + 180, cy - 100),
        (cx + 220, cy + 50),
    ], fill=COLORS['stone'], outline=COLORS['black'], width=3)
    
    # 山顶积雪
    draw.polygon([
        (cx - 80, cy - 270),
        (cx - 100, cy - 300),
        (cx - 60, cy - 240),
        (cx, cy - 200),
        (cx + 30, cy - 230),
        (cx + 60, cy - 320),
        (cx + 80, cy - 350),
        (cx + 50, cy - 290),
    ], fill=COLORS['white'], outline=COLORS['black'], width=2)
    
    # 脸部 - 在山体中央
    face_y = cy - 150
    draw_angry_eyes(draw, cx, face_y, size=40)
    draw_cute_beak(draw, cx, face_y + 35, size=30)
    
    # 岩石纹理
    for i in range(8):
        rx = cx - 150 + i * 40
        ry = cy - 50 - i * 20
        draw.ellipse([rx, ry, rx + 30, ry + 20], 
                     fill=(140, 140, 140), outline=COLORS['black'], width=1)
    
    return img

# ==================== 7. 奇瓦瓦 - 铜峡谷 ====================
def create_chihuahua_copper_canyon():
    """奇瓦瓦铜峡谷塔 - 红色峡谷风格"""
    img = create_gradient_background(WIDTH, HEIGHT, COLORS['sky_top'], COLORS['sky_bottom'])
    draw = ImageDraw.Draw(img)
    
    cx, cy = WIDTH // 2, HEIGHT - 200
    
    # 峡谷层次（铜红色系）
    canyon_colors = [
        (200, 120, 80),
        (180, 100, 60),
        COLORS['copper'],
        (140, 80, 40),
    ]
    
    # 多层峡谷
    for i, color in enumerate(canyon_colors):
        offset = i * 40
        y_pos = cy - i * 50
        
        # 左峡谷壁
        draw.polygon([
            (0, HEIGHT),
            (0, y_pos),
            (cx - 100 - offset, y_pos - 50),
            (cx - 50 - offset, cy + 100),
        ], fill=color, outline=COLORS['black'], width=2)
        
        # 右峡谷壁
        draw.polygon([
            (WIDTH, HEIGHT),
            (WIDTH, y_pos),
            (cx + 100 + offset, y_pos - 50),
            (cx + 50 + offset, cy + 100),
        ], fill=color, outline=COLORS['black'], width=2)
    
    # 中央塔（突出的岩石柱）
    draw.polygon([
        (cx - 80, cy + 100),
        (cx - 50, cy - 250),
        (cx, cy - 350),
        (cx + 50, cy - 250),
        (cx + 80, cy + 100),
    ], fill=(160, 90, 50), outline=COLORS['black'], width=3)
    
    # 顶部平台
    draw.polygon([
        (cx - 50, cy - 250),
        (cx + 50, cy - 250),
        (cx + 30, cy - 280),
        (cx - 30, cy - 280),
    ], fill=(180, 110, 60), outline=COLORS['black'], width=2)
    
    # 脸部
    face_y = cy - 150
    draw_angry_eyes(draw, cx, face_y, size=38)
    draw_cute_beak(draw, cx, face_y + 35, size=28)
    
    # 仙人掌装饰
    cactus_x = cx - 200
    draw.rectangle([cactus_x, cy - 50, cactus_x + 20, cy + 50], 
                   fill=COLORS['green'], outline=COLORS['black'], width=2)
    draw.rectangle([cactus_x - 20, cy - 20, cactus_x, cy], 
                   fill=COLORS['green'], outline=COLORS['black'], width=2)
    draw.rectangle([cactus_x + 20, cy - 10, cactus_x + 40, cy + 20], 
                   fill=COLORS['green'], outline=COLORS['black'], width=2)
    
    return img

# ==================== 8. 下加利福尼亚 - 葡萄酒庄 ====================
def create_baja_wine():
    """下加利福尼亚葡萄酒庄塔 - 葡萄和酒桶风格"""
    img = create_gradient_background(WIDTH, HEIGHT, COLORS['sky_top'], COLORS['sky_bottom'])
    draw = ImageDraw.Draw(img)
    
    cx, cy = WIDTH // 2, HEIGHT - 220
    
    # 葡萄园底座
    for row in range(4):
        y = cy + 80 - row * 25
        for col in range(8):
            x = cx - 200 + col * 55
            draw.ellipse([x, y, x + 40, y + 30], 
                         fill=COLORS['green'], outline=COLORS['black'], width=1)
    
    # 主塔身（酒桶形状）
    barrel_width = 200
    barrel_height = 350
    barrel_top = cy - 100
    
    # 酒桶主体
    draw.polygon([
        (cx - barrel_width//3, cy + 50),
        (cx - barrel_width//2, barrel_top + 50),
        (cx - barrel_width//2, barrel_top),
        (cx + barrel_width//2, barrel_top),
        (cx + barrel_width//2, barrel_top + 50),
        (cx + barrel_width//3, cy + 50),
    ], fill=(180, 120, 70), outline=COLORS['black'], width=3)
    
    # 酒桶箍
    for y in [barrel_top + 30, barrel_top + 120, barrel_top + 210, cy]:
        draw.line([(cx - barrel_width//2 + 5, y), (cx + barrel_width//2 - 5, y)], 
                  fill=(140, 90, 50), width=8)
    
    # 脸部
    face_y = barrel_top + 150
    draw_angry_eyes(draw, cx, face_y, size=40)
    draw_cute_beak(draw, cx, face_y + 40, size=30)
    
    # 葡萄串装饰
    grape_positions = [
        (cx - 120, barrel_top + 80),
        (cx + 120, barrel_top + 100),
        (cx - 100, barrel_top + 200),
    ]
    
    for gx, gy in grape_positions:
        # 葡萄串由多个小圆组成
        grape_color = (120, 50, 150)
        for i in range(4):
            for j in range(3 - i):
                draw.ellipse([gx + j*20 + i*10, gy + i*20, 
                             gx + j*20 + i*10 + 18, gy + i*20 + 18], 
                            fill=grape_color, outline=COLORS['black'], width=1)
    
    # 顶部酒杯/酒塞装饰
    draw.rectangle([cx - 30, barrel_top - 40, cx + 30, barrel_top], 
                   fill=(140, 90, 50), outline=COLORS['black'], width=2)
    draw.ellipse([cx - 35, barrel_top - 50, cx + 35, barrel_top - 30], 
                 fill=(160, 100, 60), outline=COLORS['black'], width=2)
    
    return img

# ==================== 9. 索诺拉 - 沙漠 ====================
def create_sonora_desert():
    """索诺拉沙漠塔 - 仙人掌风格"""
    img = create_gradient_background(WIDTH, HEIGHT, COLORS['sky_top'], COLORS['sky_bottom'])
    draw = ImageDraw.Draw(img)
    
    cx, cy = WIDTH // 2, HEIGHT - 220
    
    # 沙丘背景
    draw.polygon([
        (0, HEIGHT),
        (0, cy - 50),
        (200, cy - 150),
        (400, cy - 80),
        (600, cy - 180),
        (WIDTH, cy - 100),
        (WIDTH, HEIGHT),
    ], fill=COLORS['sand'], outline=COLORS['black'], width=2)
    
    # 巨型仙人掌主体
    cactus_color = (80, 160, 60)
    
    # 主干
    trunk_width = 100
    trunk_height = 400
    trunk_top = cy - 150
    
    draw.rounded_rectangle([cx - trunk_width//2, trunk_top, 
                           cx + trunk_width//2, cy + 50], 
                          radius=40, fill=cactus_color, outline=COLORS['black'], width=3)
    
    # 左臂
    draw.rounded_rectangle([cx - 140, trunk_top + 80, 
                           cx - trunk_width//2, trunk_top + 150], 
                          radius=25, fill=cactus_color, outline=COLORS['black'], width=3)
    draw.rounded_rectangle([cx - 140, trunk_top + 20, 
                           cx - 100, trunk_top + 100], 
                          radius=20, fill=cactus_color, outline=COLORS['black'], width=3)
    
    # 右臂
    draw.rounded_rectangle([cx + trunk_width//2, trunk_top + 100, 
                           cx + 140, trunk_top + 170], 
                          radius=25, fill=cactus_color, outline=COLORS['black'], width=3)
    draw.rounded_rectangle([cx + 100, trunk_top + 40, 
                           cx + 140, trunk_top + 120], 
                          radius=20, fill=cactus_color, outline=COLORS['black'], width=3)
    
    # 仙人掌刺
    for i in range(10):
        y = trunk_top + 40 + i * 35
        draw.line([(cx - trunk_width//2 + 10, y), (cx - trunk_width//2 - 10, y)], 
                  fill=(200, 200, 180), width=2)
        draw.line([(cx + trunk_width//2 - 10, y), (cx + trunk_width//2 + 10, y)], 
                  fill=(200, 200, 180), width=2)
    
    # 脸部
    face_y = trunk_top + 150
    draw_angry_eyes(draw, cx, face_y, size=35)
    draw_cute_beak(draw, cx, face_y + 35, size=25)
    
    # 顶部花朵
    flower_y = trunk_top - 20
    for angle in range(0, 360, 60):
        rad = math.radians(angle)
        px = cx + int(25 * math.cos(rad))
        py = flower_y + int(25 * math.sin(rad))
        draw.ellipse([px - 15, py - 15, px + 15, py + 15], 
                     fill=COLORS['pink'], outline=COLORS['black'], width=1)
    draw.ellipse([cx - 12, flower_y - 12, cx + 12, flower_y + 12], 
                 fill=COLORS['yellow'], outline=COLORS['black'], width=1)
    
    return img

# ==================== 10. 尤卡坦 - 奇琴伊察 ====================
def create_yucatan_chichen_itza():
    """尤卡坦奇琴伊察塔 - 玛雅金字塔风格"""
    img = create_gradient_background(WIDTH, HEIGHT, COLORS['sky_top'], COLORS['sky_bottom'])
    draw = ImageDraw.Draw(img)
    
    cx, cy = WIDTH // 2, HEIGHT - 180
    
    # 金字塔层级（9层）
    levels = 9
    base_width = 400
    level_height = 40
    
    for i in range(levels):
        y = cy - i * level_height
        width = base_width - i * 30
        
        # 台阶效果
        step_depth = 10
        
        # 正面
        draw.polygon([
            (cx - width//2, y),
            (cx + width//2, y),
            (cx + width//2 - step_depth, y - level_height),
            (cx - width//2 + step_depth, y - level_height),
        ], fill=COLORS['sand'], outline=COLORS['black'], width=2)
        
        # 左侧阴影面
        draw.polygon([
            (cx - width//2, y),
            (cx - width//2 + step_depth, y - level_height),
            (cx - width//2 + step_depth * 2, y - level_height),
            (cx - width//2 + step_depth, y),
        ], fill=(180, 160, 120), outline=COLORS['black'], width=1)
    
    # 顶部神庙
    temple_y = cy - levels * level_height
    temple_width = base_width - levels * 30 + 20
    
    draw.polygon([
        (cx - temple_width//2, temple_y),
        (cx + temple_width//2, temple_y),
        (cx + temple_width//2, temple_y - 60),
        (cx - temple_width//2, temple_y - 60),
    ], fill=COLORS['sand'], outline=COLORS['black'], width=3)
    
    # 神庙门
    draw.rectangle([cx - 15, temple_y - 50, cx + 15, temple_y], 
                   fill=(80, 60, 40), outline=COLORS['black'], width=2)
    
    # 神庙屋顶
    draw.polygon([
        (cx - temple_width//2 - 10, temple_y - 60),
        (cx + temple_width//2 + 10, temple_y - 60),
        (cx, temple_y - 110),
    ], fill=COLORS['brown'], outline=COLORS['black'], width=2)
    
    # 脸部 - 在金字塔中部
    face_y = cy - levels * level_height // 2
    draw_angry_eyes(draw, cx, face_y, size=42)
    draw_cute_beak(draw, cx, face_y + 40, size=32)
    
    # 中央楼梯
    stair_width = 60
    for i in range(levels):
        y = cy - i * level_height
        draw.polygon([
            (cx - stair_width//2, y),
            (cx + stair_width//2, y),
            (cx + stair_width//2 - 5, y - level_height),
            (cx - stair_width//2 + 5, y - level_height),
        ], fill=(200, 180, 140), outline=COLORS['black'], width=1)
    
    # 顶部装饰
    draw.ellipse([cx - 12, temple_y - 135, cx + 12, temple_y - 110], 
                 fill=COLORS['gold'], outline=COLORS['black'], width=2)
    
    return img

# ==================== 主程序 ====================
def main():
    """生成所有墨西哥州塔图片"""
    
    # 确保输出目录存在
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # 定义塔列表
    towers = [
        ("mexico-city-zocalo.png", create_mexico_city_zocalo),
        ("jalisco-tequila.png", create_jalisco_tequila),
        ("veracruz-port.png", create_veracruz_port),
        ("puebla-pyramid.png", create_puebla_pyramid),
        ("guanajuato-colorful.png", create_guanajuato_colorful),
        ("nuevo-leon-monterrey.png", create_nuevo_leon_monterrey),
        ("chihuahua-copper-canyon.png", create_chihuahua_copper_canyon),
        ("baja-wine.png", create_baja_wine),
        ("sonora-desert.png", create_sonora_desert),
        ("yucatan-chichen-itza.png", create_yucatan_chichen_itza),
    ]
    
    print("🐍 小金蛇开始生成墨西哥州卡通塔...")
    print(f"输出目录: {OUTPUT_DIR}\n")
    
    for filename, create_func in towers:
        try:
            img = create_func()
            filepath = os.path.join(OUTPUT_DIR, filename)
            img.save(filepath, "PNG")
            print(f"✅ 已生成: {filename}")
        except Exception as e:
            print(f"❌ 生成失败: {filename} - {e}")
    
    print(f"\n🎉 完成！所有图片已保存到: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
