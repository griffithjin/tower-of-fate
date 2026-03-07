#!/usr/bin/env python3
"""
生成法国大区卡通塔图片
风格：愤怒的小鸟卡通风格，可爱表情
尺寸：800x1200像素
背景：天蓝色渐变
"""

from PIL import Image, ImageDraw, ImageFilter
import math
import os

# 输出目录
OUTPUT_DIR = "/Users/moutai/Desktop/toweroffate_v1.0/assets/towers/states/france/"

# 确保输出目录存在
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 图片尺寸
WIDTH = 800
HEIGHT = 1200

def create_gradient_background(width, height):
    """创建天蓝色渐变背景"""
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    
    # 天蓝色渐变：从上到下，从浅蓝到稍深的天蓝
    for y in range(height):
        # 计算渐变色
        ratio = y / height
        r = int(135 - ratio * 30)  # 从135降到105
        g = int(206 - ratio * 30)  # 从206降到176
        b = int(235 - ratio * 10)  # 从235降到225
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    return img

def draw_rounded_rect(draw, xy, radius, fill, outline=None, width=1):
    """绘制圆角矩形"""
    x1, y1, x2, y2 = xy
    # 四个角的圆弧
    draw.pieslice([x1, y1, x1 + radius*2, y1 + radius*2], 180, 270, fill=fill)
    draw.pieslice([x2 - radius*2, y1, x2, y1 + radius*2], 270, 360, fill=fill)
    draw.pieslice([x1, y2 - radius*2, x1 + radius*2, y2], 90, 180, fill=fill)
    draw.pieslice([x2 - radius*2, y2 - radius*2, x2, y2], 0, 90, fill=fill)
    # 矩形主体
    draw.rectangle([x1 + radius, y1, x2 - radius, y2], fill=fill)
    draw.rectangle([x1, y1 + radius, x2, y2 - radius], fill=fill)
    # 中心填充
    draw.rectangle([x1 + radius, y1 + radius, x2 - radius, y2 - radius], fill=fill)

def draw_cute_eyes(draw, cx, cy, size=30):
    """绘制可爱的卡通眼睛"""
    # 左眼白
    draw.ellipse([cx - size - 15, cy - size//2, cx - 15, cy + size//2], fill=(255, 255, 255), outline=(0, 0, 0), width=2)
    # 右眼白
    draw.ellipse([cx + 15, cy - size//2, cx + size + 15, cy + size//2], fill=(255, 255, 255), outline=(0, 0, 0), width=2)
    # 左瞳孔（向上看显得可爱）
    pupil_size = max(5, size//3)
    draw.ellipse([cx - size//2 - 15, cy - size//3, cx - size//2 - 15 + pupil_size, cy - size//3 + pupil_size], fill=(0, 0, 0))
    # 右瞳孔
    draw.ellipse([cx + 20, cy - size//3, cx + 20 + pupil_size, cy - size//3 + pupil_size], fill=(0, 0, 0))
    # 高光
    highlight_size = max(3, size//8)
    draw.ellipse([cx - size//3 - 15, cy - size//4, cx - size//3 - 15 + highlight_size, cy - size//4 + highlight_size], fill=(255, 255, 255))
    draw.ellipse([cx + 25, cy - size//4, cx + 25 + highlight_size, cy - size//4 + highlight_size], fill=(255, 255, 255))

def draw_cute_mouth(draw, cx, cy, size=20):
    """绘制可爱的微笑嘴巴"""
    # 微笑弧线
    draw.arc([cx - size, cy, cx + size, cy + size], 0, 180, fill=(0, 0, 0), width=3)
    # 腮红
    draw.ellipse([cx - size - 30, cy, cx - size - 10, cy + 15], fill=(255, 182, 193, 128))
    draw.ellipse([cx + size + 10, cy, cx + size + 30, cy + 15], fill=(255, 182, 193, 128))

def draw_tower_base(img, draw, base_color, accent_color):
    """绘制塔的基础结构"""
    # 塔身主体（愤怒的小鸟风格 - 圆润的石头/木头块堆叠）
    tower_width = 300
    tower_height = 500
    tower_x = (WIDTH - tower_width) // 2
    tower_y = HEIGHT - 150 - tower_height
    
    # 底部阴影
    draw.ellipse([tower_x - 20, HEIGHT - 180, tower_x + tower_width + 20, HEIGHT - 130], 
                 fill=(0, 0, 0, 50))
    
    # 塔身（三层结构）
    layer_height = tower_height // 3
    
    for i in range(3):
        layer_y = tower_y + i * layer_height
        layer_width = tower_width - i * 30
        layer_x = (WIDTH - layer_width) // 2
        
        # 圆角矩形块
        radius = 20
        # 主体颜色
        r, g, b = base_color
        shadow_color = (max(0, r-30), max(0, g-30), max(0, b-30))
        
        # 阴影层
        draw_rounded_rect(draw, [layer_x + 5, layer_y + 5, layer_x + layer_width + 5, layer_y + layer_height - 10], 
                          radius, shadow_color)
        # 主体层
        draw_rounded_rect(draw, [layer_x, layer_y, layer_x + layer_width, layer_y + layer_height - 15], 
                          radius, base_color)
        
        # 装饰线条
        draw.line([layer_x + 20, layer_y + layer_height//2, layer_x + layer_width - 20, layer_y + layer_height//2], 
                  fill=accent_color, width=3)
    
    return tower_y, tower_width

def add_cute_face(img, draw, center_y, tower_width):
    """在塔上添加可爱表情"""
    cx = WIDTH // 2
    cy = center_y + 100
    
    draw_cute_eyes(draw, cx, cy, 35)
    draw_cute_mouth(draw, cx, cy + 40, 25)

def draw_pyramid(draw, x, y, width, height, color):
    """绘制金字塔形状"""
    points = [
        (x, y + height),  # 左下
        (x + width//2, y),  # 顶点
        (x + width, y + height),  # 右下
    ]
    draw.polygon(points, fill=color, outline=(0, 0, 0), width=2)
    
    # 侧面阴影
    shadow_points = [
        (x + width//2, y),
        (x + width, y + height),
        (x + width - width//4, y + height),
        (x + width//2 - 10, y + height//4),
    ]
    r, g, b = color
    shadow = (max(0, r-40), max(0, g-40), max(0, b-40))
    draw.polygon(shadow_points, fill=shadow)

def draw_castle_tower(draw, x, y, width, height, color):
    """绘制城堡塔楼"""
    # 塔身
    tower_color = color
    r, g, b = color
    shadow = (max(0, r-30), max(0, g-30), max(0, b-30))
    
    # 主体
    draw.rectangle([x, y + 30, x + width, y + height], fill=tower_color, outline=(0,0,0), width=2)
    # 顶部装饰
    crenellation_width = width // 4
    for i in range(4):
        cx = x + i * crenellation_width
        draw.rectangle([cx, y, cx + crenellation_width - 5, y + 30], 
                      fill=tower_color, outline=(0,0,0), width=2)
    
    # 屋顶
    roof_points = [(x - 10, y), (x + width//2, y - 40), (x + width + 10, y)]
    draw.polygon(roof_points, fill=shadow, outline=(0,0,0), width=2)

def generate_ile_de_france():
    """1. 法兰西岛 - 卢浮宫"""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    
    base_color = (210, 180, 140)  # 沙石色
    accent_color = (139, 90, 43)
    
    # 金字塔
    pyramid_size = 200
    pyramid_x = (WIDTH - pyramid_size) // 2
    pyramid_y = HEIGHT - 350
    draw_pyramid(draw, pyramid_x, pyramid_y, pyramid_size, 150, (218, 165, 32))
    
    # 玻璃金字塔效果
    for i in range(5):
        offset = i * 20
        draw.polygon([
            (pyramid_x + offset, pyramid_y + 150 - offset),
            (pyramid_x + pyramid_size//2, pyramid_y + offset),
            (pyramid_x + pyramid_size - offset, pyramid_y + 150 - offset),
        ], outline=(100, 149, 237), width=1)
    
    # 宫殿背景
    draw.rectangle([150, HEIGHT - 400, 650, HEIGHT - 200], fill=(245, 222, 179), outline=(139, 90, 43), width=3)
    
    # 可爱的眼睛和表情
    draw_cute_eyes(draw, WIDTH//2, HEIGHT - 320, 30)
    draw_cute_mouth(draw, WIDTH//2, HEIGHT - 280, 20)
    
    # 标题
    draw.text((WIDTH//2 - 80, 100), "Île-de-France", fill=(0, 0, 100), font=None)
    draw.text((WIDTH//2 - 60, 140), "Le Louvre", fill=(100, 50, 0), font=None)
    
    img.save(f"{OUTPUT_DIR}ile-de-france-louvre.png")
    print("✓ Generated: ile-de-france-louvre.png")

def generate_provence():
    """2. 普罗旺斯 - 薰衣草田"""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    
    # 薰衣草田（紫色波浪）
    for row in range(8):
        y = HEIGHT - 300 + row * 25
        for i in range(20):
            x = 50 + i * 35
            # 薰衣草花束
            flower_color = (138 + (i*3)%40, 43 + (row*5)%30, 226 - (i*2)%40)
            draw.ellipse([x, y, x + 20, y + 35], fill=flower_color, outline=(100, 0, 150), width=1)
            # 茎
            draw.line([x + 10, y + 35, x + 10, y + 50], fill=(34, 139, 34), width=2)
    
    # 普罗旺斯风格的塔
    tower_color = (255, 228, 196)  # 米色石塔
    draw.rectangle([300, HEIGHT - 500, 500, HEIGHT - 250], fill=tower_color, outline=(139, 90, 43), width=3)
    # 圆锥形屋顶
    roof_points = [(280, HEIGHT - 500), (400, HEIGHT - 620), (520, HEIGHT - 500)]
    draw.polygon(roof_points, fill=(205, 92, 92), outline=(139, 0, 0), width=3)
    
    # 窗户
    draw.ellipse([360, HEIGHT - 450, 440, HEIGHT - 380], fill=(135, 206, 235), outline=(0, 0, 100), width=2)
    
    # 可爱的表情
    draw_cute_eyes(draw, 400, HEIGHT - 420, 35)
    draw_cute_mouth(draw, 400, HEIGHT - 370, 25)
    
    # 标题
    draw.text((WIDTH//2 - 70, 100), "Provence", fill=(138, 43, 226), font=None)
    
    img.save(f"{OUTPUT_DIR}provence-lavender.png")
    print("✓ Generated: provence-lavender.png")

def generate_alps():
    """3. 阿尔卑斯 - 霞慕尼"""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    
    # 雪山背景
    mountain_points = [
        (0, HEIGHT - 200),
        (200, HEIGHT - 550),
        (400, HEIGHT - 700),  # 主峰
        (600, HEIGHT - 550),
        (WIDTH, HEIGHT - 200),
    ]
    draw.polygon(mountain_points, fill=(240, 248, 255), outline=(176, 196, 222), width=2)
    
    # 山顶积雪
    snow_points = [
        (280, HEIGHT - 620),
        (400, HEIGHT - 700),
        (520, HEIGHT - 620),
        (400, HEIGHT - 580),
    ]
    draw.polygon(snow_points, fill=(255, 255, 255), outline=(200, 200, 220), width=2)
    
    # 滑雪缆车塔
    tower_color = (139, 69, 19)
    # 塔架
    draw.rectangle([350, HEIGHT - 350, 370, HEIGHT - 200], fill=tower_color, outline=(0, 0, 0), width=2)
    draw.rectangle([430, HEIGHT - 350, 450, HEIGHT - 200], fill=tower_color, outline=(0, 0, 0), width=2)
    # 横梁
    for y in [HEIGHT - 320, HEIGHT - 280, HEIGHT - 240]:
        draw.rectangle([350, y, 450, y + 10], fill=tower_color, outline=(0, 0, 0), width=2)
    
    # 可爱的表情（在塔上）
    draw_cute_eyes(draw, 400, HEIGHT - 300, 30)
    draw_cute_mouth(draw, 400, HEIGHT - 260, 20)
    
    # 缆车线
    draw.line([(0, HEIGHT - 500), (WIDTH, HEIGHT - 500)], fill=(80, 80, 80), width=2)
    
    # 标题
    draw.text((WIDTH//2 - 70, 100), "Alpes", fill=(0, 0, 150), font=None)
    draw.text((WIDTH//2 - 80, 140), "Chamonix", fill=(100, 100, 100), font=None)
    
    img.save(f"{OUTPUT_DIR}alps-chamonix.png")
    print("✓ Generated: alps-chamonix.png")

def generate_normandy():
    """4. 诺曼底 - 圣米歇尔山"""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    
    # 岛屿基座
    island_points = [
        (200, HEIGHT - 150),
        (300, HEIGHT - 250),
        (400, HEIGHT - 280),
        (500, HEIGHT - 250),
        (600, HEIGHT - 150),
        (WIDTH, HEIGHT - 100),
        (0, HEIGHT - 100),
    ]
    draw.polygon(island_points, fill=(119, 136, 153), outline=(70, 80, 90), width=2)
    
    # 修道院建筑群
    # 主塔
    draw.rectangle([320, HEIGHT - 450, 480, HEIGHT - 280], fill=(245, 222, 179), outline=(139, 90, 43), width=2)
    # 尖顶
    spire_points = [(320, HEIGHT - 450), (400, HEIGHT - 600), (480, HEIGHT - 450)]
    draw.polygon(spire_points, fill=(139, 69, 19), outline=(100, 50, 0), width=2)
    # 金色雕像
    draw.ellipse([385, HEIGHT - 620, 415, HEIGHT - 590], fill=(255, 215, 0), outline=(200, 150, 0), width=2)
    
    # 侧塔
    draw.rectangle([260, HEIGHT - 380, 320, HEIGHT - 280], fill=(245, 222, 179), outline=(139, 90, 43), width=2)
    draw.rectangle([480, HEIGHT - 380, 540, HEIGHT - 280], fill=(245, 222, 179), outline=(139, 90, 43), width=2)
    
    # 可爱的表情
    draw_cute_eyes(draw, 400, HEIGHT - 380, 35)
    draw_cute_mouth(draw, 400, HEIGHT - 330, 25)
    
    # 海水
    draw.rectangle([0, HEIGHT - 100, WIDTH, HEIGHT], fill=(65, 105, 225, 128), outline=None)
    
    # 标题
    draw.text((WIDTH//2 - 80, 100), "Normandie", fill=(50, 50, 100), font=None)
    draw.text((WIDTH//2 - 110, 140), "Mont Saint-Michel", fill=(139, 90, 43), font=None)
    
    img.save(f"{OUTPUT_DIR}normandy-mont.png")
    print("✓ Generated: normandy-mont.png")

def generate_riviera():
    """5. 里维埃拉 - 蔚蓝海岸"""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    
    # 蔚蓝海岸沙滩
    draw.rectangle([0, HEIGHT - 200, WIDTH, HEIGHT], fill=(238, 203, 140), outline=(210, 180, 120), width=2)
    
    # 海水渐变
    for y in range(HEIGHT - 350, HEIGHT - 200):
        ratio = (y - (HEIGHT - 350)) / 150
        r = int(0 + ratio * 30)
        g = int(105 + ratio * 50)
        b = int(148 + ratio * 50)
        draw.line([(0, y), (WIDTH, y)], fill=(r, g, b))
    
    # 棕榈树
    for px in [150, 650]:
        # 树干
        draw.rectangle([px - 10, HEIGHT - 450, px + 10, HEIGHT - 250], fill=(139, 69, 19), outline=(100, 50, 0), width=2)
        # 树叶
        for angle in range(0, 360, 45):
            rad = math.radians(angle)
            leaf_x = px + int(80 * math.cos(rad))
            leaf_y = HEIGHT - 450 + int(30 * math.sin(rad))
            draw.line([px, HEIGHT - 450, leaf_x, leaf_y], fill=(34, 139, 34), width=8)
            draw.ellipse([leaf_x - 15, leaf_y - 10, leaf_x + 15, leaf_y + 10], fill=(50, 205, 50))
    
    # 海滨塔（昂蒂布风格）
    tower_color = (255, 228, 196)
    draw.rectangle([320, HEIGHT - 500, 480, HEIGHT - 300], fill=tower_color, outline=(139, 90, 43), width=3)
    # 红色屋顶
    roof_points = [(300, HEIGHT - 500), (400, HEIGHT - 580), (500, HEIGHT - 500)]
    draw.polygon(roof_points, fill=(220, 20, 60), outline=(150, 0, 0), width=3)
    
    # 可爱的表情
    draw_cute_eyes(draw, 400, HEIGHT - 420, 35)
    draw_cute_mouth(draw, 400, HEIGHT - 370, 25)
    
    # 标题
    draw.text((WIDTH//2 - 60, 100), "Riviera", fill=(0, 105, 148), font=None)
    draw.text((WIDTH//2 - 80, 140), "Côte d'Azur", fill=(65, 105, 225), font=None)
    
    img.save(f"{OUTPUT_DIR}riviera-coast.png")
    print("✓ Generated: riviera-coast.png")

def generate_loire():
    """6. 卢瓦尔河谷 - 城堡群"""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    
    # 河流
    draw.ellipse([200, HEIGHT - 100, 600, HEIGHT + 50], fill=(135, 206, 250), outline=(100, 149, 237), width=2)
    
    # 香波堡风格主塔
    castle_color = (245, 222, 179)
    # 中央主塔
    draw.rectangle([300, HEIGHT - 500, 500, HEIGHT - 250], fill=castle_color, outline=(139, 90, 43), width=3)
    
    # 四个角塔
    for tx, ty in [(250, HEIGHT - 400), (550, HEIGHT - 400), (250, HEIGHT - 300), (550, HEIGHT - 300)]:
        draw.rectangle([tx - 30, ty - 80, tx + 30, ty], fill=castle_color, outline=(139, 90, 43), width=2)
        # 塔顶
        roof_points = [(tx - 35, ty - 80), (tx, ty - 140), (tx + 35, ty - 80)]
        draw.polygon(roof_points, fill=(139, 69, 19), outline=(100, 50, 0), width=2)
    
    # 主塔屋顶
    draw.rectangle([280, HEIGHT - 540, 520, HEIGHT - 500], fill=(139, 69, 19), outline=(100, 50, 0), width=3)
    
    # 烟囱
    for cx in [320, 400, 480]:
        draw.rectangle([cx - 8, HEIGHT - 580, cx + 8, HEIGHT - 540], fill=(100, 50, 0), outline=(0, 0, 0), width=1)
        draw.ellipse([cx - 12, HEIGHT - 600, cx + 12, HEIGHT - 570], fill=(200, 200, 200, 100))
    
    # 可爱的表情
    draw_cute_eyes(draw, 400, HEIGHT - 400, 35)
    draw_cute_mouth(draw, 400, HEIGHT - 350, 25)
    
    # 标题
    draw.text((WIDTH//2 - 80, 100), "Val de Loire", fill=(139, 90, 43), font=None)
    draw.text((WIDTH//2 - 70, 140), "Châteaux", fill=(100, 50, 0), font=None)
    
    img.save(f"{OUTPUT_DIR}loire-castles.png")
    print("✓ Generated: loire-castles.png")

def generate_burgundy():
    """7. 勃艮第 - 葡萄园"""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    
    # 葡萄园梯田
    for row in range(6):
        y = HEIGHT - 280 + row * 30
        for col in range(15):
            x = 30 + col * 50
            # 葡萄藤
            draw.ellipse([x, y, x + 25, y + 25], fill=(34, 139, 34), outline=(0, 100, 0), width=1)
            # 葡萄串
            grape_colors = [(128, 0, 128), (75, 0, 130), (147, 112, 219)]
            for i in range(3):
                for j in range(2):
                    gc = grape_colors[(i+j) % 3]
                    draw.ellipse([x + 5 + i*6, y + 25 + j*6, x + 11 + i*6, y + 31 + j*6], fill=gc, outline=(100, 0, 100), width=1)
    
    # 勃艮第塔（博讷风格）
    tower_color = (205, 133, 63)
    draw.rectangle([320, HEIGHT - 500, 480, HEIGHT - 280], fill=tower_color, outline=(139, 69, 19), width=3)
    # 彩色屋顶瓦片
    for i in range(10):
        tile_color = (178 + (i*5)%40, 34, 34) if i % 2 == 0 else (139, 0, 0)
        draw.rectangle([320 + i*16, HEIGHT - 540, 336 + i*16, HEIGHT - 500], fill=tile_color, outline=(100, 0, 0), width=1)
    
    # 窗户（拱形）
    draw.arc([350, HEIGHT - 450, 450, HEIGHT - 380], 0, 180, fill=(0, 0, 100), width=4)
    draw.rectangle([350, HEIGHT - 415, 450, HEIGHT - 380], fill=(135, 206, 250), outline=(0, 0, 100), width=2)
    
    # 可爱的表情
    draw_cute_eyes(draw, 400, HEIGHT - 350, 30)
    draw_cute_mouth(draw, 400, HEIGHT - 310, 20)
    
    # 标题
    draw.text((WIDTH//2 - 70, 100), "Bourgogne", fill=(128, 0, 128), font=None)
    draw.text((WIDTH//2 - 80, 140), "Vignobles", fill=(34, 139, 34), font=None)
    
    img.save(f"{OUTPUT_DIR}burgundy-vineyard.png")
    print("✓ Generated: burgundy-vineyard.png")

def generate_alsace():
    """8. 阿尔萨斯 - 圣诞集市"""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    
    # 雪地
    draw.rectangle([0, HEIGHT - 200, WIDTH, HEIGHT], fill=(255, 250, 250), outline=(220, 220, 220), width=2)
    
    # 圣诞树
    for tx in [150, 650]:
        # 树形
        for level in range(4):
            y = HEIGHT - 350 + level * 40
            width = 80 - level * 15
            tree_points = [
                (tx - width, y + 40),
                (tx, y),
                (tx + width, y + 40),
            ]
            draw.polygon(tree_points, fill=(0, 100, 0), outline=(0, 60, 0), width=1)
        # 装饰
        for i in range(8):
            ox = tx + (i % 4 - 2) * 15
            oy = HEIGHT - 320 + (i // 4) * 30
            colors = [(255, 0, 0), (255, 215, 0), (0, 0, 255), (255, 192, 203)]
            draw.ellipse([ox - 5, oy - 5, ox + 5, oy + 5], fill=colors[i % 4])
    
    # 阿尔萨斯风格木筋房塔
    tower_color = (244, 164, 96)
    draw.rectangle([300, HEIGHT - 450, 500, HEIGHT - 280], fill=tower_color, outline=(139, 69, 19), width=3)
    
    # 木筋装饰
    for y in [HEIGHT - 430, HEIGHT - 380, HEIGHT - 330]:
        draw.line([(300, y), (500, y)], fill=(101, 67, 33), width=4)
    for x in [340, 380, 420, 460]:
        draw.line([(x, HEIGHT - 450), (x, HEIGHT - 280)], fill=(101, 67, 33), width=4)
    
    # 尖顶屋顶
    roof_points = [(280, HEIGHT - 450), (400, HEIGHT - 550), (520, HEIGHT - 450)]
    draw.polygon(roof_points, fill=(139, 0, 0), outline=(100, 0, 0), width=3)
    
    # 可爱的表情
    draw_cute_eyes(draw, 400, HEIGHT - 380, 35)
    draw_cute_mouth(draw, 400, HEIGHT - 330, 25)
    
    # 雪花
    for _ in range(20):
        sx = 50 + (_ * 37) % 700
        sy = 150 + (_ * 23) % 300
        draw.text((sx, sy), "❄", fill=(255, 255, 255))
    
    # 标题
    draw.text((WIDTH//2 - 60, 100), "Alsace", fill=(139, 0, 0), font=None)
    draw.text((WIDTH//2 - 90, 140), "Marché de Noël", fill=(0, 100, 0), font=None)
    
    img.save(f"{OUTPUT_DIR}alsace-christmas.png")
    print("✓ Generated: alsace-christmas.png")

def generate_brittany():
    """9. 布列塔尼 - 巨石阵"""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    
    # 草地
    draw.rectangle([0, HEIGHT - 200, WIDTH, HEIGHT], fill=(124, 252, 0), outline=(34, 139, 34), width=2)
    
    # 巨石阵 - 排列的立石
    stone_color = (128, 128, 128)
    
    # 前排石柱
    for i, sx in enumerate([180, 300, 420, 540]):
        height = 180 + (i % 2) * 40
        width = 50 + (i % 3) * 10
        # 石头纹理
        draw.rectangle([sx, HEIGHT - 200 - height, sx + width, HEIGHT - 200], 
                      fill=stone_color, outline=(80, 80, 80), width=3)
        # 石头纹理线条
        for j in range(3):
            draw.line([sx + 10, HEIGHT - 180 - height + j*40, sx + width - 10, HEIGHT - 170 - height + j*40], 
                     fill=(100, 100, 100), width=2)
    
    # 横石
    draw.rectangle([160, HEIGHT - 380, 590, HEIGHT - 350], fill=stone_color, outline=(80, 80, 80), width=3)
    
    # 中心巨石（带表情）
    main_stone_x, main_stone_y = 400, HEIGHT - 280
    draw.rectangle([main_stone_x - 60, main_stone_y - 150, main_stone_x + 60, main_stone_y], 
                  fill=(150, 150, 150), outline=(80, 80, 80), width=3)
    
    # 苔藓
    draw.ellipse([main_stone_x - 50, main_stone_y - 30, main_stone_x - 20, main_stone_y - 10], fill=(34, 139, 34, 100))
    draw.ellipse([main_stone_x + 20, main_stone_y - 40, main_stone_x + 50, main_stone_y - 20], fill=(34, 139, 34, 100))
    
    # 可爱的表情
    draw_cute_eyes(draw, main_stone_x, main_stone_y - 100, 30)
    draw_cute_mouth(draw, main_stone_x, main_stone_y - 70, 20)
    
    # 标题
    draw.text((WIDTH//2 - 70, 100), "Bretagne", fill=(50, 50, 150), font=None)
    draw.text((WIDTH//2 - 80, 140), "Menhirs", fill=(100, 100, 100), font=None)
    
    img.save(f"{OUTPUT_DIR}brittany-menhirs.png")
    print("✓ Generated: brittany-menhirs.png")

def generate_corsica():
    """10. 科西嘉 - 海岛"""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    
    # 海洋（更深的蓝色）
    draw.rectangle([0, HEIGHT - 250, WIDTH, HEIGHT], fill=(0, 105, 148), outline=(0, 80, 120), width=2)
    
    # 海浪
    for i in range(8):
        wave_y = HEIGHT - 200 + i * 25
        for j in range(10):
            x = j * 80 + (i % 2) * 40
            if x + 40 <= WIDTH:
                draw.arc([x, wave_y, x + 40, wave_y + 20], 0, 180, fill=(255, 255, 255), width=2)
    
    # 科西嘉岛轮廓（简化）
    island_points = [
        (250, HEIGHT - 200),
        (300, HEIGHT - 350),
        (350, HEIGHT - 450),
        (450, HEIGHT - 480),
        (550, HEIGHT - 400),
        (520, HEIGHT - 250),
        (450, HEIGHT - 200),
    ]
    draw.polygon(island_points, fill=(255, 228, 181), outline=(210, 180, 140), width=3)
    
    # 山脉
    mountain_points = [
        (320, HEIGHT - 350),
        (380, HEIGHT - 430),
        (450, HEIGHT - 480),
        (500, HEIGHT - 400),
        (480, HEIGHT - 360),
    ]
    draw.polygon(mountain_points, fill=(139, 69, 19), outline=(100, 50, 0), width=2)
    
    # 灯塔
    lighthouse_x, lighthouse_y = 420, HEIGHT - 320
    # 塔身
    draw.rectangle([lighthouse_x - 20, lighthouse_y - 100, lighthouse_x + 20, lighthouse_y], 
                  fill=(255, 255, 255), outline=(200, 200, 200), width=2)
    # 红色条纹
    draw.rectangle([lighthouse_x - 18, lighthouse_y - 80, lighthouse_x + 18, lighthouse_y - 60], fill=(220, 20, 60))
    draw.rectangle([lighthouse_x - 18, lighthouse_y - 40, lighthouse_x + 18, lighthouse_y - 20], fill=(220, 20, 60))
    # 灯室
    draw.rectangle([lighthouse_x - 15, lighthouse_y - 120, lighthouse_x + 15, lighthouse_y - 100], 
                  fill=(255, 255, 200), outline=(200, 200, 100), width=2)
    # 屋顶
    draw.polygon([
        (lighthouse_x - 20, lighthouse_y - 120),
        (lighthouse_x, lighthouse_y - 140),
        (lighthouse_x + 20, lighthouse_y - 120),
    ], fill=(220, 20, 60), outline=(150, 0, 0), width=2)
    
    # 光束 - 使用RGBA模式处理透明度
    overlay = Image.new('RGBA', img.size, (255, 255, 255, 0))
    overlay_draw = ImageDraw.Draw(overlay)
    overlay_draw.polygon([
        (lighthouse_x, lighthouse_y - 110),
        (lighthouse_x - 80, lighthouse_y - 200),
        (lighthouse_x - 60, lighthouse_y - 180),
    ], fill=(255, 255, 0, 80))
    overlay_draw.polygon([
        (lighthouse_x, lighthouse_y - 110),
        (lighthouse_x + 80, lighthouse_y - 200),
        (lighthouse_x + 60, lighthouse_y - 180),
    ], fill=(255, 255, 0, 80))
    img = Image.alpha_composite(img.convert('RGBA'), overlay)
    draw = ImageDraw.Draw(img)
    
    # 可爱的表情（在灯塔上）
    draw_cute_eyes(draw, lighthouse_x, lighthouse_y - 140, 20)
    draw_cute_mouth(draw, lighthouse_x, lighthouse_y - 120, 12)
    
    # 标题
    draw.text((WIDTH//2 - 60, 100), "Corse", fill=(0, 105, 148), font=None)
    draw.text((WIDTH//2 - 70, 140), "Île de Beauté", fill=(139, 69, 19), font=None)
    
    # 转换为RGB保存
    if img.mode == 'RGBA':
        img = img.convert('RGB')
    
    img.save(f"{OUTPUT_DIR}corsica-island.png")
    print("✓ Generated: corsica-island.png")

def main():
    """主函数：生成所有图片"""
    print("=" * 60)
    print("生成法国大区卡通塔图片")
    print("风格：愤怒的小鸟卡通风格")
    print("=" * 60)
    
    generators = [
        generate_ile_de_france,
        generate_provence,
        generate_alps,
        generate_normandy,
        generate_riviera,
        generate_loire,
        generate_burgundy,
        generate_alsace,
        generate_brittany,
        generate_corsica,
    ]
    
    for generator in generators:
        try:
            generator()
        except Exception as e:
            print(f"✗ Error generating {generator.__name__}: {e}")
    
    print("=" * 60)
    print("所有图片生成完成！")
    print(f"保存位置: {OUTPUT_DIR}")
    print("=" * 60)

if __name__ == "__main__":
    main()
