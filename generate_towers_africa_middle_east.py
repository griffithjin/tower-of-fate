#!/usr/bin/env python3
"""
生成非洲+中东+中亚地区卡通风格地标图片
愤怒的小鸟风格 - 可爱表情
"""

from PIL import Image, ImageDraw, ImageFont
import math
import os

# 图片规格
WIDTH = 800
HEIGHT = 1200
BG_TOP = (135, 206, 250)  # 天蓝色
BG_BOTTOM = (176, 224, 230)  # 淡蓝色

def create_gradient_background(draw, width, height):
    """创建天蓝色渐变背景"""
    for y in range(height):
        ratio = y / height
        r = int(BG_TOP[0] + (BG_BOTTOM[0] - BG_TOP[0]) * ratio)
        g = int(BG_TOP[1] + (BG_BOTTOM[1] - BG_TOP[1]) * ratio)
        b = int(BG_TOP[2] + (BG_BOTTOM[2] - BG_TOP[2]) * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

def draw_angry_bird_style_eyes(draw, x, y, size=30):
    """绘制愤怒的小鸟风格的可爱眼睛"""
    # 白色眼白
    draw.ellipse([x-size, y-size//2, x+size, y+size//2], fill=(255, 255, 255), outline=(0, 0, 0), width=2)
    draw.ellipse([x+size, y-size//2, x+size*3, y+size//2], fill=(255, 255, 255), outline=(0, 0, 0), width=2)
    # 黑色瞳孔
    draw.ellipse([x-size//3, y-size//4, x+size//3, y+size//4], fill=(0, 0, 0))
    draw.ellipse([x+size+size//3, y-size//4, x+size*2+size//3, y+size//4], fill=(0, 0, 0))
    # 高光
    draw.ellipse([x-size//4, y-size//3, x, y-size//6], fill=(255, 255, 255))
    draw.ellipse([x+size+size//2, y-size//3, x+size+size//4*3, y-size//6], fill=(255, 255, 255))

def draw_cute_smile(draw, x, y, size=20):
    """绘制可爱微笑"""
    draw.arc([x-size, y, x+size, y+size*2], start=0, end=180, fill=(0, 0, 0), width=3)

def draw_ground(draw, y):
    """绘制地面"""
    draw.rectangle([0, y, WIDTH, HEIGHT], fill=(144, 238, 144))  # 浅绿色草地
    # 草地纹理
    for i in range(0, WIDTH, 30):
        draw.polygon([(i, y), (i+15, y-10), (i+30, y)], fill=(34, 139, 34))

def draw_cloud(draw, x, y, size=60):
    """绘制云朵"""
    color = (255, 255, 255)
    draw.ellipse([x-size, y-size//2, x+size, y+size//2], fill=color)
    draw.ellipse([x-size//2, y-size, x+size//2, y+size], fill=color)
    draw.ellipse([x, y-size//2, x+size*1.5, y+size//2], fill=color)

def draw_sun(draw, x, y, size=50):
    """绘制卡通太阳"""
    # 太阳光芒
    for angle in range(0, 360, 30):
        rad = math.radians(angle)
        x1 = x + math.cos(rad) * (size + 10)
        y1 = y + math.sin(rad) * (size + 10)
        x2 = x + math.cos(rad) * (size + 25)
        y2 = y + math.sin(rad) * (size + 25)
        draw.line([(x1, y1), (x2, y2)], fill=(255, 215, 0), width=4)
    # 太阳本体
    draw.ellipse([x-size, y-size, x+size, y+size], fill=(255, 255, 0), outline=(255, 215, 0), width=3)
    # 太阳眼睛
    draw_angry_bird_style_eyes(draw, x, y-5, 12)
    draw_cute_smile(draw, x, y+15, 8)

# ==================== 1. 摩洛哥 - 舍夫沙万蓝色小镇 ====================
def create_chefchaouen():
    img = Image.new('RGB', (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(img)
    create_gradient_background(draw, WIDTH, HEIGHT)
    
    # 云朵
    draw_cloud(draw, 150, 150, 50)
    draw_cloud(draw, 600, 200, 60)
    draw_cloud(draw, 400, 100, 40)
    
    # 地面
    draw_ground(draw, 900)
    
    # 蓝色建筑群
    blue_colors = [(70, 130, 180), (100, 149, 237), (65, 105, 225), (30, 144, 255)]
    
    # 建筑1 - 带表情的主建筑
    x1, y1, w1, h1 = 100, 500, 200, 350
    draw.rectangle([x1, y1, x1+w1, y1+h1], fill=blue_colors[0], outline=(0, 0, 100), width=3)
    # 屋顶
    draw.polygon([(x1-20, y1), (x1+w1//2, y1-60), (x1+w1+20, y1)], fill=(139, 69, 19))
    # 窗户
    draw.rectangle([x1+50, y1+80, x1+100, y1+150], fill=(135, 206, 250), outline=(255, 255, 255), width=2)
    draw.rectangle([x1+120, y1+80, x1+170, y1+150], fill=(135, 206, 250), outline=(255, 255, 255), width=2)
    # 可爱表情
    draw_angry_bird_style_eyes(draw, x1+w1//2, y1+200, 25)
    draw_cute_smile(draw, x1+w1//2, y1+240, 15)
    
    # 建筑2
    x2, y2, w2, h2 = 350, 550, 180, 300
    draw.rectangle([x2, y2, x2+w2, y2+h2], fill=blue_colors[1], outline=(0, 0, 100), width=3)
    draw.polygon([(x2-15, y2), (x2+w2//2, y2-50), (x2+w2+15, y2)], fill=(139, 69, 19))
    draw.rectangle([x2+40, y2+60, x2+90, y2+120], fill=(135, 206, 250), outline=(255, 255, 255), width=2)
    draw_angry_bird_style_eyes(draw, x2+w2//2, y2+180, 20)
    draw_cute_smile(draw, x2+w2//2, y2+210, 12)
    
    # 建筑3
    x3, y3, w3, h3 = 550, 480, 160, 370
    draw.rectangle([x3, y3, x3+w3, y3+h3], fill=blue_colors[2], outline=(0, 0, 100), width=3)
    draw.polygon([(x3-15, y3), (x3+w3//2, y3-60), (x3+w3+15, y3)], fill=(139, 69, 19))
    draw.rectangle([x3+35, y3+70, x3+85, y3+130], fill=(135, 206, 250), outline=(255, 255, 255), width=2)
    draw.rectangle([x3+100, y3+70, x3+125, y3+200], fill=(139, 69, 19), outline=(100, 50, 0), width=2)  # 门
    draw_angry_bird_style_eyes(draw, x3+w3//2, y3+250, 22)
    draw_cute_smile(draw, x3+w3//2, y3+290, 14)
    
    # 标题
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 40)
    except:
        font = ImageFont.load_default()
    draw.text((WIDTH//2-200, 50), "Chefchaouen", fill=(255, 255, 255), font=font, stroke_width=2, stroke_fill=(0, 0, 0))
    draw.text((WIDTH//2-150, 100), "Morocco", fill=(255, 255, 200), font=font, stroke_width=2, stroke_fill=(0, 0, 0))
    
    return img

# ==================== 2. 肯尼亚 - 乞力马扎罗山 ====================
def create_kilimanjaro():
    img = Image.new('RGB', (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(img)
    create_gradient_background(draw, WIDTH, HEIGHT)
    
    # 太阳
    draw_sun(draw, 650, 120, 45)
    
    # 云朵
    draw_cloud(draw, 200, 150, 55)
    
    # 地面
    draw_ground(draw, 950)
    
    # 乞力马扎罗山 - 雪山
    # 山体主体
    mountain_color = (139, 119, 101)
    snow_color = (255, 250, 250)
    
    # 左峰
    points_left = [(150, 850), (300, 400), (450, 850)]
    draw.polygon(points_left, fill=mountain_color, outline=(100, 80, 60), width=3)
    # 雪顶
    snow_left = [(240, 530), (300, 400), (360, 530), (320, 500), (300, 480), (280, 500)]
    draw.polygon(snow_left, fill=snow_color, outline=(200, 200, 220), width=2)
    
    # 主峰 - 带表情
    points_main = [(350, 900), (550, 300), (750, 900)]
    draw.polygon(points_main, fill=mountain_color, outline=(100, 80, 60), width=3)
    # 雪顶
    snow_main = [(480, 430), (550, 300), (620, 430), (580, 400), (550, 370), (520, 400)]
    draw.polygon(snow_main, fill=snow_color, outline=(200, 200, 220), width=2)
    
    # 山的表情
    draw_angry_bird_style_eyes(draw, 550, 550, 28)
    draw_cute_smile(draw, 550, 600, 18)
    
    # 右小峰
    points_right = [(650, 850), (750, 500), (850, 850)]
    draw.polygon(points_right, fill=mountain_color, outline=(100, 80, 60), width=3)
    snow_right = [(710, 590), (750, 500), (790, 590), (770, 570), (750, 550), (730, 570)]
    draw.polygon(snow_right, fill=snow_color, outline=(200, 200, 220), width=2)
    
    # 大象剪影 - 卡通风格
    elephant_x, elephant_y = 250, 820
    # 身体
    draw.ellipse([elephant_x, elephant_y, elephant_x+120, elephant_y+80], fill=(80, 60, 40), outline=(50, 40, 30), width=2)
    # 头
    draw.ellipse([elephant_x+90, elephant_y-20, elephant_x+150, elephant_y+50], fill=(80, 60, 40), outline=(50, 40, 30), width=2)
    # 象鼻
    draw.arc([elephant_x+130, elephant_y-10, elephant_x+180, elephant_y+60], start=0, end=120, fill=(80, 60, 40), width=15)
    # 耳朵
    draw.ellipse([elephant_x+100, elephant_y-40, elephant_x+140, elephant_y+10], fill=(100, 80, 60), outline=(50, 40, 30), width=2)
    # 腿
    for i in range(4):
        draw.rectangle([elephant_x+20+i*25, elephant_y+70, elephant_x+40+i*25, elephant_y+110], fill=(80, 60, 40), outline=(50, 40, 30), width=2)
    # 大象眼睛
    draw_angry_bird_style_eyes(draw, elephant_x+120, elephant_y+10, 10)
    
    # 标题
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 40)
    except:
        font = ImageFont.load_default()
    draw.text((WIDTH//2-200, 50), "Kilimanjaro", fill=(255, 255, 255), font=font, stroke_width=2, stroke_fill=(0, 0, 0))
    draw.text((WIDTH//2-120, 100), "Kenya", fill=(255, 255, 200), font=font, stroke_width=2, stroke_fill=(0, 0, 0))
    
    return img

# ==================== 3. 坦桑尼亚 - 塞伦盖蒂 ====================
def create_serengeti():
    img = Image.new('RGB', (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(img)
    create_gradient_background(draw, WIDTH, HEIGHT)
    
    # 太阳 - 日落风格
    draw.ellipse([550, 150, 700, 300], fill=(255, 140, 0), outline=(255, 100, 0), width=3)
    draw.angry_bird_style_eyes = lambda draw, x, y, size: draw_angry_bird_style_eyes(draw, x, y, size)
    draw_angry_bird_style_eyes(draw, 625, 225, 20)
    
    # 云朵
    draw_cloud(draw, 200, 180, 60)
    draw_cloud(draw, 400, 120, 45)
    
    # 地面 - 草原色
    draw.rectangle([0, 800, WIDTH, HEIGHT], fill=(218, 165, 32), outline=(184, 134, 11), width=3)
    # 草地纹理
    for i in range(0, WIDTH, 20):
        height_var = 20 + (i % 30)
        draw.line([(i, 800), (i, 800-height_var)], fill=(184, 134, 11), width=2)
    
    # 金合欢树 - 带表情
    tree_x, tree_y = 400, 800
    # 树干 - 弯曲的
    points_trunk = [
        (tree_x-30, tree_y), (tree_x-20, tree_y-150), (tree_x-40, tree_y-250),
        (tree_x+40, tree_y-250), (tree_x+20, tree_y-150), (tree_x+30, tree_y)
    ]
    draw.polygon(points_trunk, fill=(139, 90, 43), outline=(100, 60, 30), width=3)
    
    # 树冠 - 扁平的伞状
    canopy_y = tree_y - 250
    # 多层树冠
    for i, (cx, size) in enumerate([(tree_x-80, 70), (tree_x+80, 70), (tree_x, 90), (tree_x-40, 60), (tree_x+40, 60)]):
        green_val = 100 + i * 15
        draw.ellipse([cx-size, canopy_y-size//2, cx+size, canopy_y+size//2], 
                     fill=(50, green_val, 50), outline=(30, green_val-20, 30), width=2)
    
    # 树的眼睛
    draw_angry_bird_style_eyes(draw, tree_x, tree_y - 200, 18)
    draw_cute_smile(draw, tree_x, tree_y - 170, 10)
    
    # 远处的山丘
    draw.polygon([(0, 800), (200, 650), (400, 750), (600, 600), (800, 800)], 
                 fill=(210, 180, 140), outline=(180, 150, 100), width=2)
    
    # 小动物剪影 - 卡通风格的长颈鹿
    giraffe_x, giraffe_y = 150, 780
    # 身体
    draw.ellipse([giraffe_x, giraffe_y, giraffe_x+40, giraffe_y+25], fill=(160, 140, 100), outline=(130, 110, 70), width=2)
    # 脖子
    draw.rectangle([giraffe_x+25, giraffe_y-40, giraffe_x+35, giraffe_y], fill=(160, 140, 100), outline=(130, 110, 70), width=2)
    # 头
    draw.ellipse([giraffe_x+22, giraffe_y-55, giraffe_x+42, giraffe_y-35], fill=(160, 140, 100), outline=(130, 110, 70), width=2)
    # 腿
    for i in range(4):
        draw.rectangle([giraffe_x+5+i*9, giraffe_y+20, giraffe_x+12+i*9, giraffe_y+50], fill=(160, 140, 100), outline=(130, 110, 70), width=2)
    # 斑点
    draw.ellipse([giraffe_x+10, giraffe_y+5, giraffe_x+20, giraffe_y+15], fill=(140, 120, 80))
    draw.ellipse([giraffe_x+25, giraffe_y+10, giraffe_x+35, giraffe_y+20], fill=(140, 120, 80))
    draw_angry_bird_style_eyes(draw, giraffe_x+32, giraffe_y-45, 6)
    
    # 标题
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 40)
    except:
        font = ImageFont.load_default()
    draw.text((WIDTH//2-180, 50), "Serengeti", fill=(255, 255, 255), font=font, stroke_width=2, stroke_fill=(0, 0, 0))
    draw.text((WIDTH//2-160, 100), "Tanzania", fill=(255, 255, 200), font=font, stroke_width=2, stroke_fill=(0, 0, 0))
    
    return img

# ==================== 4. 以色列 - 耶路撒冷 ====================
def create_jerusalem():
    img = Image.new('RGB', (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(img)
    create_gradient_background(draw, WIDTH, HEIGHT)
    
    # 云朵
    draw_cloud(draw, 150, 160, 50)
    draw_cloud(draw, 600, 140, 55)
    
    # 地面
    draw_ground(draw, 900)
    
    # 圆顶清真寺 - 带表情
    dome_x, dome_y = 400, 850
    
    # 底座
    draw.rectangle([dome_x-120, dome_y-100, dome_x+120, dome_y], fill=(238, 203, 140), outline=(200, 170, 110), width=3)
    # 装饰条纹
    for i in range(3):
        y_pos = dome_y - 80 + i * 25
        draw.rectangle([dome_x-120, y_pos, dome_x+120, y_pos+10], fill=(0, 100, 150), outline=(0, 70, 100), width=1)
    
    # 拱形窗户
    draw.arc([dome_x-80, dome_y-80, dome_x-40, dome_y-40], start=0, end=180, fill=(139, 90, 43), width=4)
    draw.arc([dome_x+40, dome_y-80, dome_x+80, dome_y-40], start=0, end=180, fill=(139, 90, 43), width=4)
    
    # 金色圆顶 - 带表情
    draw.ellipse([dome_x-100, dome_y-280, dome_x+100, dome_y-100], fill=(255, 215, 0), outline=(218, 165, 32), width=4)
    
    # 圆顶表情
    draw_angry_bird_style_eyes(draw, dome_x, dome_y - 190, 25)
    draw_cute_smile(draw, dome_x, dome_y - 150, 15)
    
    # 顶部装饰
    draw.rectangle([dome_x-5, dome_y-300, dome_x+5, dome_y-280], fill=(255, 215, 0), outline=(218, 165, 32), width=2)
    draw.ellipse([dome_x-15, dome_y-310, dome_x+15, dome_y-290], fill=(255, 215, 0), outline=(218, 165, 32), width=2)
    
    # 墙壁装饰图案
    for i in range(-2, 3):
        x_pos = dome_x + i * 40
        draw.rectangle([x_pos-10, dome_y-70, x_pos+10, dome_y-50], fill=(0, 120, 180), outline=(0, 80, 120), width=1)
    
    # 旁边的建筑
    # 左侧建筑
    draw.rectangle([dome_x-200, dome_y-50, dome_x-130, dome_y], fill=(210, 180, 140), outline=(180, 150, 100), width=2)
    draw.polygon([(dome_x-210, dome_y-50), (dome_x-165, dome_y-90), (dome_x-120, dome_y-50)], fill=(139, 69, 19))
    draw_angry_bird_style_eyes(draw, dome_x-165, dome_y-25, 15)
    
    # 右侧建筑
    draw.rectangle([dome_x+130, dome_y-60, dome_x+200, dome_y], fill=(220, 190, 150), outline=(180, 150, 100), width=2)
    draw.polygon([(dome_x+120, dome_y-60), (dome_x+165, dome_y-100), (dome_x+210, dome_y-60)], fill=(139, 69, 19))
    draw_angry_bird_style_eyes(draw, dome_x+165, dome_y-30, 15)
    
    # 标题
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 40)
    except:
        font = ImageFont.load_default()
    draw.text((WIDTH//2-200, 50), "Jerusalem", fill=(255, 255, 255), font=font, stroke_width=2, stroke_fill=(0, 0, 0))
    draw.text((WIDTH//2-120, 100), "Israel", fill=(255, 255, 200), font=font, stroke_width=2, stroke_fill=(0, 0, 0))
    
    return img

# ==================== 5. 约旦 - 佩特拉 ====================
def create_petra():
    img = Image.new('RGB', (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(img)
    create_gradient_background(draw, WIDTH, HEIGHT)
    
    # 太阳
    draw_sun(draw, 120, 120, 40)
    
    # 云朵
    draw_cloud(draw, 500, 150, 55)
    
    # 地面 - 沙漠色
    draw.rectangle([0, 850, WIDTH, HEIGHT], fill=(238, 203, 140), outline=(210, 180, 120), width=3)
    
    # 佩特拉玫瑰古城 - 岩石雕刻风格
    rock_colors = [(205, 133, 63), (188, 143, 143), (210, 150, 100), (230, 170, 120)]
    
    # 主岩壁 - 带表情
    cliff_x, cliff_y = 400, 850
    # 岩壁轮廓 - 不规则形状
    cliff_points = [
        (cliff_x-250, cliff_y), (cliff_x-200, cliff_y-350), (cliff_x-100, cliff_y-400),
        (cliff_x, cliff_y-420), (cliff_x+100, cliff_y-400), (cliff_x+200, cliff_y-350),
        (cliff_x+250, cliff_y)
    ]
    draw.polygon(cliff_points, fill=rock_colors[0], outline=(160, 100, 50), width=4)
    
    # 岩壁纹理层次
    layer_points1 = [(cliff_x-230, cliff_y), (cliff_x-180, cliff_y-300), (cliff_x+180, cliff_y-300), (cliff_x+230, cliff_y)]
    draw.polygon(layer_points1, fill=rock_colors[1], outline=(160, 100, 50), width=2)
    
    # 卡兹尼神殿风格正面
    temple_y = cliff_y - 200
    # 柱子
    for i, x_offset in enumerate([-100, -50, 50, 100]):
        draw.rectangle([cliff_x+x_offset-15, temple_y, cliff_x+x_offset+15, temple_y+150], 
                      fill=rock_colors[2], outline=(160, 100, 50), width=2)
        # 柱头装饰
        draw.polygon([
            (cliff_x+x_offset-20, temple_y), (cliff_x+x_offset, temple_y-15), (cliff_x+x_offset+20, temple_y)
        ], fill=rock_colors[3], outline=(160, 100, 50), width=2)
    
    # 上层圆顶
    draw.ellipse([cliff_x-80, temple_y-100, cliff_x+80, temple_y+20], fill=rock_colors[3], outline=(160, 100, 50), width=3)
    
    # 岩壁表情
    draw_angry_bird_style_eyes(draw, cliff_x, temple_y + 80, 28)
    draw_cute_smile(draw, cliff_x, temple_y + 130, 18)
    
    # 雕刻细节
    draw.rectangle([cliff_x-60, temple_y+40, cliff_x+60, temple_y+120], fill=rock_colors[2], outline=(160, 100, 50), width=2)
    draw.arc([cliff_x-40, temple_y+50, cliff_x, temple_y+100], start=0, end=180, fill=(139, 90, 43), width=3)
    draw.arc([cliff_x, temple_y+50, cliff_x+40, temple_y+100], start=0, end=180, fill=(139, 90, 43), width=3)
    
    # 侧面小岩壁
    side_points = [(50, 850), (80, 700), (150, 650), (180, 850)]
    draw.polygon(side_points, fill=rock_colors[1], outline=(160, 100, 50), width=3)
    draw_angry_bird_style_eyes(draw, 115, 750, 18)
    
    side_points2 = [(620, 850), (650, 680), (720, 620), (780, 850)]
    draw.polygon(side_points2, fill=rock_colors[1], outline=(160, 100, 50), width=3)
    draw_angry_bird_style_eyes(draw, 690, 720, 18)
    
    # 沙漠植物
    for x in [100, 700]:
        draw.line([(x, 850), (x, 820)], fill=(107, 142, 35), width=4)
        draw.ellipse([x-10, 810, x+10, 830], fill=(107, 142, 35))
    
    # 标题
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 40)
    except:
        font = ImageFont.load_default()
    draw.text((WIDTH//2-100, 50), "Petra", fill=(255, 255, 255), font=font, stroke_width=2, stroke_fill=(0, 0, 0))
    draw.text((WIDTH//2-100, 100), "Jordan", fill=(255, 255, 200), font=font, stroke_width=2, stroke_fill=(0, 0, 0))
    
    return img

# ==================== 6. 伊朗 - 伊玛目广场 ====================
def create_imam_square():
    img = Image.new('RGB', (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(img)
    create_gradient_background(draw, WIDTH, HEIGHT)
    
    # 云朵
    draw_cloud(draw, 200, 140, 50)
    draw_cloud(draw, 600, 180, 60)
    
    # 地面
    draw_ground(draw, 900)
    
    # 蓝色瓷砖建筑 - 伊玛目清真寺风格
    blue_colors = [(0, 100, 150), (0, 130, 180), (70, 150, 200), (100, 180, 220)]
    
    # 主建筑 - 带表情
    main_x, main_y = 400, 850
    # 主体
    draw.rectangle([main_x-150, main_y-200, main_x+150, main_y], fill=blue_colors[0], outline=(0, 70, 100), width=3)
    
    # 蓝色瓷砖图案装饰
    for row in range(4):
        for col in range(6):
            x = main_x - 130 + col * 45
            y = main_y - 180 + row * 45
            color = blue_colors[(row + col) % 4]
            draw.rectangle([x, y, x+35, y+35], fill=color, outline=(255, 255, 255), width=1)
            # 内部装饰图案
            draw.ellipse([x+10, y+10, x+25, y+25], fill=(255, 215, 0), outline=(218, 165, 32), width=1)
    
    # 主圆顶
    dome_points = [(main_x-100, main_y-200), (main_x, main_y-380), (main_x+100, main_y-200)]
    draw.polygon(dome_points, fill=blue_colors[2], outline=(0, 100, 150), width=3)
    # 圆顶上的瓷砖图案
    for i in range(3):
        y_offset = 350 - i * 50
        width = 80 - i * 20
        draw.arc([main_x-width, main_y-y_offset-20, main_x+width, main_y-y_offset+20], 
                start=0, end=180, fill=(255, 215, 0), width=3)
    
    # 主建筑表情
    draw_angry_bird_style_eyes(draw, main_x, main_y - 280, 30)
    draw_cute_smile(draw, main_x, main_y - 230, 18)
    
    # 顶部尖塔
    draw.rectangle([main_x-10, main_y-420, main_x+10, main_y-380], fill=(255, 215, 0), outline=(218, 165, 32), width=2)
    draw.polygon([(main_x-15, main_y-420), (main_x, main_y-450), (main_x+15, main_y-420)], fill=(255, 215, 0))
    
    # 两侧尖塔
    for x_offset in [-180, 180]:
        tower_x = main_x + x_offset
        # 塔身
        draw.rectangle([tower_x-25, main_y-300, tower_x+25, main_y], fill=blue_colors[1], outline=(0, 70, 100), width=2)
        # 塔身装饰条纹
        for i in range(5):
            y = main_y - 250 + i * 50
            draw.rectangle([tower_x-25, y, tower_x+25, y+20], fill=blue_colors[3], outline=(255, 255, 255), width=1)
        # 塔顶
        draw.polygon([(tower_x-30, main_y-300), (tower_x, main_y-360), (tower_x+30, main_y-300)], fill=(255, 215, 0))
        draw.ellipse([tower_x-8, main_y-375, tower_x+8, main_y-355], fill=(255, 215, 0))
        # 塔的表情
        draw_angry_bird_style_eyes(draw, tower_x, main_y - 200, 15)
    
    # 拱门
    draw.arc([main_x-60, main_y-120, main_x+60, main_y], start=0, end=180, fill=(139, 90, 43), width=5)
    
    # 标题
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 36)
    except:
        font = ImageFont.load_default()
    draw.text((WIDTH//2-200, 40), "Imam Square", fill=(255, 255, 255), font=font, stroke_width=2, stroke_fill=(0, 0, 0))
    draw.text((WIDTH//2-80, 90), "Iran", fill=(255, 255, 200), font=font, stroke_width=2, stroke_fill=(0, 0, 0))
    
    return img

# ==================== 7. 哈萨克斯坦 - 草原 ====================
def create_steppe():
    img = Image.new('RGB', (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(img)
    create_gradient_background(draw, WIDTH, HEIGHT)
    
    # 太阳
    draw_sun(draw, 680, 130, 50)
    
    # 云朵
    draw_cloud(draw, 200, 160, 55)
    draw_cloud(draw, 450, 120, 45)
    
    # 地面 - 草原绿色
    draw.rectangle([0, 750, WIDTH, HEIGHT], fill=(124, 180, 100), outline=(100, 150, 80), width=3)
    # 草地波浪纹理
    for i in range(0, WIDTH, 25):
        height_var = 30 + (i % 40)
        draw.line([(i, 750), (i, 750-height_var)], fill=(85, 140, 65), width=3)
    
    # 远处的山丘
    draw.polygon([(0, 750), (150, 600), (350, 680), (550, 580), (800, 750)], 
                 fill=(144, 180, 120), outline=(120, 150, 100), width=2)
    
    # 蒙古包 (毡房) - 带表情
    yurt_x, yurt_y = 300, 750
    
    # 蒙古包主体 - 圆形
    draw.ellipse([yurt_x-100, yurt_y-120, yurt_x+100, yurt_y], fill=(245, 222, 179), outline=(210, 180, 140), width=4)
    
    # 蒙古包顶部
    yurt_top_points = [(yurt_x-60, yurt_y-120), (yurt_x, yurt_y-200), (yurt_x+60, yurt_y-120)]
    draw.polygon(yurt_top_points, fill=(245, 222, 179), outline=(210, 180, 140), width=3)
    
    # 顶部圆环
    draw.ellipse([yurt_x-25, yurt_y-210, yurt_x+25, yurt_y-165], fill=(139, 69, 19), outline=(100, 50, 0), width=2)
    
    # 蒙古包装饰条纹
    stripe_colors = [(200, 50, 50), (50, 100, 150), (200, 150, 50), (150, 50, 150)]
    for i, color in enumerate(stripe_colors):
        y_pos = yurt_y - 100 + i * 25
        draw.arc([yurt_x-95+i*5, y_pos-20, yurt_x+95-i*5, y_pos+20], start=0, end=180, fill=color, width=4)
    
    # 蒙古包门
    draw.rectangle([yurt_x-30, yurt_y-60, yurt_x+30, yurt_y], fill=(139, 69, 19), outline=(100, 50, 0), width=3)
    draw.ellipse([yurt_x-30, yurt_y-90, yurt_x+30, yurt_y-30], fill=(139, 69, 19), outline=(100, 50, 0), width=3)
    
    # 蒙古包表情
    draw_angry_bird_style_eyes(draw, yurt_x, yurt_y - 150, 22)
    draw_cute_smile(draw, yurt_x, yurt_y - 115, 14)
    
    # 第二个小蒙古包
    yurt2_x, yurt2_y = 580, 780
    draw.ellipse([yurt2_x-60, yurt2_y-70, yurt2_x+60, yurt2_y], fill=(255, 228, 196), outline=(210, 180, 140), width=3)
    yurt2_top = [(yurt2_x-35, yurt2_y-70), (yurt2_x, yurt2_y-120), (yurt2_x+35, yurt2_y-70)]
    draw.polygon(yurt2_top, fill=(255, 228, 196), outline=(210, 180, 140), width=2)
    draw.ellipse([yurt2_x-15, yurt2_y-125, yurt2_x+15, yurt2_y-100], fill=(139, 69, 19), outline=(100, 50, 0), width=2)
    # 装饰
    draw.arc([yurt2_x-55, yurt2_y-60, yurt2_x+55, yurt2_y-40], start=0, end=180, fill=(200, 100, 100), width=3)
    draw.arc([yurt2_x-50, yurt2_y-40, yurt2_x+50, yurt2_y-20], start=0, end=180, fill=(100, 150, 200), width=3)
    draw_angry_bird_style_eyes(draw, yurt2_x, yurt2_y - 90, 14)
    
    # 马 - 卡通风格
    horse_x, horse_y = 480, 730
    # 身体
    draw.ellipse([horse_x, horse_y-30, horse_x+80, horse_y+20], fill=(160, 120, 80), outline=(130, 90, 50), width=2)
    # 脖子
    draw.polygon([(horse_x+60, horse_y-20), (horse_x+90, horse_y-60), (horse_x+100, horse_y-10)], 
                 fill=(160, 120, 80), outline=(130, 90, 50), width=2)
    # 头
    draw.ellipse([horse_x+80, horse_y-70, horse_x+120, horse_y-40], fill=(160, 120, 80), outline=(130, 90, 50), width=2)
    # 耳朵
    draw.polygon([(horse_x+85, horse_y-70), (horse_x+90, horse_y-85), (horse_x+95, horse_y-70)], fill=(160, 120, 80))
    draw.polygon([(horse_x+95, horse_y-70), (horse_x+100, horse_y-80), (horse_x+105, horse_y-70)], fill=(160, 120, 80))
    # 腿
    for i, x_off in enumerate([10, 25, 50, 65]):
        draw.rectangle([horse_x+x_off, horse_y+10, horse_x+x_off+12, horse_y+50], fill=(160, 120, 80), outline=(130, 90, 50), width=2)
    # 马尾
    draw.ellipse([horse_x-15, horse_y-20, horse_x+5, horse_y+10], fill=(130, 90, 50), outline=(100, 70, 30), width=2)
    # 马眼
    draw_angry_bird_style_eyes(draw, horse_x+100, horse_y-55, 8)
    
    # 标题
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 40)
    except:
        font = ImageFont.load_default()
    draw.text((WIDTH//2-120, 50), "Steppe", fill=(255, 255, 255), font=font, stroke_width=2, stroke_fill=(0, 0, 0))
    draw.text((WIDTH//2-200, 100), "Kazakhstan", fill=(255, 255, 200), font=font, stroke_width=2, stroke_fill=(0, 0, 0))
    
    return img

# ==================== 主函数 ====================
def main():
    output_dir = "/Users/moutai/Desktop/toweroffate_v1.0/assets/towers/"
    
    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)
    
    # 定义要生成的图片
    towers = [
        ("chefchaouen.png", create_chefchaouen, "摩洛哥 - 舍夫沙万"),
        ("kilimanjaro.png", create_kilimanjaro, "肯尼亚 - 乞力马扎罗山"),
        ("serengeti.png", create_serengeti, "坦桑尼亚 - 塞伦盖蒂"),
        ("jerusalem.png", create_jerusalem, "以色列 - 耶路撒冷"),
        ("petra.png", create_petra, "约旦 - 佩特拉"),
        ("imam-square.png", create_imam_square, "伊朗 - 伊玛目广场"),
        ("steppe.png", create_steppe, "哈萨克斯坦 - 草原"),
    ]
    
    print("开始生成卡通风格地标图片...")
    print("=" * 50)
    
    for filename, create_func, name in towers:
        print(f"正在生成: {name} -> {filename}")
        try:
            img = create_func()
            filepath = os.path.join(output_dir, filename)
            img.save(filepath, "PNG", quality=95)
            print(f"  ✓ 已保存: {filepath}")
        except Exception as e:
            print(f"  ✗ 错误: {e}")
    
    print("=" * 50)
    print("生成完成!")
    print(f"图片保存在: {output_dir}")

if __name__ == "__main__":
    main()
