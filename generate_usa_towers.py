#!/usr/bin/env python3
"""
生成美国州卡通塔图片 - 愤怒的小鸟风格
"""

from PIL import Image, ImageDraw, ImageFont
import math
import os

# 输出目录
OUTPUT_DIR = "/Users/moutai/Desktop/toweroffate_v1.0/assets/towers/states/usa/"

# 图片尺寸
WIDTH, HEIGHT = 800, 1200

def create_gradient_background(width, height):
    """创建天蓝色渐变背景"""
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    
    # 天蓝色渐变 - 从浅蓝到更浅的蓝
    for y in range(height):
        # 渐变比例
        ratio = y / height
        # 从天蓝(135, 206, 235)到更浅的天蓝(200, 240, 255)
        r = int(135 + (200 - 135) * ratio)
        g = int(206 + (240 - 206) * ratio)
        b = int(235 + (255 - 235) * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    return img

def draw_circle_eye(draw, x, y, size, pupil_offset=(0, 0)):
    """绘制愤怒的小鸟风格的大眼睛"""
    # 眼白
    draw.ellipse([x-size, y-size, x+size, y+size], fill=(255, 255, 255), outline=(0, 0, 0), width=2)
    # 瞳孔
    pupil_x = x + pupil_offset[0]
    pupil_y = y + pupil_offset[1]
    pupil_size = size // 2
    draw.ellipse([pupil_x-pupil_size, pupil_y-pupil_size, pupil_x+pupil_size, pupil_y+pupil_size], fill=(0, 0, 0))
    # 高光
    highlight_size = size // 5
    draw.ellipse([pupil_x-pupil_size//2, pupil_y-pupil_size//2, 
                  pupil_x+pupil_size//2, pupil_y+pupil_size//2], fill=(255, 255, 255))

def draw_cute_mouth(draw, x, y, size, happy=True):
    """绘制可爱的嘴巴"""
    if happy:
        # 微笑
        draw.arc([x-size, y-size, x+size, y+size], start=0, end=180, fill=(0, 0, 0), width=3)
    else:
        # 惊讶/中性
        draw.ellipse([x-size//2, y-size//2, x+size//2, y+size//2], fill=(200, 50, 50))

def draw_rounded_rect(draw, bbox, radius, fill, outline=None, width=1):
    """绘制圆角矩形"""
    x1, y1, x2, y2 = bbox
    # 主体矩形
    draw.rectangle([x1+radius, y1, x2-radius, y2], fill=fill)
    draw.rectangle([x1, y1+radius, x2, y2-radius], fill=fill)
    # 四个圆角
    draw.pieslice([x1, y1, x1+radius*2, y1+radius*2], 180, 270, fill=fill)
    draw.pieslice([x2-radius*2, y1, x2, y1+radius*2], 270, 360, fill=fill)
    draw.pieslice([x1, y2-radius*2, x1+radius*2, y2], 90, 180, fill=fill)
    draw.pieslice([x2-radius*2, y2-radius*2, x2, y2], 0, 90, fill=fill)
    
    if outline:
        draw.arc([x1, y1, x1+radius*2, y1+radius*2], 180, 270, fill=outline, width=width)
        draw.arc([x2-radius*2, y1, x2, y1+radius*2], 270, 360, fill=outline, width=width)
        draw.arc([x1, y2-radius*2, x1+radius*2, y2], 90, 180, fill=outline, width=width)
        draw.arc([x2-radius*2, y2-radius*2, x2, y2], 0, 90, fill=outline, width=width)
        draw.line([x1+radius, y1, x2-radius, y1], fill=outline, width=width)
        draw.line([x1+radius, y2, x2-radius, y2], fill=outline, width=width)
        draw.line([x1, y1+radius, x1, y2-radius], fill=outline, width=width)
        draw.line([x2, y1+radius, x2, y2-radius], fill=outline, width=width)

def draw_tower_base(draw, x, y, width, height, color, dark_color):
    """绘制塔的基础 - 愤怒的小鸟风格的圆柱形"""
    # 主体 - 圆柱形
    draw_rounded_rect(draw, [x-width//2, y-height, x+width//2, y], 30, color, (0, 0, 0), 3)
    
    # 顶部圆形盖子
    draw.ellipse([x-width//2-10, y-height-30, x+width//2+10, y-height+30], fill=color, outline=(0, 0, 0), width=3)
    
    # 阴影/高光效果
    draw.arc([x-width//2+20, y-height, x+width//2-20, y], 0, 180, fill=dark_color, width=20)

def california_golden_gate():
    """加州 - 金门大桥塔"""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    
    center_x, base_y = WIDTH//2, HEIGHT - 100
    
    # 绘制塔身 - 国际橙色
    tower_color = (204, 85, 0)  # 国际橙色
    dark_color = (150, 60, 0)
    
    # 主塔结构
    for i in range(3):
        y_offset = i * 200
        w = 250 - i * 30
        draw_tower_base(draw, center_x, base_y - y_offset, w, 180, tower_color, dark_color)
    
    # 塔顶
    draw.ellipse([center_x-80, base_y-600-40, center_x+80, base_y-600+40], fill=tower_color, outline=(0,0,0), width=3)
    
    # 金门大桥元素 - 悬索
    draw.line([(center_x-200, base_y), (center_x-80, base_y-580)], fill=(180, 70, 0), width=8)
    draw.line([(center_x+200, base_y), (center_x+80, base_y-580)], fill=(180, 70, 0), width=8)
    
    # 垂直悬索
    for i in range(8):
        y = base_y - 50 - i * 70
        draw.line([(center_x-200+i*25, base_y), (center_x-200+i*25, y)], fill=(160, 60, 0), width=3)
        draw.line([(center_x+200-i*25, base_y), (center_x+200-i*25, y)], fill=(160, 60, 0), width=3)
    
    # 可爱的大眼睛
    draw_circle_eye(draw, center_x-40, base_y-550, 35, (-5, 5))
    draw_circle_eye(draw, center_x+40, base_y-550, 35, (5, 5))
    
    # 微笑
    draw_cute_mouth(draw, center_x, base_y-500, 30)
    
    # 腮红
    draw.ellipse([center_x-80, base_y-520, center_x-50, base_y-490], fill=(255, 150, 150))
    draw.ellipse([center_x+50, base_y-520, center_x+80, base_y-490], fill=(255, 150, 150))
    
    return img

def texas_cowboy():
    """德州 - 牛仔帽+仙人掌塔"""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    
    center_x, base_y = WIDTH//2, HEIGHT - 100
    
    # 仙人掌绿色
    cactus_color = (34, 139, 34)
    dark_cactus = (20, 90, 20)
    
    # 主仙人掌身体
    draw_rounded_rect(draw, [center_x-100, base_y-500, center_x+100, base_y], 50, cactus_color, (0,0,0), 3)
    
    # 左侧手臂
    draw_rounded_rect(draw, [center_x-200, base_y-350, center_x-100, base_y-250], 40, cactus_color, (0,0,0), 3)
    draw.ellipse([center_x-200-40, base_y-350-40, center_x-200+40, base_y-350+40], fill=cactus_color, outline=(0,0,0), width=3)
    
    # 右侧手臂
    draw_rounded_rect(draw, [center_x+100, base_y-400, center_x+200, base_y-300], 40, cactus_color, (0,0,0), 3)
    draw.ellipse([center_x+200-40, base_y-400-40, center_x+200+40, base_y-400+40], fill=cactus_color, outline=(0,0,0), width=3)
    
    # 仙人掌纹理
    for i in range(5):
        y = base_y - 400 + i * 80
        draw.line([(center_x-60, y), (center_x-40, y)], fill=dark_cactus, width=4)
        draw.line([(center_x+40, y), (center_x+60, y)], fill=dark_cactus, width=4)
    
    # 牛仔帽
    hat_color = (139, 69, 19)  # 棕色
    # 帽檐
    draw.ellipse([center_x-180, base_y-560, center_x+180, base_y-480], fill=hat_color, outline=(0,0,0), width=3)
    # 帽顶
    draw_rounded_rect(draw, [center_x-80, base_y-650, center_x+80, base_y-520], 20, hat_color, (0,0,0), 3)
    
    # 帽子上的星星
    draw.polygon([
        (center_x, base_y-620),
        (center_x+10, base_y-600),
        (center_x+30, base_y-600),
        (center_x+15, base_y-585),
        (center_x+20, base_y-565),
        (center_x, base_y-575),
        (center_x-20, base_y-565),
        (center_x-15, base_y-585),
        (center_x-30, base_y-600),
        (center_x-10, base_y-600),
    ], fill=(255, 215, 0), outline=(0,0,0))
    
    # 眼睛
    draw_circle_eye(draw, center_x-50, base_y-480, 30, (-5, 0))
    draw_circle_eye(draw, center_x+50, base_y-480, 30, (5, 0))
    
    # 微笑
    draw_cute_mouth(draw, center_x, base_y-430, 25)
    
    # 腮红
    draw.ellipse([center_x-90, base_y-460, center_x-60, base_y-430], fill=(255, 150, 150))
    draw.ellipse([center_x+60, base_y-460, center_x+90, base_y-430], fill=(255, 150, 150))
    
    return img

def new_york_liberty():
    """纽约 - 自由女神+时代广场塔"""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    
    center_x, base_y = WIDTH//2, HEIGHT - 100
    
    # 自由女神绿色
    statue_color = (50, 150, 100)
    dark_color = (30, 100, 60)
    
    # 塔基座
    draw_rounded_rect(draw, [center_x-120, base_y-200, center_x+120, base_y], 20, (150, 150, 150), (0,0,0), 3)
    
    # 女神身体
    draw_rounded_rect(draw, [center_x-80, base_y-450, center_x+80, base_y-200], 30, statue_color, (0,0,0), 3)
    
    # 长袍褶皱
    for i in range(4):
        x = center_x - 60 + i * 40
        draw.line([(x, base_y-420), (x, base_y-220)], fill=dark_color, width=4)
    
    # 头部
    draw.ellipse([center_x-60, base_y-530, center_x+60, base_y-430], fill=statue_color, outline=(0,0,0), width=3)
    
    # 皇冠
    crown_color = (255, 215, 0)
    for i in range(7):
        angle = -60 + i * 20
        x1 = center_x + int(50 * math.sin(math.radians(angle)))
        y1 = base_y - 530 - 40
        x2 = center_x + int(70 * math.sin(math.radians(angle)))
        y2 = base_y - 530 - 70
        draw.polygon([(x1, y1), (x2-5, y2), (x2+5, y2)], fill=crown_color, outline=(0,0,0))
    draw.ellipse([center_x-55, base_y-550, center_x+55, base_y-510], fill=crown_color, outline=(0,0,0), width=2)
    
    # 火炬
    torch_x, torch_y = center_x + 100, base_y - 450
    draw_rounded_rect(draw, [torch_x-15, torch_y-80, torch_x+15, torch_y], 10, (200, 150, 50), (0,0,0), 2)
    # 火焰
    flame_colors = [(255, 100, 0), (255, 200, 0), (255, 255, 100)]
    for i, color in enumerate(flame_colors):
        size = 50 - i * 15
        draw.ellipse([torch_x-size, torch_y-120-i*20, torch_x+size, torch_y-60-i*20], fill=color)
    
    # 时代广场霓虹灯效果
    for i in range(8):
        x = center_x - 150 + i * 40
        colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]
        color = colors[i % len(colors)]
        draw.rectangle([x, base_y-150, x+25, base_y-100], fill=color, outline=(0,0,0), width=2)
    
    # 眼睛
    draw_circle_eye(draw, center_x-30, base_y-490, 25, (-3, 2))
    draw_circle_eye(draw, center_x+30, base_y-490, 25, (3, 2))
    
    # 微笑
    draw_cute_mouth(draw, center_x, base_y-460, 20)
    
    return img

def florida_beach():
    """佛州 - 海滩+棕榈树塔"""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    
    center_x, base_y = WIDTH//2, HEIGHT - 100
    
    # 沙滩塔身
    sand_color = (238, 203, 140)
    dark_sand = (200, 160, 100)
    
    # 沙滩基础
    draw_rounded_rect(draw, [center_x-150, base_y-300, center_x+150, base_y], 40, sand_color, (0,0,0), 3)
    
    # 波浪纹理
    for i in range(4):
        y = base_y - 250 + i * 60
        for j in range(5):
            x = center_x - 120 + j * 60
            draw.arc([x, y, x+40, y+30], 0, 180, fill=(150, 200, 255), width=4)
    
    # 棕榈树树干 - 弯曲的
    trunk_color = (139, 90, 43)
    points = []
    for i in range(20):
        t = i / 19
        x = center_x + int(30 * math.sin(t * 3))
        y = base_y - 300 - int(t * 300)
        points.append((x, y))
    
    for i in range(len(points)-1):
        draw.line([points[i], points[i+1]], fill=trunk_color, width=20)
    
    # 棕榈叶
    leaf_color = (34, 139, 34)
    top_x, top_y = points[-1]
    for angle in range(0, 360, 45):
        rad = math.radians(angle)
        for r in range(20, 120, 10):
            x = top_x + int(r * math.cos(rad))
            y = top_y + int(r * math.sin(rad))
            size = 15 - r // 10
            draw.ellipse([x-size, y-size, x+size, y+size], fill=leaf_color)
    draw.ellipse([top_x-40, top_y-40, top_x+40, top_y+40], fill=leaf_color, outline=(0,0,0), width=2)
    
    # 椰子
    for angle in [30, 150, 270]:
        rad = math.radians(angle)
        x = top_x + int(35 * math.cos(rad))
        y = top_y + int(35 * math.sin(rad))
        draw.ellipse([x-15, y-20, x+15, y+20], fill=(139, 90, 43), outline=(0,0,0), width=2)
    
    # 太阳装饰
    draw.ellipse([center_x+200, 100, center_x+320, 220], fill=(255, 220, 50), outline=(255, 180, 0), width=5)
    for angle in range(0, 360, 30):
        rad = math.radians(angle)
        x1 = center_x + 260 + int(70 * math.cos(rad))
        y1 = 160 + int(70 * math.sin(rad))
        x2 = center_x + 260 + int(90 * math.cos(rad))
        y2 = 160 + int(90 * math.sin(rad))
        draw.line([(x1, y1), (x2, y2)], fill=(255, 200, 0), width=4)
    
    # 眼睛 - 在树干上
    draw_circle_eye(draw, center_x-40, base_y-180, 28, (-4, 0))
    draw_circle_eye(draw, center_x+40, base_y-180, 28, (4, 0))
    
    # 微笑
    draw_cute_mouth(draw, center_x, base_y-130, 25)
    
    # 腮红
    draw.ellipse([center_x-80, base_y-160, center_x-50, base_y-130], fill=(255, 150, 150))
    draw.ellipse([center_x+50, base_y-160, center_x+80, base_y-130], fill=(255, 150, 150))
    
    return img

def illinois_chicago():
    """伊利诺伊 - 芝加哥天际线塔"""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    
    center_x, base_y = WIDTH//2, HEIGHT - 100
    
    # 摩天大楼颜色
    building_colors = [
        (100, 120, 150),
        (120, 140, 170),
        (90, 110, 140),
        (130, 150, 180),
    ]
    
    # 绘制多个摩天大楼组成塔身
    buildings = [
        (-150, 250, 80, 400),
        (-80, 200, 70, 450),
        (0, 150, 100, 500),  # 中间最高
        (60, 220, 75, 430),
        (130, 280, 70, 370),
    ]
    
    for i, (offset, height, width, b_height) in enumerate(buildings):
        x = center_x + offset
        color = building_colors[i % len(building_colors)]
        # 大楼主体
        draw_rounded_rect(draw, [x-width//2, base_y-b_height, x+width//2, base_y], 10, color, (0,0,0), 2)
        
        # 窗户
        for row in range(5, int(b_height)//50):
            for col in range(2, width//20):
                wx = x - width//2 + col * 18
                wy = base_y - row * 50
                if (row + col) % 3 == 0:
                    draw.rectangle([wx, wy, wx+10, wy+15], fill=(255, 255, 150))  # 亮灯
                else:
                    draw.rectangle([wx, wy, wx+10, wy+15], fill=(60, 70, 90))  # 暗窗
    
    # 天线
    draw.line([(center_x, base_y-650), (center_x, base_y-500)], fill=(200, 200, 200), width=8)
    draw.ellipse([center_x-20, base_y-670, center_x+20, base_y-630], fill=(255, 50, 50))
    
    # 眼睛 - 在最高的建筑上
    draw_circle_eye(draw, center_x-35, base_y-400, 30, (-5, 3))
    draw_circle_eye(draw, center_x+35, base_y-400, 30, (5, 3))
    
    # 微笑
    draw_cute_mouth(draw, center_x, base_y-350, 25)
    
    # 腮红
    draw.ellipse([center_x-80, base_y-380, center_x-50, base_y-350], fill=(255, 150, 150))
    draw.ellipse([center_x+50, base_y-380, center_x+80, base_y-350], fill=(255, 150, 150))
    
    return img

def pennsylvania_liberty_bell():
    """宾州 - 自由钟塔"""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    
    center_x, base_y = WIDTH//2, HEIGHT - 100
    
    # 钟的颜色
    bell_color = (180, 150, 100)
    dark_bell = (140, 110, 60)
    
    # 钟塔基座
    draw_rounded_rect(draw, [center_x-130, base_y-250, center_x+130, base_y], 30, (120, 100, 80), (0,0,0), 3)
    
    # 巨大的钟形塔身
    # 钟顶
    draw.ellipse([center_x-120, base_y-550, center_x+120, base_y-400], fill=bell_color, outline=(0,0,0), width=4)
    
    # 钟身
    draw.polygon([
        (center_x-100, base_y-430),
        (center_x+100, base_y-430),
        (center_x+130, base_y-200),
        (center_x-130, base_y-200),
    ], fill=bell_color, outline=(0,0,0), width=4)
    
    # 钟的纹理和细节
    for i in range(5):
        y = base_y - 400 + i * 45
        draw.arc([center_x-90+i*5, y, center_x+90-i*5, y+40], 0, 180, fill=dark_bell, width=3)
    
    # 裂缝！著名的自由钟裂缝
    crack_points = [
        (center_x+30, base_y-420),
        (center_x+25, base_y-380),
        (center_x+40, base_y-350),
        (center_x+20, base_y-300),
    ]
    for i in range(len(crack_points)-1):
        draw.line([crack_points[i], crack_points[i+1]], fill=(60, 50, 40), width=5)
    
    # 钟内的舌头/撞击器
    draw.ellipse([center_x-30, base_y-250, center_x+30, base_y-180], fill=(200, 170, 120), outline=(0,0,0), width=3)
    
    # 眼睛
    draw_circle_eye(draw, center_x-50, base_y-480, 32, (-4, 2))
    draw_circle_eye(draw, center_x+40, base_y-480, 32, (4, 2))
    
    # 微笑
    draw_cute_mouth(draw, center_x, base_y-430, 28)
    
    # 腮红
    draw.ellipse([center_x-100, base_y-460, center_x-65, base_y-425], fill=(255, 150, 150))
    draw.ellipse([center_x+65, base_y-460, center_x+100, base_y-425], fill=(255, 150, 150))
    
    return img

def ohio_rock_hall():
    """俄亥俄 - 摇滚名人堂塔"""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    
    center_x, base_y = WIDTH//2, HEIGHT - 100
    
    # 摇滚风格 - 黑色和金属色
    rock_color = (40, 40, 50)
    metal_color = (150, 150, 160)
    accent_color = (220, 50, 50)  # 红色摇滚元素
    
    # 基座 - 舞台风格
    draw_rounded_rect(draw, [center_x-180, base_y-200, center_x+180, base_y], 20, rock_color, (0,0,0), 3)
    
    # 主塔 - 独特的几何形状像摇滚名人堂建筑
    # 三角形塔身
    draw.polygon([
        (center_x, base_y-600),
        (center_x-130, base_y-200),
        (center_x+130, base_y-200),
    ], fill=rock_color, outline=(0,0,0), width=4)
    
    # 玻璃幕墙效果
    for i in range(8):
        y1 = base_y - 550 + i * 45
        y2 = y1 + 35
        x1 = center_x - 40 - i * 10
        x2 = center_x + 40 + i * 10
        draw.polygon([
            (center_x, y1),
            (x1, y2),
            (x2, y2),
        ], fill=(100+i*10, 150+i*5, 200))
    
    # 吉他元素
    guitar_x, guitar_y = center_x - 100, base_y - 150
    # 吉他琴身
    draw.ellipse([guitar_x-50, guitar_y-30, guitar_x+50, guitar_y+50], fill=(200, 50, 50), outline=(0,0,0), width=3)
    draw.ellipse([guitar_x-30, guitar_y-10, guitar_x+30, guitar_y+30], fill=(255, 100, 100))
    # 琴颈
    draw.rounded_rectangle([guitar_x-15, guitar_y-120, guitar_x+15, guitar_y], radius=5, fill=(139, 90, 43), outline=(0,0,0), width=2)
    
    # 扬声器
    for i, x_offset in enumerate([-120, 120]):
        sx = center_x + x_offset
        draw.rectangle([sx-40, base_y-180, sx+40, base_y-80], fill=(50, 50, 50), outline=(0,0,0), width=3)
        draw.ellipse([sx-30, base_y-170, sx+30, base_y-130], fill=(100, 100, 100), outline=(0,0,0), width=2)
        draw.ellipse([sx-30, base_y-120, sx+30, base_y-80], fill=(100, 100, 100), outline=(0,0,0), width=2)
    
    # 眼睛
    draw_circle_eye(draw, center_x-50, base_y-500, 30, (-5, 3))
    draw_circle_eye(draw, center_x+50, base_y-500, 30, (5, 3))
    
    # 摇滚风格的咧嘴笑
    draw.arc([center_x-40, base_y-480, center_x+40, base_y-420], start=0, end=180, fill=(0,0,0), width=4)
    # 牙齿
    for i in range(4):
        x = center_x - 25 + i * 18
        draw.rectangle([x, base_y-460, x+12, base_y-445], fill=(255, 255, 255), outline=(0,0,0))
    
    return img

def georgia_coke():
    """乔治亚 - 可口可乐塔"""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    
    center_x, base_y = WIDTH//2, HEIGHT - 100
    
    # 可口可乐红
    coke_red = (240, 40, 40)
    dark_red = (180, 20, 20)
    white = (255, 255, 255)
    
    # 瓶子形状塔身
    # 瓶底
    draw.ellipse([center_x-120, base_y-100, center_x+120, base_y], fill=coke_red, outline=(0,0,0), width=3)
    
    # 瓶身主体
    draw_rounded_rect(draw, [center_x-100, base_y-450, center_x+100, base_y-50], 40, coke_red, (0,0,0), 3)
    
    # 瓶肩
    draw.polygon([
        (center_x-100, base_y-450),
        (center_x+100, base_y-450),
        (center_x-50, base_y-550),
        (center_x+50, base_y-550),
    ], fill=coke_red, outline=(0,0,0), width=3)
    
    # 瓶颈
    draw_rounded_rect(draw, [center_x-40, base_y-650, center_x+40, base_y-550], 15, coke_red, (0,0,0), 3)
    
    # 瓶盖
    draw.ellipse([center_x-50, base_y-680, center_x+50, base_y-630], fill=(200, 200, 200), outline=(0,0,0), width=3)
    
    # 波浪纹装饰 - 可乐瓶标志
    for i in range(3):
        y = base_y - 350 + i * 80
        # 白色波浪条
        draw.arc([center_x-80, y, center_x+80, y+60], 180, 360, fill=white, width=20)
        draw.arc([center_x-60, y+20, center_x+60, y+80], 0, 180, fill=coke_red, width=15)
    
    # 气泡
    for i in range(15):
        import random
        bx = center_x + random.randint(-80, 80)
        by = base_y - random.randint(100, 400)
        size = random.randint(8, 20)
        draw.ellipse([bx-size, by-size, bx+size, by+size], fill=(255, 255, 255, 180))
        draw.arc([bx-size, by-size, bx+size, by+size], 45, 180, fill=(200, 200, 200), width=2)
    
    # 眼睛
    draw_circle_eye(draw, center_x-45, base_y-580, 32, (-4, 2))
    draw_circle_eye(draw, center_x+45, base_y-580, 32, (4, 2))
    
    # 微笑
    draw_cute_mouth(draw, center_x, base_y-530, 28)
    
    # 腮红
    draw.ellipse([center_x-90, base_y-560, center_x-55, base_y-525], fill=(255, 180, 180))
    draw.ellipse([center_x+55, base_y-560, center_x+90, base_y-525], fill=(255, 180, 180))
    
    return img

def washington_space_needle():
    """华盛顿州 - 太空针塔"""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    
    center_x, base_y = WIDTH//2, HEIGHT - 100
    
    # 太空针塔颜色
    needle_color = (200, 200, 210)
    dark_metal = (150, 150, 160)
    accent_color = (255, 100, 100)
    
    # 塔基
    draw.ellipse([center_x-150, base_y-80, center_x+150, base_y], fill=(100, 100, 110), outline=(0,0,0), width=3)
    
    # 支撑腿
    for angle in [-30, 0, 30]:
        rad = math.radians(angle)
        x1 = center_x + int(80 * math.sin(rad))
        y1 = base_y - 80
        x2 = center_x + int(30 * math.sin(rad))
        y2 = base_y - 350
        draw.line([(x1, y1), (x2, y2)], fill=dark_metal, width=25)
    
    # 中央核心
    draw.line([(center_x, base_y-80), (center_x, base_y-500)], fill=needle_color, width=30)
    
    # 观景台 - 飞碟形状
    # 底部圆盘
    draw.ellipse([center_x-180, base_y-400, center_x+180, base_y-320], fill=needle_color, outline=(0,0,0), width=4)
    # 顶部圆顶
    draw.ellipse([center_x-140, base_y-480, center_x+140, base_y-380], fill=(220, 220, 230), outline=(0,0,0), width=3)
    
    # 观景台窗户
    for i in range(12):
        angle = i * 30
        rad = math.radians(angle)
        x = center_x + int(100 * math.cos(rad))
        y = base_y - 360 + int(20 * math.sin(rad))
        draw.ellipse([x-15, y-20, x+15, y+20], fill=(100, 200, 255), outline=(0,0,0), width=2)
    
    # 天线
    draw.line([(center_x, base_y-600), (center_x, base_y-480)], fill=needle_color, width=8)
    draw.ellipse([center_x-15, base_y-620, center_x+15, base_y-580], fill=(255, 50, 50))
    
    # 眼睛 - 在观景台上
    draw_circle_eye(draw, center_x-50, base_y-430, 30, (-4, 2))
    draw_circle_eye(draw, center_x+50, base_y-430, 30, (4, 2))
    
    # 微笑
    draw_cute_mouth(draw, center_x, base_y-380, 25)
    
    # 腮红
    draw.ellipse([center_x-100, base_y-410, center_x-65, base_y-375], fill=(255, 150, 150))
    draw.ellipse([center_x+65, base_y-410, center_x+100, base_y-375], fill=(255, 150, 150))
    
    # 星星装饰
    for _ in range(10):
        import random
        sx = random.randint(50, WIDTH-50)
        sy = random.randint(50, 200)
        size = random.randint(10, 20)
        draw.polygon([
            (sx, sy-size), (sx+size//3, sy-size//3),
            (sx+size, sy), (sx+size//3, sy+size//3),
            (sx, sy+size), (sx-size//3, sy+size//3),
            (sx-size, sy), (sx-size//3, sy-size//3),
        ], fill=(255, 220, 100))
    
    return img

def new_jersey_boardwalk():
    """新泽西 - 海滨木板路塔"""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    
    center_x, base_y = WIDTH//2, HEIGHT - 100
    
    # 木板颜色
    wood_color = (200, 170, 130)
    dark_wood = (160, 130, 90)
    
    # 木板路基座
    for i in range(8):
        x = center_x - 160 + i * 45
        draw.rectangle([x, base_y-100, x+40, base_y], fill=wood_color, outline=(0,0,0), width=2)
        # 木板纹理
        draw.line([(x+5, base_y-100), (x+5, base_y)], fill=dark_wood, width=2)
        draw.line([(x+20, base_y-100), (x+20, base_y)], fill=dark_wood, width=2)
        draw.line([(x+35, base_y-100), (x+35, base_y)], fill=dark_wood, width=2)
    
    # 塔身 - 木板结构
    draw_rounded_rect(draw, [center_x-120, base_y-450, center_x+120, base_y-100], 20, wood_color, (0,0,0), 3)
    
    # 横向木板条
    for i in range(8):
        y = base_y - 420 + i * 40
        draw.rectangle([center_x-120, y, center_x+120, y+25], fill=wood_color, outline=(0,0,0), width=2)
        # 钉子
        draw.ellipse([center_x-100, y+10, center_x-90, y+20], fill=(100, 100, 100))
        draw.ellipse([center_x+90, y+10, center_x+100, y+20], fill=(100, 100, 100))
    
    # 顶部遮阳棚
    draw.polygon([
        (center_x-160, base_y-450),
        (center_x+160, base_y-450),
        (center_x+140, base_y-520),
        (center_x-140, base_y-520),
    ], fill=(255, 100, 100), outline=(0,0,0), width=3)
    
    # 遮阳棚条纹
    for i in range(6):
        x = center_x - 130 + i * 50
        draw.polygon([
            (x, base_y-450),
            (x+25, base_y-450),
            (x+20, base_y-510),
            (x-5, base_y-510),
        ], fill=(255, 255, 255))
    
    # 旗杆
    draw.line([(center_x+100, base_y-520), (center_x+100, base_y-620)], fill=(150, 150, 150), width=6)
    # 旗帜
    draw.polygon([
        (center_x+100, base_y-620),
        (center_x+200, base_y-590),
        (center_x+100, base_y-560),
    ], fill=(255, 50, 50), outline=(0,0,0), width=2)
    
    # 游乐设施元素 - 摩天轮轮廓
    wheel_x, wheel_y = center_x - 150, base_y - 250
    draw.ellipse([wheel_x-60, wheel_y-60, wheel_x+60, wheel_y+60], outline=(255, 50, 50), width=4)
    draw.line([(wheel_x, wheel_y-60), (wheel_x, wheel_y+60)], fill=(255, 50, 50), width=3)
    draw.line([(wheel_x-60, wheel_y), (wheel_x+60, wheel_y)], fill=(255, 50, 50), width=3)
    # 摩天轮座舱
    for angle in [0, 45, 90, 135, 180, 225, 270, 315]:
        rad = math.radians(angle)
        x = wheel_x + int(50 * math.cos(rad))
        y = wheel_y + int(50 * math.sin(rad))
        draw.ellipse([x-10, y-10, x+10, y+10], fill=(255, 200, 0), outline=(0,0,0), width=2)
    
    # 眼睛
    draw_circle_eye(draw, center_x-50, base_y-480, 30, (-4, 2))
    draw_circle_eye(draw, center_x+50, base_y-480, 30, (4, 2))
    
    # 微笑
    draw_cute_mouth(draw, center_x, base_y-430, 25)
    
    # 腮红
    draw.ellipse([center_x-100, base_y-460, center_x-65, base_y-425], fill=(255, 150, 150))
    draw.ellipse([center_x+65, base_y-460, center_x+100, base_y-425], fill=(255, 150, 150))
    
    return img

def main():
    """生成所有州塔图片"""
    towers = [
        (california_golden_gate, "california-golden-gate.png"),
        (texas_cowboy, "texas-cowboy.png"),
        (new_york_liberty, "new-york-liberty.png"),
        (florida_beach, "florida-beach.png"),
        (illinois_chicago, "illinois-chicago.png"),
        (pennsylvania_liberty_bell, "pennsylvania-liberty-bell.png"),
        (ohio_rock_hall, "ohio-rock-hall.png"),
        (georgia_coke, "georgia-coke.png"),
        (washington_space_needle, "washington-space-needle.png"),
        (new_jersey_boardwalk, "new-jersey-boardwalk.png"),
    ]
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    for func, filename in towers:
        print(f"Generating {filename}...")
        img = func()
        filepath = os.path.join(OUTPUT_DIR, filename)
        img.save(filepath, "PNG", quality=95)
        print(f"  Saved: {filepath}")
    
    print("\n✅ All 10 USA state towers generated successfully!")

if __name__ == "__main__":
    main()
