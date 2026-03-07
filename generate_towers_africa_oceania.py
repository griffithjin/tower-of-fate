from PIL import Image, ImageDraw, ImageFilter
import math
import os

# 输出目录
OUTPUT_DIR = "/Users/moutai/Desktop/toweroffate_v1.0/assets/towers/"

# 图片规格
WIDTH, HEIGHT = 800, 1200

# 愤怒的小鸟风格配色
COLORS = {
    'sky_top': (135, 206, 235),      # 天蓝色顶部
    'sky_bottom': (200, 230, 255),   # 浅天蓝色底部
    'skin': (255, 200, 150),         # 肤色
    'skin_dark': (230, 170, 120),    # 深色皮肤
    'eye_white': (255, 255, 255),    # 眼白
    'eye_black': (30, 30, 30),       # 瞳孔
    'beak': (255, 165, 0),           # 橙色嘴巴
    'beak_dark': (220, 130, 0),      # 深橙色
    'brown': (139, 90, 43),          # 棕色
    'brown_dark': (101, 67, 33),     # 深棕色
    'green': (107, 142, 35),         # 绿色
    'green_light': (154, 205, 50),   # 浅绿色
    'green_dark': (85, 107, 47),     # 深绿色
    'stone': (169, 169, 169),        # 石头灰
    'stone_dark': (128, 128, 128),   # 深灰色
    'sand': (238, 214, 175),         # 沙色
    'water': (64, 164, 223),         # 水蓝
    'water_light': (135, 206, 250),  # 浅水蓝
    'lava': (255, 69, 0),            # 岩浆红
    'lava_dark': (178, 34, 34),      # 深红
    'yellow': (255, 223, 0),         # 黄色
    'pink': (255, 182, 193),         # 粉色
    'red': (220, 20, 60),            # 红色
    'white': (255, 255, 255),
    'black': (30, 30, 30),
    'purple': (138, 43, 226),        # 紫色
    'orange': (255, 140, 0),         # 橙色
}

def create_gradient_background(width, height):
    """创建天蓝色渐变背景"""
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    
    for y in range(height):
        ratio = y / height
        r = int(COLORS['sky_top'][0] + (COLORS['sky_bottom'][0] - COLORS['sky_top'][0]) * ratio)
        g = int(COLORS['sky_top'][1] + (COLORS['sky_bottom'][1] - COLORS['sky_top'][1]) * ratio)
        b = int(COLORS['sky_top'][2] + (COLORS['sky_bottom'][2] - COLORS['sky_top'][2]) * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    return img

def draw_circle(draw, center, radius, color, outline=None, outline_width=2):
    """画圆形"""
    x, y = center
    draw.ellipse([x-radius, y-radius, x+radius, y+radius], fill=color, outline=outline, width=outline_width)

def draw_angry_eyes(draw, cx, cy, size=40, angry_level=0.3):
    """画愤怒的小鸟风格眼睛"""
    # 眉毛（愤怒表情）
    brow_y = cy - size * 0.6
    brow_offset = size * 0.4
    draw.polygon([
        (cx - size*0.8, brow_y - size*0.3),
        (cx - size*0.2, brow_y + size*0.1),
        (cx + size*0.2, brow_y + size*0.1),
        (cx + size*0.8, brow_y - size*0.3),
        (cx + size*0.8, brow_y + size*0.2),
        (cx + size*0.2, brow_y + size*0.4),
        (cx - size*0.2, brow_y + size*0.4),
        (cx - size*0.8, brow_y + size*0.2),
    ], fill=COLORS['black'])
    
    # 左眼白
    draw_circle(draw, (cx - size*0.5, cy), size*0.45, COLORS['eye_white'], COLORS['black'], 2)
    # 右眼白
    draw_circle(draw, (cx + size*0.5, cy), size*0.45, COLORS['eye_white'], COLORS['black'], 2)
    
    # 左瞳孔
    draw_circle(draw, (cx - size*0.5, cy), size*0.25, COLORS['eye_black'])
    # 右瞳孔
    draw_circle(draw, (cx + size*0.5, cy), size*0.25, COLORS['eye_black'])
    
    # 高光
    draw_circle(draw, (cx - size*0.6, cy - size*0.2), size*0.08, COLORS['white'])
    draw_circle(draw, (cx + size*0.4, cy - size*0.2), size*0.08, COLORS['white'])

def draw_beak(draw, cx, cy, size=30):
    """画橙色尖嘴"""
    # 上嘴
    draw.polygon([
        (cx, cy - size*0.3),
        (cx + size*0.9, cy + size*0.2),
        (cx, cy + size*0.5),
    ], fill=COLORS['beak'], outline=COLORS['beak_dark'])
    # 下嘴
    draw.polygon([
        (cx, cy + size*0.5),
        (cx + size*0.7, cy + size*0.4),
        (cx, cy + size*0.9),
    ], fill=COLORS['beak_dark'], outline=COLORS['brown'])

def draw_cute_mouth(draw, cx, cy, size=20):
    """画可爱的微笑嘴"""
    draw.arc([cx-size, cy, cx+size, cy+size], 0, 180, fill=COLORS['black'], width=3)

def draw_angry_bird_face(draw, cx, cy, size=80, color=COLORS['red']):
    """画愤怒的小鸟风格的脸"""
    # 主体圆形
    draw_circle(draw, (cx, cy), size, color, COLORS['black'], 3)
    
    # 肚子（浅色）
    belly_y = cy + size * 0.4
    draw.ellipse([cx-size*0.7, belly_y-size*0.5, cx+size*0.7, belly_y+size*0.6], 
                 fill=(255, 220, 180))
    
    # 眼睛
    draw_angry_eyes(draw, cx, cy - size*0.1, size*0.6)
    
    # 嘴巴
    draw_beak(draw, cx, cy + size*0.2, size*0.5)
    
    # 头顶羽毛
    draw.polygon([
        (cx - size*0.3, cy - size*0.8),
        (cx, cy - size*1.2),
        (cx + size*0.3, cy - size*0.8),
    ], fill=COLORS['black'])

def add_clouds(draw, width, height):
    """添加卡通云朵"""
    clouds = [
        (150, 150, 80),
        (600, 200, 100),
        (400, 100, 60),
        (700, 350, 70),
        (100, 400, 65),
    ]
    for x, y, r in clouds:
        draw_circle(draw, (x, y), r, COLORS['white'])
        draw_circle(draw, (x-r*0.5, y+r*0.2), r*0.7, COLORS['white'])
        draw_circle(draw, (x+r*0.5, y+r*0.2), r*0.7, COLORS['white'])
        draw_circle(draw, (x, y+r*0.4), r*0.6, COLORS['white'])

# ============ 1. 埃塞俄比亚 - 岩石教堂 ============
def create_lalibela():
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    add_clouds(draw, WIDTH, HEIGHT)
    
    cx, cy = WIDTH // 2, HEIGHT // 2 + 100
    
    # 岩石基座
    draw.polygon([
        (cx - 300, cy + 300),
        (cx + 300, cy + 300),
        (cx + 350, cy + 450),
        (cx - 350, cy + 450),
    ], fill=COLORS['stone'], outline=COLORS['stone_dark'], width=3)
    
    # 岩石纹理
    for i in range(5):
        x = cx - 250 + i * 120
        draw.polygon([
            (x, cy + 320),
            (x + 40, cy + 300),
            (x + 80, cy + 340),
        ], fill=COLORS['stone_dark'])
    
    # 教堂主体 - 十字形
    cross_size = 120
    # 竖条
    draw.rectangle([cx - 60, cy - 200, cx + 60, cy + 300], 
                   fill=COLORS['stone'], outline=COLORS['stone_dark'], width=4)
    # 横条
    draw.rectangle([cx - 180, cy - 80, cx + 180, cy + 80], 
                   fill=COLORS['stone'], outline=COLORS['stone_dark'], width=4)
    
    # 教堂窗户（卡通风格）
    window_color = (80, 80, 100)
    for wx, wy in [(cx - 30, cy - 150), (cx + 30, cy - 150), 
                   (cx - 30, cy + 50), (cx + 30, cy + 50),
                   (cx - 120, cy - 30), (cx + 120, cy - 30)]:
        draw.arc([wx-25, wy-35, wx+25, wy+35], 0, 180, fill=window_color, width=8)
    
    # 教堂顶部圆顶
    draw_circle(draw, (cx, cy - 200), 70, COLORS['stone'], COLORS['stone_dark'], 3)
    # 十字架
    draw.rectangle([cx - 10, cy - 300, cx + 10, cy - 180], fill=COLORS['yellow'])
    draw.rectangle([cx - 35, cy - 250, cx + 35, cy - 230], fill=COLORS['yellow'])
    
    # 给教堂加愤怒小鸟脸
    draw_angry_eyes(draw, cx, cy - 30, 35)
    draw_beak(draw, cx, cy + 10, 25)
    
    # 装饰性柱子
    for px in [cx - 140, cx + 140]:
        draw.rectangle([px - 20, cy + 80, px + 20, cy + 280], 
                       fill=COLORS['stone'], outline=COLORS['stone_dark'], width=2)
    
    # 底部草地
    draw.polygon([
        (0, HEIGHT - 100),
        (WIDTH, HEIGHT - 100),
        (WIDTH, HEIGHT),
        (0, HEIGHT),
    ], fill=COLORS['green'])
    
    return img

# ============ 2. 赞比亚 - 维多利亚瀑布 ============
def create_victoria_falls():
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    add_clouds(draw, WIDTH, HEIGHT)
    
    # 瀑布背景悬崖
    draw.polygon([
        (0, 0),
        (300, 0),
        (350, 400),
        (200, 500),
        (0, 450),
    ], fill=COLORS['green'], outline=COLORS['green_dark'], width=3)
    
    draw.polygon([
        (WIDTH, 0),
        (500, 0),
        (450, 400),
        (600, 500),
        (WIDTH, 450),
    ], fill=COLORS['green'], outline=COLORS['green_dark'], width=3)
    
    # 瀑布水流（多层）
    for layer in range(5):
        y_start = 300 + layer * 80
        alpha = 255 - layer * 30
        water_color = (135, 206, 250)
        # 左瀑布
        for i in range(15):
            x = 320 + i * 8
            wave = math.sin(i * 0.5 + layer) * 10
            draw.line([(x, y_start), (x + wave, y_start + 100 + layer*50)], 
                     fill=water_color, width=6)
        # 右瀑布
        for i in range(15):
            x = 430 + i * 8
            wave = math.sin(i * 0.5 + layer + 2) * 10
            draw.line([(x, y_start), (x + wave, y_start + 100 + layer*50)], 
                     fill=water_color, width=6)
    
    # 瀑布底部水雾（圆形装饰）
    for i in range(8):
        x = 300 + i * 30
        y = 700 + (i % 3) * 20
        size = 20 + (i % 4) * 10
        draw_circle(draw, (x, y), size, COLORS['white'])
    
    # 中心瀑布脸（卡通化）
    cx, cy = WIDTH // 2, 500
    # 水帘后的岩石脸
    draw_circle(draw, (cx, cy), 100, COLORS['stone'], COLORS['stone_dark'], 3)
    draw_angry_eyes(draw, cx, cy - 20, 45)
    draw_beak(draw, cx, cy + 30, 35)
    
    # 底部河流
    draw.polygon([
        (0, HEIGHT - 150),
        (WIDTH, HEIGHT - 150),
        (WIDTH, HEIGHT),
        (0, HEIGHT),
    ], fill=COLORS['water'])
    
    # 河流水纹
    for i in range(10):
        y = HEIGHT - 120 + i * 10
        draw.line([(100, y), (300, y)], fill=COLORS['water_light'], width=3)
        draw.line([(500, y), (700, y)], fill=COLORS['water_light'], width=3)
    
    return img

# ============ 3. 毛里求斯 - 莫纳山 ============
def create_le_morne():
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    add_clouds(draw, WIDTH, HEIGHT)
    
    cx, cy = WIDTH // 2, HEIGHT // 2 + 50
    
    # 山体（陡峭的山峰形状）
    mountain_points = [
        (cx - 250, HEIGHT - 100),  # 左下
        (cx - 100, cy + 100),      # 左中
        (cx - 50, cy - 50),        # 左肩
        (cx, cy - 300),            # 山顶
        (cx + 50, cy - 50),        # 右肩
        (cx + 100, cy + 100),      # 右中
        (cx + 250, HEIGHT - 100),  # 右下
    ]
    draw.polygon(mountain_points, fill=COLORS['green'], outline=COLORS['green_dark'], width=4)
    
    # 山顶岩石区域
    draw.polygon([
        (cx - 40, cy - 200),
        (cx, cy - 300),
        (cx + 40, cy - 200),
        (cx + 30, cy - 150),
        (cx - 30, cy - 150),
    ], fill=COLORS['stone'], outline=COLORS['stone_dark'], width=2)
    
    # 山体纹理（植被层）
    for i in range(6):
        y = cy - 100 + i * 60
        width = 200 - i * 25
        draw.arc([cx - width, y, cx + width, y + 80], 0, 180, 
                fill=COLORS['green_dark'], width=3)
    
    # 山的脸
    draw_angry_eyes(draw, cx, cy - 80, 50)
    draw_beak(draw, cx, cy - 20, 40)
    
    # 山腰云朵（莫纳山著名的云海）
    for i in range(5):
        x = cx - 200 + i * 100
        y = cy + 50 + (i % 2) * 30
        draw_circle(draw, (x, y), 40, COLORS['white'])
        draw_circle(draw, (x - 25, y + 10), 30, COLORS['white'])
        draw_circle(draw, (x + 25, y + 10), 30, COLORS['white'])
    
    # 底部海水
    draw.polygon([
        (0, HEIGHT - 100),
        (WIDTH, HEIGHT - 100),
        (WIDTH, HEIGHT),
        (0, HEIGHT),
    ], fill=(0, 150, 200))
    
    # 海浪
    for i in range(12):
        x = i * 70
        y = HEIGHT - 80
        draw.arc([x, y, x + 50, y + 30], 0, 180, fill=COLORS['white'], width=3)
    
    return img

# ============ 4. 马达加斯加 - 猴面包树 ============
def create_baobab():
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    add_clouds(draw, WIDTH, HEIGHT)
    
    cx, cy = WIDTH // 2, HEIGHT - 150
    
    # 树干（超级粗大的圆柱形）
    trunk_width = 180
    trunk_height = 400
    
    # 树干主体
    draw.polygon([
        (cx - trunk_width*0.6, cy - trunk_height),
        (cx + trunk_width*0.6, cy - trunk_height),
        (cx + trunk_width*0.8, cy),
        (cx - trunk_width*0.8, cy),
    ], fill=COLORS['brown'], outline=COLORS['brown_dark'], width=4)
    
    # 树皮纹理（垂直条纹）
    for i in range(8):
        x = cx - trunk_width*0.5 + i * 45
        draw.line([(x, cy - trunk_height + 50), (x, cy - 50)], 
                 fill=COLORS['brown_dark'], width=4)
    
    # 树枝（向天空伸展）
    branches = [
        (cx - 150, cy - trunk_height - 100, -30),
        (cx - 80, cy - trunk_height - 150, -15),
        (cx, cy - trunk_height - 180, 0),
        (cx + 80, cy - trunk_height - 150, 15),
        (cx + 150, cy - trunk_height - 100, 30),
    ]
    
    for bx, by, angle in branches:
        # 树枝
        draw.polygon([
            (cx - 30, cy - trunk_height + 50),
            (cx + 30, cy - trunk_height + 50),
            (bx + 20, by),
            (bx - 20, by),
        ], fill=COLORS['brown'], outline=COLORS['brown_dark'], width=2)
        # 树枝末端小树冠
        draw_circle(draw, (bx, by), 50, COLORS['green'], COLORS['green_dark'], 2)
        draw_circle(draw, (bx - 20, by - 10), 30, COLORS['green_light'])
        draw_circle(draw, (bx + 20, by - 10), 30, COLORS['green_light'])
    
    # 树干上的脸
    draw_angry_eyes(draw, cx, cy - trunk_height*0.5, 55)
    draw_beak(draw, cx, cy - trunk_height*0.5 + 50, 45)
    
    # 根部突起
    for i in range(5):
        rx = cx - 120 + i * 60
        draw.polygon([
            (rx, cy - 50),
            (rx + 30, cy - 100),
            (rx + 50, cy),
            (rx - 20, cy),
        ], fill=COLORS['brown'], outline=COLORS['brown_dark'], width=2)
    
    # 底部草地
    draw.polygon([
        (0, HEIGHT - 100),
        (WIDTH, HEIGHT - 100),
        (WIDTH, HEIGHT),
        (0, HEIGHT),
    ], fill=COLORS['green'])
    
    # 远处的小猴面包树
    for sx, sy in [(100, HEIGHT - 80), (700, HEIGHT - 100)]:
        draw.polygon([
            (sx - 30, sy - 150),
            (sx + 30, sy - 150),
            (sx + 40, sy),
            (sx - 40, sy),
        ], fill=COLORS['brown'])
        draw_circle(draw, (sx, sy - 180), 40, COLORS['green'])
    
    return img

# ============ 5. 斐济 - 海滩棕榈树 ============
def create_fiji():
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    add_clouds(draw, WIDTH, HEIGHT)
    
    cx, cy = WIDTH // 2, HEIGHT - 100
    
    # 沙滩
    draw.polygon([
        (0, HEIGHT - 200),
        (WIDTH, HEIGHT - 250),
        (WIDTH, HEIGHT),
        (0, HEIGHT),
    ], fill=COLORS['sand'], outline=COLORS['brown'], width=2)
    
    # 海水
    draw.polygon([
        (0, HEIGHT - 200),
        (WIDTH, HEIGHT - 250),
        (WIDTH, HEIGHT - 400),
        (0, HEIGHT - 350),
    ], fill=(0, 180, 220))
    
    # 海浪线
    for i in range(3):
        y = HEIGHT - 280 - i * 50
        for x in range(0, WIDTH, 60):
            draw.arc([x, y, x + 40, y + 20], 0, 180, fill=COLORS['white'], width=3)
    
    # 椰子树树干（弯曲的）
    trunk_points = [
        (cx - 40, cy),
        (cx + 40, cy),
        (cx + 25, cy - 200),
        (cx - 15, cy - 250),
        (cx - 20, cy - 350),
        (cx - 50, cy - 400),
        (cx - 60, cy - 400),
        (cx - 50, cy - 350),
        (cx - 35, cy - 250),
        (cx - 35, cy - 200),
    ]
    draw.polygon(trunk_points, fill=COLORS['brown'], outline=COLORS['brown_dark'], width=3)
    
    # 树干纹理
    for y in range(int(cy - 350), int(cy), 40):
        draw.line([(cx - 35, y), (cx + 10, y)], fill=COLORS['brown_dark'], width=3)
    
    # 树叶（从顶部向四周伸展）
    tree_top_x, tree_top_y = cx - 55, cy - 400
    leaf_angles = [45, 90, 135, 180, 225, 270, 315, 0]
    
    for angle in leaf_angles:
        rad = math.radians(angle)
        leaf_len = 180
        end_x = tree_top_x + math.cos(rad) * leaf_len
        end_y = tree_top_y + math.sin(rad) * leaf_len * 0.5
        
        # 叶子形状
        mid_x = (tree_top_x + end_x) / 2
        mid_y = (tree_top_y + end_y) / 2
        ctrl_x = mid_x + math.cos(rad + 0.5) * 50
        ctrl_y = mid_y + math.sin(rad + 0.5) * 30
        
        draw.polygon([
            (tree_top_x, tree_top_y),
            (ctrl_x - 15, ctrl_y),
            (end_x, end_y),
            (ctrl_x + 15, ctrl_y),
        ], fill=COLORS['green'], outline=COLORS['green_dark'], width=2)
    
    # 椰子（在树干顶部）
    for i, (ox, oy) in enumerate([(cx - 70, cy - 380), (cx - 40, cy - 390), (cx - 80, cy - 360)]):
        draw_circle(draw, (ox, oy), 20, COLORS['brown'], COLORS['brown_dark'], 2)
        # 椰子脸
        if i == 0:
            draw_angry_eyes(draw, ox, oy - 5, 8)
    
    # 树干上的脸
    draw_angry_eyes(draw, cx - 20, cy - 150, 40)
    draw_beak(draw, cx - 20, cy - 110, 30)
    
    # 太阳
    draw_circle(draw, (700, 150), 60, COLORS['yellow'], COLORS['orange'], 3)
    for i in range(8):
        angle = math.radians(i * 45)
        x1 = 700 + math.cos(angle) * 75
        y1 = 150 + math.sin(angle) * 75
        x2 = 700 + math.cos(angle) * 95
        y2 = 150 + math.sin(angle) * 95
        draw.line([(x1, y1), (x2, y2)], fill=COLORS['yellow'], width=5)
    
    return img

# ============ 6. 巴布亚新几内亚 - 部落面具 ============
def create_png():
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    add_clouds(draw, WIDTH, HEIGHT)
    
    cx, cy = WIDTH // 2, HEIGHT // 2
    
    # 面具外框（椭圆形）
    mask_width, mask_height = 250, 350
    draw.ellipse([cx - mask_width, cy - mask_height, cx + mask_width, cy + mask_height],
                 fill=COLORS['brown'], outline=COLORS['brown_dark'], width=5)
    
    # 面具内部（稍小的椭圆）
    inner_w, inner_h = 200, 280
    draw.ellipse([cx - inner_w, cy - inner_h, cx + inner_w, cy + inner_h],
                 fill=(139, 90, 43), outline=COLORS['yellow'], width=4)
    
    # 额头装饰（三角形图案）
    for i in range(5):
        tx = cx - 150 + i * 75
        ty = cy - 200
        size = 25
        color = COLORS['red'] if i % 2 == 0 else COLORS['yellow']
        draw.polygon([
            (tx, ty - size),
            (tx - size, ty + size),
            (tx + size, ty + size),
        ], fill=color, outline=COLORS['black'], width=2)
    
    # 眼睛（大而圆的愤怒小鸟风格）
    eye_y = cy - 80
    eye_size = 60
    # 左眼框
    draw.ellipse([cx - 120, eye_y - eye_size, cx - 20, eye_y + eye_size],
                 fill=COLORS['white'], outline=COLORS['black'], width=4)
    # 右眼框
    draw.ellipse([cx + 20, eye_y - eye_size, cx + 120, eye_y + eye_size],
                 fill=COLORS['white'], outline=COLORS['black'], width=4)
    
    # 瞳孔（螺旋图案 - 部落风格）
    for ex in [cx - 70, cx + 70]:
        for r in [25, 15, 5]:
            color = COLORS['black'] if r > 10 else COLORS['red']
            draw.ellipse([ex - r, eye_y - r, ex + r, eye_y + r], fill=color)
    
    # 眉毛（粗壮的部落风格）
    draw.polygon([
        (cx - 130, eye_y - 80),
        (cx - 60, eye_y - 50),
        (cx + 60, eye_y - 50),
        (cx + 130, eye_y - 80),
        (cx + 110, eye_y - 40),
        (cx - 110, eye_y - 40),
    ], fill=COLORS['black'])
    
    # 鼻子（长而突出的形状）
    nose_points = [
        (cx - 30, cy - 20),
        (cx + 30, cy - 20),
        (cx + 20, cy + 120),
        (cx, cy + 150),
        (cx - 20, cy + 120),
    ]
    draw.polygon(nose_points, fill=COLORS['brown_dark'], outline=COLORS['black'], width=3)
    
    # 鼻孔
    draw.ellipse([cx - 15, cy + 80, cx - 5, cy + 100], fill=COLORS['black'])
    draw.ellipse([cx + 5, cy + 80, cx + 15, cy + 100], fill=COLORS['black'])
    
    # 嘴巴（宽而微笑）
    mouth_y = cy + 180
    draw.arc([cx - 100, mouth_y - 30, cx + 100, mouth_y + 50], 0, 180, 
            fill=COLORS['black'], width=6)
    
    # 獠牙/牙齿
    for i in range(4):
        tx = cx - 60 + i * 40
        draw.polygon([
            (tx, mouth_y + 20),
            (tx + 15, mouth_y + 70),
            (tx + 30, mouth_y + 20),
        ], fill=COLORS['white'], outline=COLORS['black'], width=2)
    
    # 脸颊装饰（圆形图案）
    for sx, sy in [(cx - 160, cy + 50), (cx + 160, cy + 50)]:
        for r, color in [(30, COLORS['yellow']), (20, COLORS['red']), (10, COLORS['white'])]:
            draw_circle(draw, (sx, sy), r, color)
    
    # 面具底部流苏/羽毛
    for i in range(9):
        fx = cx - 200 + i * 50
        fy = cy + 300
        feather_len = 80 + (i % 3) * 30
        color = COLORS['red'] if i % 3 == 0 else (COLORS['yellow'] if i % 3 == 1 else COLORS['white'])
        draw.polygon([
            (fx - 10, fy),
            (fx + 10, fy),
            (fx, fy + feather_len),
        ], fill=color, outline=COLORS['black'], width=2)
    
    return img

# ============ 7. 瓦努阿图 - 火山 ============
def create_vanuatu():
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    add_clouds(draw, WIDTH, HEIGHT)
    
    cx, cy = WIDTH // 2, HEIGHT - 100
    
    # 火山山体（圆锥形）
    mountain_height = 500
    draw.polygon([
        (cx - 280, cy),
        (cx - 100, cy - mountain_height * 0.6),
        (cx, cy - mountain_height),
        (cx + 100, cy - mountain_height * 0.6),
        (cx + 280, cy),
    ], fill=(80, 60, 50), outline=(50, 40, 35), width=4)
    
    # 火山纹理（熔岩流痕迹）
    for i in range(5):
        lava_x = cx - 150 + i * 75
        lava_y_start = cy - 200 - i * 50
        draw.polygon([
            (lava_x - 15, lava_y_start),
            (lava_x + 15, lava_y_start),
            (lava_x + 25, cy - 50),
            (lava_x - 25, cy - 50),
        ], fill=(100, 70, 60), outline=COLORS['lava_dark'], width=2)
    
    # 火山口
    crater_y = cy - mountain_height
    draw.ellipse([cx - 80, crater_y - 30, cx + 80, crater_y + 30], 
                fill=COLORS['lava_dark'], outline=(60, 40, 35), width=4)
    draw.ellipse([cx - 50, crater_y - 20, cx + 50, crater_y + 20], 
                fill=COLORS['lava'], outline=COLORS['yellow'], width=3)
    
    # 山体上的脸
    face_y = cy - mountain_height * 0.4
    draw_angry_eyes(draw, cx, face_y - 30, 50, angry_level=0.5)
    draw_beak(draw, cx, face_y + 20, 40)
    
    # 喷发的岩浆和火山灰
    for i in range(12):
        angle = math.radians(-60 - i * 5)
        dist = 100 + (i % 4) * 50
        px = cx + math.cos(angle) * dist
        py = crater_y + math.sin(angle) * dist * 0.5
        size = 15 + (i % 3) * 10
        color = COLORS['lava'] if i % 2 == 0 else COLORS['orange']
        draw_circle(draw, (px, py), size, color)
        # 拖尾
        draw.polygon([
            (px - size*0.5, py),
            (px + size*0.5, py),
            (cx, crater_y),
        ], fill=color)
    
    # 火山灰云
    ash_y = crater_y - 100
    for i in range(8):
        ax = cx - 200 + i * 60 + (i % 2) * 30
        ay = ash_y - (i % 4) * 30
        size = 50 + (i % 3) * 20
        gray = 100 - i * 5
        draw_circle(draw, (ax, ay), size, (gray, gray, gray))
    
    # 底部熔岩河
    draw.polygon([
        (cx - 60, cy - 50),
        (cx + 60, cy - 50),
        (cx + 120, HEIGHT),
        (cx - 120, HEIGHT),
    ], fill=COLORS['lava'], outline=COLORS['lava_dark'], width=3)
    
    # 熔岩发光效果
    for i in range(5):
        lx = cx - 50 + i * 25
        ly = cy + i * 40
        draw_circle(draw, (lx, ly), 15, COLORS['yellow'])
    
    # 底部岩石地
    draw.polygon([
        (0, HEIGHT - 80),
        (WIDTH, HEIGHT - 80),
        (WIDTH, HEIGHT),
        (0, HEIGHT),
    ], fill=(60, 50, 45))
    
    return img

# ============ 主程序 ============
def main():
    towers = [
        ("lalibela.png", create_lalibela, "埃塞俄比亚 - 岩石教堂"),
        ("victoria-falls.png", create_victoria_falls, "赞比亚 - 维多利亚瀑布"),
        ("le-morne.png", create_le_morne, "毛里求斯 - 莫纳山"),
        ("baobab.png", create_baobab, "马达加斯加 - 猴面包树"),
        ("fiji.png", create_fiji, "斐济 - 海滩棕榈树"),
        ("png.png", create_png, "巴布亚新几内亚 - 部落面具"),
        ("vanuatu.png", create_vanuatu, "瓦努阿图 - 火山"),
    ]
    
    for filename, create_func, name in towers:
        filepath = os.path.join(OUTPUT_DIR, filename)
        print(f"正在生成: {name} -> {filename}")
        img = create_func()
        img.save(filepath, "PNG")
        print(f"  ✓ 已保存: {filepath}")
    
    print("\n全部7个塔图片生成完成！")

if __name__ == "__main__":
    main()
