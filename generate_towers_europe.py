#!/usr/bin/env python3
"""
生成卡通化欧洲地标图片
风格：愤怒的小鸟卡通风格，可爱表情
尺寸：800x1200像素
背景：天蓝色渐变
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math
import os

def create_gradient_background(width, height):
    """创建天蓝色渐变背景"""
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    
    # 天蓝色渐变：从浅蓝到稍深的蓝色
    top_color = (135, 206, 250)  # 浅天蓝
    bottom_color = (70, 160, 220)  # 稍深的天蓝
    
    for y in range(height):
        ratio = y / height
        r = int(top_color[0] + (bottom_color[0] - top_color[0]) * ratio)
        g = int(top_color[1] + (bottom_color[1] - top_color[1]) * ratio)
        b = int(top_color[2] + (bottom_color[2] - top_color[2]) * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    return img

def draw_rounded_rect(draw, xy, radius, fill, outline=None, width=1):
    """绘制圆角矩形"""
    x1, y1, x2, y2 = xy
    # 主体矩形
    draw.rectangle([x1+radius, y1, x2-radius, y2], fill=fill)
    draw.rectangle([x1, y1+radius, x2, y2-radius], fill=fill)
    # 四个圆角
    draw.ellipse([x1, y1, x1+radius*2, y1+radius*2], fill=fill)
    draw.ellipse([x2-radius*2, y1, x2, y1+radius*2], fill=fill)
    draw.ellipse([x1, y2-radius*2, x1+radius*2, y2], fill=fill)
    draw.ellipse([x2-radius*2, y2-radius*2, x2, y2], fill=fill)
    
    if outline:
        # 绘制边框
        draw.arc([x1, y1, x1+radius*2, y1+radius*2], 180, 270, fill=outline, width=width)
        draw.arc([x2-radius*2, y1, x2, y1+radius*2], 270, 360, fill=outline, width=width)
        draw.arc([x1, y2-radius*2, x1+radius*2, y2], 90, 180, fill=outline, width=width)
        draw.arc([x2-radius*2, y2-radius*2, x2, y2], 0, 90, fill=outline, width=width)
        draw.line([x1+radius, y1, x2-radius, y1], fill=outline, width=width)
        draw.line([x1+radius, y2, x2-radius, y2], fill=outline, width=width)
        draw.line([x1, y1+radius, x1, y2-radius], fill=outline, width=width)
        draw.line([x2, y1+radius, x2, y2-radius], fill=outline, width=width)

def draw_cute_eyes(draw, cx, cy, size=20, happy=True):
    """绘制可爱的卡通眼睛"""
    eye_spacing = size * 1.5
    eye_y_offset = 0
    
    # 左眼
    lx, ly = cx - eye_spacing//2, cy + eye_y_offset
    # 右眼
    rx, ry = cx + eye_spacing//2, cy + eye_y_offset
    
    # 眼白（大圆）
    draw.ellipse([lx-size, ly-size, lx+size, ly+size], fill=(255, 255, 255), outline=(30, 30, 30), width=3)
    draw.ellipse([rx-size, ry-size, rx+size, ry+size], fill=(255, 255, 255), outline=(30, 30, 30), width=3)
    
    # 瞳孔
    pupil_size = size // 2
    draw.ellipse([lx-pupil_size, ly-pupil_size, lx+pupil_size, ly+pupil_size], fill=(30, 30, 30))
    draw.ellipse([rx-pupil_size, ry-pupil_size, rx+pupil_size, ry+pupil_size], fill=(30, 30, 30))
    
    # 高光
    highlight_size = size // 4
    draw.ellipse([lx-pupil_size-2, ly-pupil_size-5, lx-pupil_size+highlight_size, ly-pupil_size+highlight_size-5], fill=(255, 255, 255))
    draw.ellipse([rx-pupil_size-2, ry-pupil_size-5, rx-pupil_size+highlight_size, ry-pupil_size+highlight_size-5], fill=(255, 255, 255))

def draw_cute_mouth(draw, cx, cy, size=15, happy=True):
    """绘制可爱的卡通嘴巴"""
    if happy:
        # 开心的微笑
        draw.arc([cx-size, cy-size, cx+size, cy+size], 0, 180, fill=(30, 30, 30), width=3)
    else:
        # 惊讶的小圆嘴
        draw.ellipse([cx-size//2, cy, cx+size//2, cy+size], fill=(255, 100, 100), outline=(30, 30, 30), width=2)

def draw_cute_cheeks(draw, cx, cy, size=12):
    """绘制可爱的腮红"""
    cheek_spacing = 45
    draw.ellipse([cx-cheek_spacing-size, cy-size//2, cx-cheek_spacing+size, cy+size//2], fill=(255, 180, 180))
    draw.ellipse([cx+cheek_spacing-size, cy-size//2, cx+cheek_spacing+size, cy+size//2], fill=(255, 180, 180))

def draw_cloud(draw, x, y, size=40):
    """绘制卡通云朵"""
    color = (255, 255, 255)
    draw.ellipse([x-size, y-size//2, x+size, y+size//2], fill=color)
    draw.ellipse([x-size//2, y-size, x+size//2, y+size], fill=color)
    draw.ellipse([x, y-size//3, x+size, y+size//3], fill=color)

def draw_decorations(draw, width, height):
    """绘制装饰元素（云朵等）"""
    draw_cloud(draw, 100, 150, 50)
    draw_cloud(draw, 650, 100, 40)
    draw_cloud(draw, 700, 250, 35)
    draw_cloud(draw, 150, 300, 30)

# ==================== 1. 维也纳金色大厅 ====================
def draw_vienna_opera():
    """绘制维也纳金色大厅"""
    img = create_gradient_background(800, 1200)
    draw = ImageDraw.Draw(img)
    draw_decorations(draw, 800, 1200)
    
    cx, cy = 400, 650  # 中心点
    
    # 建筑主体 - 金色
    gold_color = (255, 215, 0)
    dark_gold = (218, 165, 32)
    
    # 底座
    draw.rectangle([150, 900, 650, 950], fill=(139, 90, 43), outline=(80, 50, 30), width=3)
    
    # 主建筑体
    draw.rectangle([180, 600, 620, 900], fill=gold_color, outline=dark_gold, width=4)
    
    # 屋顶 - 红色
    roof_points = [(150, 600), (400, 450), (650, 600)]
    draw.polygon(roof_points, fill=(180, 50, 50), outline=(120, 30, 30), width=4)
    
    # 屋顶装饰雕像
    draw.ellipse([380, 430, 420, 470], fill=gold_color, outline=dark_gold, width=3)
    
    # 柱子（简化版）
    for i in range(6):
        x = 200 + i * 70
        draw.rectangle([x, 620, x+40, 880], fill=(255, 235, 150), outline=dark_gold, width=3)
        # 柱头
        draw.ellipse([x-5, 610, x+45, 640], fill=gold_color, outline=dark_gold, width=2)
        draw.ellipse([x-5, 870, x+45, 900], fill=gold_color, outline=dark_gold, width=2)
    
    # 入口
    draw.rectangle([350, 800, 450, 900], fill=(80, 40, 20), outline=(50, 25, 15), width=3)
    draw.arc([350, 750, 450, 850], 0, 180, fill=(80, 40, 20), width=3)
    
    # 窗户
    for i in range(2):
        for j in range(3):
            wx = 230 + i * 300
            wy = 680 + j * 60
            draw.rectangle([wx, wy, wx+50, wy+40], fill=(200, 230, 255), outline=dark_gold, width=2)
    
    # 可爱的表情 - 在建筑顶部
    draw_cute_eyes(draw, cx, 520, 18)
    draw_cute_mouth(draw, cx, 550, 12)
    draw_cute_cheeks(draw, cx, 540)
    
    # 标签
    try:
        font = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 40)
    except:
        font = ImageFont.load_default()
    draw.text((400, 1050), "维也纳金色大厅", fill=(50, 50, 50), font=font, anchor="mm")
    
    return img

# ==================== 2. 布拉格广场 - 天文钟 ====================
def draw_prague():
    """绘制布拉格天文钟"""
    img = create_gradient_background(800, 1200)
    draw = ImageDraw.Draw(img)
    draw_decorations(draw, 800, 1200)
    
    cx, cy = 400, 600
    
    # 建筑颜色
    wall_color = (210, 180, 140)  # 米色石墙
    dark_wall = (160, 140, 100)
    roof_color = (80, 50, 50)  # 深棕色屋顶
    
    # 左侧建筑
    draw.rectangle([100, 400, 300, 900], fill=wall_color, outline=dark_wall, width=3)
    # 右侧建筑
    draw.rectangle([500, 400, 700, 900], fill=wall_color, outline=dark_wall, width=3)
    
    # 屋顶
    draw.polygon([(80, 400), (200, 300), (320, 400)], fill=roof_color, outline=(50, 30, 30), width=3)
    draw.polygon([(480, 400), (600, 300), (720, 400)], fill=roof_color, outline=(50, 30, 30), width=3)
    
    # 中央天文钟楼
    tower_color = (180, 150, 110)
    draw.rectangle([280, 350, 520, 900], fill=tower_color, outline=(130, 110, 80), width=4)
    
    # 尖顶
    draw.polygon([(280, 350), (400, 150), (520, 350)], fill=(100, 60, 60), outline=(60, 40, 40), width=3)
    
    # 天文钟 - 圆形
    clock_x, clock_y = 400, 550
    clock_radius = 100
    
    # 钟外框
    draw.ellipse([clock_x-clock_radius-10, clock_y-clock_radius-10, 
                  clock_x+clock_radius+10, clock_y+clock_radius+10], 
                 fill=(80, 50, 30), outline=(50, 30, 20), width=4)
    
    # 钟面 - 深蓝底色
    draw.ellipse([clock_x-clock_radius, clock_y-clock_radius, 
                  clock_x+clock_radius, clock_y+clock_radius], 
                 fill=(30, 50, 100), outline=(218, 165, 32), width=5)
    
    # 天文环装饰
    for r in [30, 50, 70]:
        draw.ellipse([clock_x-r, clock_y-r, clock_x+r, clock_y+r], 
                     outline=(218, 165, 32), width=2)
    
    # 星座图案（简化）
    for i in range(12):
        angle = i * 30 * math.pi / 180
        px = clock_x + int(60 * math.cos(angle))
        py = clock_y + int(60 * math.sin(angle))
        draw.ellipse([px-5, py-5, px+5, py+5], fill=(255, 215, 0))
    
    # 指针
    draw.line([clock_x, clock_y, clock_x+40, clock_y-30], fill=(255, 215, 0), width=4)
    draw.line([clock_x, clock_y, clock_x-20, clock_y+50], fill=(200, 150, 50), width=3)
    
    # 中心点
    draw.ellipse([clock_x-8, clock_y-8, clock_x+8, clock_y+8], fill=(255, 50, 50))
    
    # 给天文钟添加可爱表情
    draw_cute_eyes(draw, clock_x, clock_y-35, 12)
    draw_cute_mouth(draw, clock_x, clock_y-20, 8)
    
    # 建筑窗户
    for x in [150, 250]:
        draw.rectangle([x, 500, x+50, 600], fill=(100, 60, 40), outline=(60, 40, 30), width=2)
        draw.rectangle([x+10, 510, x+40, 590], fill=(200, 230, 255))
    
    for x in [550, 650]:
        draw.rectangle([x, 500, x+50, 600], fill=(100, 60, 40), outline=(60, 40, 30), width=2)
        draw.rectangle([x+10, 510, x+40, 590], fill=(200, 230, 255))
    
    # 标签
    try:
        font = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 40)
    except:
        font = ImageFont.load_default()
    draw.text((400, 1050), "布拉格天文钟", fill=(50, 50, 50), font=font, anchor="mm")
    
    return img

# ==================== 3. 布达佩斯国会大厦 ====================
def draw_budapest():
    """绘制布达佩斯国会大厦"""
    img = create_gradient_background(800, 1200)
    draw = ImageDraw.Draw(img)
    draw_decorations(draw, 800, 1200)
    
    cx, cy = 400, 600
    
    # 颜色
    white_stone = (240, 240, 230)
    dark_stone = (180, 180, 170)
    red_roof = (180, 60, 60)
    dome_color = (220, 220, 210)
    
    # 多瑙河
    draw.rectangle([0, 950, 800, 1200], fill=(100, 150, 200), outline=(80, 130, 180), width=2)
    # 河水波纹
    for i in range(5):
        y = 1000 + i * 40
        for x in range(0, 800, 100):
            draw.arc([x, y, x+60, y+20], 0, 180, fill=(120, 170, 220), width=2)
    
    # 主建筑
    draw.rectangle([100, 600, 700, 950], fill=white_stone, outline=dark_stone, width=4)
    
    # 中央大圆顶
    dome_y = 450
    draw.ellipse([250, dome_y, 550, dome_y+300], fill=dome_color, outline=dark_stone, width=4)
    # 圆顶上的小金顶
    draw.polygon([(380, dome_y-80), (400, dome_y-150), (420, dome_y-80)], fill=(218, 165, 32), outline=(180, 140, 30), width=2)
    draw.ellipse([395, dome_y-165, 405, dome_y-145], fill=(255, 215, 0))
    
    # 两侧塔楼
    for x in [120, 620]:
        draw.rectangle([x, 500, x+80, 950], fill=white_stone, outline=dark_stone, width=3)
        # 塔尖
        draw.polygon([(x, 500), (x+40, 350), (x+80, 500)], fill=red_roof, outline=(120, 40, 40), width=3)
        # 塔顶装饰
        draw.line([x+40, 350, x+40, 320], fill=(218, 165, 32), width=4)
        draw.ellipse([x+35, 310, x+45, 330], fill=(255, 215, 0))
    
    # 中央入口柱廊
    for i in range(8):
        x = 200 + i * 50
        draw.rectangle([x, 750, x+30, 950], fill=(220, 220, 210), outline=dark_stone, width=2)
        draw.ellipse([x-5, 740, x+35, 780], fill=white_stone, outline=dark_stone, width=2)
    
    # 台阶
    for i in range(5):
        y = 950 + i * 8
        draw.rectangle([150-i*20, y, 650+i*20, y+8], fill=(200, 200, 190), outline=(170, 170, 160), width=1)
    
    # 窗户
    for i in range(6):
        x = 200 + i * 80
        draw.rectangle([x, 650, x+50, 720], fill=(180, 210, 240), outline=dark_stone, width=2)
        draw.arc([x, 650, x+50, 700], 0, 180, fill=dark_stone, width=2)
    
    # 可爱表情 - 在大圆顶上
    draw_cute_eyes(draw, cx, dome_y+100, 20)
    draw_cute_mouth(draw, cx, dome_y+140, 15)
    draw_cute_cheeks(draw, cx, dome_y+130)
    
    # 标签
    try:
        font = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 36)
    except:
        font = ImageFont.load_default()
    draw.text((400, 1050), "布达佩斯国会大厦", fill=(50, 50, 50), font=font, anchor="mm")
    draw.text((400, 1100), "多瑙河畔", fill=(80, 80, 80), font=font, anchor="mm")
    
    return img

# ==================== 4. 华沙老城 ====================
def draw_warsaw():
    """绘制华沙老城彩色建筑"""
    img = create_gradient_background(800, 1200)
    draw = ImageDraw.Draw(img)
    draw_decorations(draw, 800, 1200)
    
    cx, cy = 400, 600
    
    # 鹅卵石街道
    draw.rectangle([0, 900, 800, 1200], fill=(160, 140, 120), outline=(140, 120, 100), width=2)
    for i in range(20):
        x = (i * 47) % 800
        y = 920 + (i * 23) % 280
        draw.ellipse([x, y, x+15, y+10], fill=(140, 120, 100))
    
    # 彩色建筑数组
    colors = [
        (255, 180, 180),  # 粉红
        (180, 220, 255),  # 天蓝
        (255, 255, 180),  # 黄色
        (180, 255, 180),  # 绿色
        (255, 200, 150),  # 橙色
    ]
    
    roof_colors = [
        (150, 50, 50),
        (80, 80, 120),
        (150, 120, 50),
        (50, 100, 50),
        (150, 100, 50),
    ]
    
    building_width = 130
    start_x = 75
    
    for i in range(5):
        x = start_x + i * building_width
        color = colors[i]
        roof_color = roof_colors[i]
        
        # 建筑主体高度不一
        height = 400 + (i % 3) * 50
        
        # 建筑
        draw.rectangle([x, 900-height, x+building_width-10, 900], fill=color, outline=(100, 100, 100), width=3)
        
        # 尖顶屋顶
        roof_height = 100 + (i % 2) * 30
        draw.polygon([(x-10, 900-height), (x+(building_width-10)//2, 900-height-roof_height), (x+building_width, 900-height)], 
                     fill=roof_color, outline=(60, 40, 40), width=3)
        
        # 窗户 - 每层2个
        floors = 4
        for f in range(floors):
            wy = 900 - height + 40 + f * 80
            draw.rectangle([x+20, wy, x+50, wy+50], fill=(220, 240, 255), outline=(80, 80, 80), width=2)
            draw.rectangle([x+70, wy, x+100, wy+50], fill=(220, 240, 255), outline=(80, 80, 80), width=2)
            # 窗框十字
            draw.line([x+35, wy, x+35, wy+50], fill=(80, 80, 80), width=2)
            draw.line([x+20, wy+25, x+50, wy+25], fill=(80, 80, 80), width=2)
            draw.line([x+85, wy, x+85, wy+50], fill=(80, 80, 80), width=2)
            draw.line([x+70, wy+25, x+100, wy+25], fill=(80, 80, 80), width=2)
        
        # 门
        draw.rectangle([x+35, 840, x+85, 900], fill=(100, 60, 40), outline=(60, 40, 30), width=2)
        draw.arc([x+35, 800, x+85, 860], 0, 180, fill=(60, 40, 30), width=2)
    
    # 中央最高的建筑添加表情
    main_building_x = start_x + 2 * building_width + 60
    draw_cute_eyes(draw, main_building_x, 650, 18)
    draw_cute_mouth(draw, main_building_x, 680, 12)
    draw_cute_cheeks(draw, main_building_x, 670)
    
    # 标签
    try:
        font = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 40)
    except:
        font = ImageFont.load_default()
    draw.text((400, 1050), "华沙老城", fill=(50, 50, 50), font=font, anchor="mm")
    draw.text((400, 1100), "彩色建筑", fill=(80, 80, 80), font=font, anchor="mm")
    
    return img

# ==================== 5. 基辅圣索菲亚大教堂 ====================
def draw_kyiv():
    """绘制基辅圣索菲亚大教堂"""
    img = create_gradient_background(800, 1200)
    draw = ImageDraw.Draw(img)
    draw_decorations(draw, 800, 1200)
    
    cx, cy = 400, 600
    
    # 颜色
    white_wall = (245, 245, 240)
    blue_roof = (65, 105, 225)
    gold_dome = (255, 215, 0)
    
    # 主建筑
    draw.rectangle([200, 550, 600, 950], fill=white_wall, outline=(180, 180, 170), width=4)
    
    # 中央主圆顶
    draw.ellipse([300, 350, 500, 550], fill=blue_roof, outline=(45, 85, 195), width=4)
    # 主金色洋葱顶
    draw.ellipse([360, 280, 440, 360], fill=gold_dome, outline=(218, 165, 32), width=3)
    draw.line([400, 260, 400, 280], fill=(218, 165, 32), width=4)
    draw.ellipse([395, 250, 405, 270], fill=gold_dome)
    
    # 四个小圆顶
    dome_positions = [(250, 500), (550, 500), (250, 650), (550, 650)]
    for dx, dy in dome_positions:
        draw.ellipse([dx-50, dy-50, dx+50, dy+50], fill=blue_roof, outline=(45, 85, 195), width=3)
        # 小金洋葱
        draw.ellipse([dx-20, dy-60, dx+20, dy-20], fill=gold_dome, outline=(218, 165, 32), width=2)
        draw.line([dx, dy-75, dx, dy-60], fill=(218, 165, 32), width=3)
        draw.ellipse([dx-5, dy-85, dx+5, dy-75], fill=gold_dome)
    
    # 拱形窗户
    for i in range(3):
        wx = 280 + i * 100
        draw.rectangle([wx, 750, wx+60, 850], fill=(200, 220, 250), outline=(150, 150, 140), width=2)
        draw.arc([wx, 720, wx+60, 800], 0, 180, fill=(150, 150, 140), width=3)
    
    # 装饰性拱门
    for i in range(4):
        ax = 220 + i * 100
        draw.arc([ax, 880, ax+80, 980], 0, 180, fill=(150, 150, 140), width=3)
    
    # 铃铛塔（右侧）
    draw.rectangle([620, 400, 720, 950], fill=white_wall, outline=(180, 180, 170), width=3)
    draw.rectangle([630, 450, 710, 550], fill=(200, 220, 250), outline=(150, 150, 140), width=2)
    # 钟楼屋顶
    draw.polygon([(620, 400), (670, 280), (720, 400)], fill=blue_roof, outline=(45, 85, 195), width=3)
    draw.ellipse([650, 250, 690, 290], fill=gold_dome, outline=(218, 165, 32), width=2)
    
    # 可爱表情 - 在主圆顶上
    draw_cute_eyes(draw, cx, 450, 20)
    draw_cute_mouth(draw, cx, 485, 15)
    draw_cute_cheeks(draw, cx, 475)
    
    # 标签
    try:
        font = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 38)
    except:
        font = ImageFont.load_default()
    draw.text((400, 1050), "基辅圣索菲亚大教堂", fill=(50, 50, 50), font=font, anchor="mm")
    
    return img

# ==================== 6. 斯德哥尔摩老城 ====================
def draw_stockholm():
    """绘制斯德哥尔摩老城"""
    img = create_gradient_background(800, 1200)
    draw = ImageDraw.Draw(img)
    draw_decorations(draw, 800, 1200)
    
    cx, cy = 400, 600
    
    # 颜色
    warm_orange = (230, 150, 80)
    warm_yellow = (255, 220, 120)
    red_brown = (160, 80, 60)
    green_roof = (80, 120, 80)
    
    # 水面
    draw.rectangle([0, 850, 800, 1200], fill=(120, 170, 200), outline=(100, 150, 180), width=2)
    
    # 左侧建筑 - 橙色
    draw.rectangle([50, 550, 250, 900], fill=warm_orange, outline=(180, 120, 60), width=3)
    draw.polygon([(40, 550), (150, 400), (260, 550)], fill=green_roof, outline=(60, 90, 60), width=3)
    # 尖顶
    draw.line([150, 400, 150, 350], fill=(80, 80, 100), width=4)
    draw.ellipse([145, 340, 155, 360], fill=(200, 200, 210))
    
    # 中央主建筑 - 黄色
    draw.rectangle([250, 500, 550, 900], fill=warm_yellow, outline=(200, 170, 90), width=4)
    # 阶梯状山墙
    gable_points = [(250, 500), (300, 420), (350, 480), (400, 380), (450, 480), (500, 420), (550, 500)]
    draw.polygon(gable_points, fill=red_brown, outline=(120, 60, 45), width=3)
    # 中央尖顶
    draw.polygon([(380, 380), (400, 280), (420, 380)], fill=(60, 60, 80), outline=(40, 40, 60), width=3)
    draw.ellipse([395, 265, 405, 285], fill=(200, 200, 210))
    
    # 右侧建筑 - 深橙色
    draw.rectangle([550, 580, 750, 900], fill=(220, 130, 90), outline=(170, 100, 70), width=3)
    draw.polygon([(540, 580), (650, 450), (760, 580)], fill=green_roof, outline=(60, 90, 60), width=3)
    draw.line([650, 450, 650, 400], fill=(80, 80, 100), width=4)
    draw.ellipse([645, 390, 655, 410], fill=(200, 200, 210))
    
    # 窗户 - 白色带深色框架
    window_color = (250, 250, 245)
    
    # 左建筑窗户
    for y in [600, 700, 800]:
        draw.rectangle([80, y, 120, y+60], fill=window_color, outline=(120, 80, 40), width=2)
        draw.rectangle([140, y, 180, y+60], fill=window_color, outline=(120, 80, 40), width=2)
        # 窗框
        draw.line([100, y, 100, y+60], fill=(120, 80, 40), width=2)
        draw.line([160, y, 160, y+60], fill=(120, 80, 40), width=2)
    
    # 中央建筑窗户
    for y in [600, 700, 800]:
        for x in [300, 400, 500]:
            draw.rectangle([x-30, y, x+30, y+70], fill=window_color, outline=(150, 120, 60), width=2)
            draw.arc([x-30, y-20, x+30, y+30], 0, 180, fill=(150, 120, 60), width=2)
    
    # 右建筑窗户
    for y in [650, 750, 850]:
        draw.rectangle([580, y, 630, y+60], fill=window_color, outline=(130, 70, 50), width=2)
        draw.rectangle([660, y, 710, y+60], fill=window_color, outline=(130, 70, 50), width=2)
    
    # 可爱表情 - 在中央建筑
    draw_cute_eyes(draw, 400, 550, 18)
    draw_cute_mouth(draw, 400, 580, 12)
    draw_cute_cheeks(draw, 400, 570)
    
    # 标签
    try:
        font = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 38)
    except:
        font = ImageFont.load_default()
    draw.text((400, 1050), "斯德哥尔摩老城", fill=(50, 50, 50), font=font, anchor="mm")
    
    return img

# ==================== 7. 哥本哈根小美人鱼 ====================
def draw_copenhagen():
    """绘制哥本哈根小美人鱼"""
    img = create_gradient_background(800, 1200)
    draw = ImageDraw.Draw(img)
    draw_decorations(draw, 800, 1200)
    
    cx, cy = 400, 600
    
    # 颜色
    rock_color = (140, 140, 140)
    rock_dark = (100, 100, 100)
    skin_color = (255, 220, 190)
    hair_color = (180, 100, 50)
    tail_color = (100, 180, 180)
    
    # 海洋
    draw.rectangle([0, 700, 800, 1200], fill=(100, 160, 200), outline=(80, 140, 180), width=2)
    # 波浪
    for i in range(10):
        x = (i * 85) % 900 - 50
        y = 700 + (i * 37) % 400
        draw.arc([x, y, x+80, y+30], 0, 180, fill=(120, 180, 220), width=3)
    
    # 岩石基座
    rock_points = [(200, 900), (300, 750), (500, 700), (600, 800), (650, 950), (550, 1000), (250, 980)]
    draw.polygon(rock_points, fill=rock_color, outline=rock_dark, width=4)
    
    # 岩石纹理
    for i in range(8):
        x = 250 + (i * 45) % 350
        y = 750 + (i * 30) % 200
        draw.ellipse([x, y, x+20, y+15], fill=(120, 120, 120))
    
    # 小美人鱼
    mermaid_x, mermaid_y = 400, 650
    
    # 鱼尾
    tail_points = [(mermaid_x, mermaid_y+80), (mermaid_x-40, mermaid_y+180), 
                   (mermaid_x, mermaid_y+220), (mermaid_x+40, mermaid_y+180)]
    draw.polygon(tail_points, fill=tail_color, outline=(80, 150, 150), width=3)
    # 鱼鳞效果
    for i in range(3):
        y = mermaid_y + 120 + i * 30
        draw.arc([mermaid_x-30, y, mermaid_x+30, y+20], 0, 180, fill=(80, 150, 150), width=2)
    
    # 鱼尾鳍
    fin_points = [(mermaid_x, mermaid_y+220), (mermaid_x-50, mermaid_y+280), 
                  (mermaid_x, mermaid_y+260), (mermaid_x+50, mermaid_y+280)]
    draw.polygon(fin_points, fill=(120, 200, 200), outline=(80, 150, 150), width=3)
    
    # 身体
    draw.ellipse([mermaid_x-30, mermaid_y+20, mermaid_x+30, mermaid_y+100], fill=tail_color, outline=(80, 150, 150), width=3)
    
    # 头部
    draw.ellipse([mermaid_x-35, mermaid_y-40, mermaid_x+35, mermaid_y+40], fill=skin_color, outline=(220, 190, 160), width=3)
    
    # 头发 - 长发飘逸
    hair_points = [
        (mermaid_x-35, mermaid_y-20),
        (mermaid_x-60, mermaid_y+20),
        (mermaid_x-50, mermaid_y+80),
        (mermaid_x-30, mermaid_y+60),
        (mermaid_x+30, mermaid_y+60),
        (mermaid_x+50, mermaid_y+80),
        (mermaid_x+60, mermaid_y+20),
        (mermaid_x+35, mermaid_y-20),
    ]
    draw.polygon(hair_points, fill=hair_color, outline=(150, 80, 40), width=2)
    # 头顶头发
    draw.ellipse([mermaid_x-40, mermaid_y-60, mermaid_x+40, mermaid_y+10], fill=hair_color, outline=(150, 80, 40), width=2)
    
    # 可爱表情
    draw_cute_eyes(draw, mermaid_x, mermaid_y-10, 16)
    draw_cute_mouth(draw, mermaid_x, mermaid_y+15, 10)
    draw_cute_cheeks(draw, mermaid_x, mermaid_y+5)
    
    # 手臂
    draw.line([mermaid_x-25, mermaid_y+40, mermaid_x-50, mermaid_y+70], fill=skin_color, width=8)
    draw.line([mermaid_x+25, mermaid_y+40, mermaid_x+50, mermaid_y+70], fill=skin_color, width=8)
    draw.ellipse([mermaid_x-55, mermaid_y+65, mermaid_x-45, mermaid_y+75], fill=skin_color)
    draw.ellipse([mermaid_x+45, mermaid_y+65, mermaid_x+55, mermaid_y+75], fill=skin_color)
    
    # 岩石上的海藻/装饰
    for i in range(5):
        sx = 300 + i * 70
        draw.line([sx, 750, sx-10, 720], fill=(80, 150, 80), width=4)
        draw.line([sx+5, 755, sx+15, 725], fill=(100, 180, 100), width=3)
    
    # 标签
    try:
        font = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 38)
    except:
        font = ImageFont.load_default()
    draw.text((400, 1050), "哥本哈根小美人鱼", fill=(50, 50, 50), font=font, anchor="mm")
    
    return img

def main():
    """主函数：生成所有图片"""
    output_dir = "/Users/moutai/Desktop/toweroffate_v1.0/assets/towers"
    os.makedirs(output_dir, exist_ok=True)
    
    towers = [
        ("vienna-opera.png", draw_vienna_opera, "维也纳金色大厅"),
        ("prague.png", draw_prague, "布拉格广场"),
        ("budapest.png", draw_budapest, "布达佩斯国会大厦"),
        ("warsaw.png", draw_warsaw, "华沙老城"),
        ("kyiv.png", draw_kyiv, "基辅圣索菲亚大教堂"),
        ("stockholm.png", draw_stockholm, "斯德哥尔摩老城"),
        ("copenhagen.png", draw_copenhagen, "哥本哈根小美人鱼"),
    ]
    
    for filename, draw_func, name in towers:
        try:
            img = draw_func()
            filepath = os.path.join(output_dir, filename)
            img.save(filepath, "PNG", quality=95)
            print(f"✅ 已生成: {filename} - {name}")
        except Exception as e:
            print(f"❌ 失败: {filename} - {name}: {e}")
    
    print(f"\n🎉 所有图片已保存到: {output_dir}")

if __name__ == "__main__":
    main()
