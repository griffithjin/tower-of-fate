from PIL import Image, ImageDraw, ImageFilter
import os

def create_gradient_background(width, height):
    """创建天蓝色渐变背景"""
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    
    # 天蓝色渐变：从浅蓝到更浅的蓝
    for y in range(height):
        # 从顶部(135, 206, 235)到底部(176, 224, 230)
        r = int(135 + (176 - 135) * y / height)
        g = int(206 + (224 - 206) * y / height)
        b = int(235 + (230 - 235) * y / height)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    return img

def draw_circle(draw, center, radius, color, outline_color=None, outline_width=2):
    """绘制圆形"""
    x, y = center
    bbox = [x - radius, y - radius, x + radius, y + radius]
    draw.ellipse(bbox, fill=color)
    if outline_color:
        draw.ellipse(bbox, outline=outline_color, width=outline_width)

def draw_rounded_rect(draw, bbox, radius, color, outline_color=None, outline_width=2):
    """绘制圆角矩形"""
    x1, y1, x2, y2 = bbox
    draw.rounded_rectangle(bbox, radius=radius, fill=color)
    if outline_color:
        draw.rounded_rectangle(bbox, radius=radius, outline=outline_color, width=outline_width)

def draw_eyes(draw, center_x, center_y, eye_size=25, pupil_size=12):
    """绘制愤怒的小鸟风格的眼睛"""
    # 左眼白
    draw_circle(draw, (center_x - 20, center_y), eye_size, (255, 255, 255), (0, 0, 0), 2)
    # 右眼白
    draw_circle(draw, (center_x + 20, center_y), eye_size, (255, 255, 255), (0, 0, 0), 2)
    # 左瞳孔
    draw_circle(draw, (center_x - 18, center_y), pupil_size, (0, 0, 0))
    # 右瞳孔
    draw_circle(draw, (center_x + 18, center_y), pupil_size, (0, 0, 0))
    # 高光
    draw_circle(draw, (center_x - 22, center_y - 8), 6, (255, 255, 255))
    draw_circle(draw, (center_x + 16, center_y - 8), 6, (255, 255, 255))

def draw_cute_beak(draw, center_x, center_y, size=20):
    """绘制可爱的鸟嘴"""
    # 上喙
    points = [
        (center_x, center_y - 5),
        (center_x - size, center_y + 10),
        (center_x + size, center_y + 10)
    ]
    draw.polygon(points, fill=(255, 200, 50), outline=(200, 150, 0), width=2)
    # 下喙
    points2 = [
        (center_x, center_y + 15),
        (center_x - size + 5, center_y + 8),
        (center_x + size - 5, center_y + 8)
    ]
    draw.polygon(points2, fill=(255, 180, 30), outline=(200, 140, 0), width=2)

def draw_cute_eyebrows(draw, center_x, center_y, expression='normal'):
    """绘制眉毛表情"""
    if expression == 'angry':
        # 愤怒眉毛
        draw.line([(center_x - 35, center_y - 15), (center_x - 10, center_y - 5)], fill=(0, 0, 0), width=4)
        draw.line([(center_x + 35, center_y - 15), (center_x + 10, center_y - 5)], fill=(0, 0, 0), width=4)
    elif expression == 'happy':
        # 开心眉毛（弯的）
        draw.arc([center_x - 40, center_y - 25, center_x - 10, center_y - 5], 200, 340, fill=(0, 0, 0), width=3)
        draw.arc([center_x + 10, center_y - 25, center_x + 40, center_y - 5], 200, 340, fill=(0, 0, 0), width=3)
    else:
        # 正常眉毛
        draw.line([(center_x - 35, center_y - 10), (center_x - 10, center_y - 10)], fill=(0, 0, 0), width=3)
        draw.line([(center_x + 35, center_y - 10), (center_x + 10, center_y - 10)], fill=(0, 0, 0), width=3)

def draw_clouds(draw, width, height):
    """绘制装饰云朵"""
    cloud_positions = [
        (100, 100), (600, 150), (200, 300), (650, 400),
        (150, 600), (620, 700), (180, 900), (640, 1000)
    ]
    for cx, cy in cloud_positions:
        # 绘制云朵（多个圆叠加）
        for offset in [(-25, 0), (25, 0), (0, -15), (-15, 10), (15, 10)]:
            draw_circle(draw, (cx + offset[0], cy + offset[1]), 20, (255, 255, 255, 180))

def create_bandung_tower():
    """西爪哇 - 万隆：高山茶园风格塔"""
    img = create_gradient_background(800, 1200)
    draw = ImageDraw.Draw(img)
    
    cx, cy = 400, 600
    
    # 塔身 - 绿色圆顶（茶园主题）
    base_color = (34, 139, 34)
    highlight = (60, 180, 60)
    shadow = (20, 100, 20)
    
    # 底层
    draw_rounded_rect(draw, [cx - 120, cy + 200, cx + 120, cy + 400], 20, base_color, (0, 0, 0), 3)
    # 中层
    draw_rounded_rect(draw, [cx - 90, cy, cx + 90, cy + 200], 20, highlight, (0, 0, 0), 3)
    # 顶层圆顶
    draw_circle(draw, (cx, cy - 50), 100, base_color, (0, 0, 0), 3)
    
    # 脸部
    draw_eyes(draw, cx, cy - 80)
    draw_cute_beak(draw, cx, cy - 40, 18)
    draw_cute_eyebrows(draw, cx, cy - 100, 'happy')
    
    # 茶叶装饰
    for i in range(-80, 81, 40):
        leaf_points = [(cx + i, cy + 300), (cx + i - 15, cy + 270), (cx + i + 15, cy + 270)]
        draw.polygon(leaf_points, fill=(50, 160, 50), outline=(30, 100, 30), width=2)
    
    # 腮红
    draw_circle(draw, (cx - 60, cy - 60), 15, (255, 150, 150, 100))
    draw_circle(draw, (cx + 60, cy - 60), 15, (255, 150, 150, 100))
    
    return img

def create_bromo_tower():
    """东爪哇 - 布罗莫火山：火山风格塔"""
    img = create_gradient_background(800, 1200)
    draw = ImageDraw.Draw(img)
    
    cx, cy = 400, 600
    
    # 火山形状塔
    volcano_color = (139, 69, 19)
    crater_color = (80, 40, 10)
    
    # 火山主体（三角形底座）
    volcano_points = [
        (cx, cy - 200),      # 顶点
        (cx - 150, cy + 350), # 左下
        (cx + 150, cy + 350), # 右下
    ]
    draw.polygon(volcano_points, fill=volcano_color, outline=(60, 30, 10), width=3)
    
    # 火山口
    crater_points = [
        (cx - 40, cy - 150),
        (cx + 40, cy - 150),
        (cx, cy - 100)
    ]
    draw.polygon(crater_points, fill=(50, 30, 20), outline=(0, 0, 0), width=2)
    
    # 烟雾
    for i, offset in enumerate([(-20, -180), (20, -200), (0, -230), (-15, -260)]):
        alpha = 200 - i * 30
        draw_circle(draw, (cx + offset[0], cy + offset[1]), 25 - i * 3, (200, 200, 200))
    
    # 脸部在火山体上
    draw_eyes(draw, cx, cy + 50, eye_size=22, pupil_size=10)
    draw_cute_beak(draw, cx, cy + 85, 16)
    draw_cute_eyebrows(draw, cx, cy + 25, 'normal')
    
    # 腮红
    draw_circle(draw, (cx - 50, cy + 60), 12, (255, 150, 150))
    draw_circle(draw, (cx + 50, cy + 60), 12, (255, 150, 150))
    
    return img

def create_borobudur_tower():
    """中爪哇 - 婆罗浮屠：佛塔风格塔"""
    img = create_gradient_background(800, 1200)
    draw = ImageDraw.Draw(img)
    
    cx, cy = 400, 550
    
    # 石质颜色
    stone_color = (180, 160, 140)
    stone_dark = (140, 120, 100)
    
    # 方形基座（多层阶梯）
    for i, size in enumerate([(200, 150), (160, 120), (120, 100), (80, 80)]):
        y_offset = 300 - i * 80
        draw_rounded_rect(draw, [cx - size[0], cy + y_offset, cx + size[0], cy + y_offset + size[1]], 
                         10, stone_color if i % 2 == 0 else stone_dark, (80, 70, 60), 3)
    
    # 顶部圆塔（佛塔）
    draw_circle(draw, (cx, cy - 100), 70, stone_color, (80, 70, 60), 3)
    # 尖顶
    spire_points = [(cx, cy - 250), (cx - 20, cy - 170), (cx + 20, cy - 170)]
    draw.polygon(spire_points, fill=stone_dark, outline=(80, 70, 60), width=2)
    
    # 脸部在圆塔上
    draw_eyes(draw, cx, cy - 100, eye_size=18, pupil_size=9)
    draw_cute_beak(draw, cx, cy - 70, 14)
    draw_cute_eyebrows(draw, cx, cy - 120, 'happy')
    
    # 装饰铃铛
    for angle in range(0, 360, 45):
        import math
        rad = math.radians(angle)
        bx = cx + int(50 * math.cos(rad))
        by = cy - 100 + int(50 * math.sin(rad))
        draw_circle(draw, (bx, by), 8, (160, 140, 120), (100, 90, 80), 1)
    
    # 腮红
    draw_circle(draw, (cx - 40, cy - 90), 10, (255, 150, 150))
    draw_circle(draw, (cx + 40, cy - 90), 10, (255, 150, 150))
    
    return img

def create_toba_tower():
    """北苏门答腊 - 多巴湖：湖水蓝风格塔"""
    img = create_gradient_background(800, 1200)
    draw = ImageDraw.Draw(img)
    
    cx, cy = 400, 600
    
    # 湖水蓝颜色
    lake_color = (70, 130, 180)
    lake_light = (100, 160, 210)
    lake_dark = (50, 100, 150)
    
    # 波浪形塔身（模拟湖水）
    # 底层波浪
    for i in range(5):
        x_offset = -100 + i * 50
        draw_circle(draw, (cx + x_offset, cy + 300), 40, lake_color, (40, 80, 120), 2)
    
    # 中层
    draw_rounded_rect(draw, [cx - 100, cy + 100, cx + 100, cy + 250], 30, lake_light, (40, 80, 120), 3)
    
    # 顶部圆顶
    draw_circle(draw, (cx, cy), 90, lake_color, (40, 80, 120), 3)
    draw_circle(draw, (cx, cy - 20), 60, lake_light, (40, 80, 120), 2)
    
    # 脸部
    draw_eyes(draw, cx, cy - 10, eye_size=20, pupil_size=10)
    draw_cute_beak(draw, cx, cy + 20, 15)
    draw_cute_eyebrows(draw, cx, cy - 30, 'happy')
    
    # 水波纹装饰
    for y in range(cy + 150, cy + 250, 30):
        draw.arc([cx - 60, y - 10, cx + 60, y + 10], 0, 180, fill=(150, 190, 220), width=3)
    
    # 腮红
    draw_circle(draw, (cx - 50, cy), 12, (255, 150, 150))
    draw_circle(draw, (cx + 50, cy), 12, (255, 150, 150))
    
    return img

def create_monas_tower():
    """雅加达 - 民族纪念碑：方尖碑风格塔"""
    img = create_gradient_background(800, 1200)
    draw = ImageDraw.Draw(img)
    
    cx, cy = 400, 650
    
    # 金色和白色
    gold_color = (255, 215, 0)
    white_color = (250, 250, 245)
    flame_orange = (255, 140, 0)
    
    # 底座
    draw_rounded_rect(draw, [cx - 130, cy + 250, cx + 130, cy + 350], 15, white_color, (200, 200, 190), 3)
    
    # 方尖碑主体（逐渐变细）
    obelisk_points = [
        (cx - 60, cy + 250),  # 底部左
        (cx + 60, cy + 250),  # 底部右
        (cx + 25, cy - 200),  # 顶部右
        (cx - 25, cy - 200),  # 顶部左
    ]
    draw.polygon(obelisk_points, fill=white_color, outline=(200, 200, 190), width=3)
    
    # 顶部火焰
    flame_points = [
        (cx, cy - 280),
        (cx - 30, cy - 200),
        (cx + 30, cy - 200)
    ]
    draw.polygon(flame_points, fill=flame_orange, outline=(200, 100, 0), width=2)
    # 火焰内部
    flame_inner = [
        (cx, cy - 260),
        (cx - 15, cy - 205),
        (cx + 15, cy - 205)
    ]
    draw.polygon(flame_inner, fill=(255, 200, 50), outline=(200, 150, 0), width=1)
    
    # 脸部在中部
    draw_eyes(draw, cx, cy + 50, eye_size=22, pupil_size=11)
    draw_cute_beak(draw, cx, cy + 85, 16)
    draw_cute_eyebrows(draw, cx, cy + 25, 'angry')
    
    # 金色装饰条纹
    for y in [cy + 100, cy, cy - 100]:
        draw.line([(cx - 40, y), (cx + 40, y)], fill=gold_color, width=5)
    
    # 腮红
    draw_circle(draw, (cx - 45, cy + 60), 11, (255, 150, 150))
    draw_circle(draw, (cx + 45, cy + 60), 11, (255, 150, 150))
    
    return img

def create_toraja_tower():
    """南苏拉威西 - 托拉查：船形屋顶风格塔"""
    img = create_gradient_background(800, 1200)
    draw = ImageDraw.Draw(img)
    
    cx, cy = 400, 600
    
    # 木质颜色
    wood_color = (139, 90, 43)
    wood_dark = (101, 67, 33)
    wood_light = (180, 130, 80)
    
    # 船形屋顶（高耸的船形）
    roof_points = [
        (cx, cy - 250),       # 顶尖
        (cx - 160, cy + 100), # 左下
        (cx - 100, cy + 150), # 左底内
        (cx + 100, cy + 150), # 右底内
        (cx + 160, cy + 100), # 右下
    ]
    draw.polygon(roof_points, fill=wood_color, outline=(80, 50, 25), width=4)
    
    # 屋顶纹理
    for i in range(-140, 141, 35):
        y_top = cy - 200 + abs(i) * 0.5
        y_bottom = cy + 120
        draw.line([(cx + i, y_top), (cx + i, y_bottom)], fill=wood_dark, width=3)
    
    # 房屋主体
    draw_rounded_rect(draw, [cx - 80, cy + 100, cx + 80, cy + 300], 15, wood_light, (100, 70, 40), 3)
    
    # 脸部
    draw_eyes(draw, cx, cy + 180, eye_size=20, pupil_size=10)
    draw_cute_beak(draw, cx, cy + 210, 14)
    draw_cute_eyebrows(draw, cx, cy + 155, 'normal')
    
    # 托拉查传统图案装饰
    for x in range(cx - 60, cx + 61, 40):
        draw_circle(draw, (x, cy + 260), 12, wood_dark, (80, 50, 25), 2)
    
    # 腮红
    draw_circle(draw, (cx - 50, cy + 190), 10, (255, 150, 150))
    draw_circle(draw, (cx + 50, cy + 190), 10, (255, 150, 150))
    
    return img

def create_tanah_lot_tower():
    """巴厘岛 - 海神庙：神庙风格塔"""
    img = create_gradient_background(800, 1200)
    draw = ImageDraw.Draw(img)
    
    cx, cy = 400, 600
    
    # 神庙灰色
    temple_color = (169, 169, 169)
    temple_dark = (128, 128, 128)
    temple_light = (192, 192, 192)
    
    # 多层塔顶（Meru风格）
    for i in range(7):
        width = 140 - i * 15
        y_pos = cy - 150 + i * 35
        # 每层都是草屋顶形状
        roof_points = [
            (cx, y_pos - 20),
            (cx - width, y_pos + 10),
            (cx + width, y_pos + 10)
        ]
        color = temple_dark if i % 2 == 0 else temple_color
        draw.polygon(roof_points, fill=color, outline=(100, 100, 100), width=2)
    
    # 主体
    draw_rounded_rect(draw, [cx - 70, cy + 100, cx + 70, cy + 300], 15, temple_light, (100, 100, 100), 3)
    
    # 神庙门
    door_points = [
        (cx, cy + 180),
        (cx - 30, cy + 280),
        (cx + 30, cy + 280)
    ]
    draw.polygon(door_points, fill=(80, 60, 50), outline=(60, 40, 30), width=2)
    
    # 脸部在主体上
    draw_eyes(draw, cx, cy + 180, eye_size=18, pupil_size=9)
    draw_cute_beak(draw, cx, cy + 205, 12)
    draw_cute_eyebrows(draw, cx, cy + 160, 'happy')
    
    # 海水波浪
    for i in range(5):
        wave_y = cy + 320 + i * 20
        draw.arc([cx - 150 + i * 30, wave_y, cx - 50 + i * 30, wave_y + 30], 0, 180, 
                fill=(100, 150, 200), width=3)
        draw.arc([cx + 50 - i * 30, wave_y, cx + 150 - i * 30, wave_y + 30], 0, 180, 
                fill=(100, 150, 200), width=3)
    
    # 腮红
    draw_circle(draw, (cx - 45, cy + 190), 10, (255, 150, 150))
    draw_circle(draw, (cx + 45, cy + 190), 10, (255, 150, 150))
    
    return img

def create_komodo_tower():
    """东努沙登加拉 - 科莫多岛：巨蜥/恐龙风格塔"""
    img = create_gradient_background(800, 1200)
    draw = ImageDraw.Draw(img)
    
    cx, cy = 400, 600
    
    # 科莫多龙颜色
    dragon_color = (85, 107, 47)
    dragon_light = (107, 142, 35)
    dragon_dark = (60, 80, 30)
    
    # 身体（厚实）
    draw_rounded_rect(draw, [cx - 100, cy + 100, cx + 100, cy + 350], 30, dragon_color, (50, 70, 25), 4)
    
    # 颈部
    neck_points = [
        (cx - 40, cy + 100),
        (cx + 40, cy + 100),
        (cx + 60, cy - 100),
        (cx - 60, cy - 100)
    ]
    draw.polygon(neck_points, fill=dragon_light, outline=(50, 70, 25), width=3)
    
    # 头部
    head_points = [
        (cx, cy - 180),
        (cx - 80, cy - 100),
        (cx - 70, cy - 50),
        (cx + 70, cy - 50),
        (cx + 80, cy - 100)
    ]
    draw.polygon(head_points, fill=dragon_color, outline=(50, 70, 25), width=3)
    
    # 眼睛（科莫多龙的小眼睛）
    draw_circle(draw, (cx - 35, cy - 110), 15, (255, 255, 255), (0, 0, 0), 2)
    draw_circle(draw, (cx + 35, cy - 110), 15, (255, 255, 255), (0, 0, 0), 2)
    draw_circle(draw, (cx - 32, cy - 110), 8, (0, 0, 0))
    draw_circle(draw, (cx + 32, cy - 110), 8, (0, 0, 0))
    
    # 鼻孔
    draw_circle(draw, (cx - 15, cy - 70), 5, (40, 60, 20))
    draw_circle(draw, (cx + 15, cy - 70), 5, (40, 60, 20))
    
    # 鳞片纹理
    for y in range(cy + 150, cy + 320, 40):
        for x in range(cx - 70, cx + 71, 35):
            draw_circle(draw, (x, y), 8, dragon_dark, (40, 60, 20), 1)
    
    # 眉毛（凶猛但可爱）
    draw.line([(cx - 50, cy - 130), (cx - 20, cy - 120)], fill=(0, 0, 0), width=3)
    draw.line([(cx + 50, cy - 130), (cx + 20, cy - 120)], fill=(0, 0, 0), width=3)
    
    # 腮红
    draw_circle(draw, (cx - 55, cy - 90), 10, (255, 150, 150))
    draw_circle(draw, (cx + 55, cy - 90), 10, (255, 150, 150))
    
    return img

def create_krakatau_tower():
    """楠榜 - 喀拉喀托火山：爆发火山风格塔"""
    img = create_gradient_background(800, 1200)
    draw = ImageDraw.Draw(img)
    
    cx, cy = 400, 600
    
    # 火山颜色
    volcano_color = (64, 64, 64)
    volcano_dark = (40, 40, 40)
    lava_color = (255, 69, 0)
    lava_bright = (255, 140, 0)
    
    # 火山主体
    volcano_points = [
        (cx, cy - 180),
        (cx - 140, cy + 350),
        (cx + 140, cy + 350)
    ]
    draw.polygon(volcano_points, fill=volcano_color, outline=(30, 30, 30), width=3)
    
    # 火山口与岩浆
    crater_points = [
        (cx - 50, cy - 120),
        (cx + 50, cy - 120),
        (cx, cy - 80)
    ]
    draw.polygon(crater_points, fill=lava_color, outline=(200, 50, 0), width=2)
    
    # 岩浆流动
    for i, offset in enumerate([(-30, -80), (30, -70), (0, -50)]):
        lava_points = [
            (cx + offset[0], cy + offset[1]),
            (cx + offset[0] - 10, cy + offset[1] + 40),
            (cx + offset[0] + 10, cy + offset[1] + 40)
        ]
        draw.polygon(lava_points, fill=lava_bright, outline=(200, 80, 0), width=1)
    
    # 爆发烟雾和灰烬
    for i, pos in enumerate([(cx - 40, cy - 200), (cx + 30, cy - 230), (cx, cy - 270), 
                             (cx - 20, cy - 310), (cx + 40, cy - 340)]):
        size = 30 - i * 4
        gray = 150 - i * 20
        draw_circle(draw, pos, size, (gray, gray, gray), (gray - 30, gray - 30, gray - 30), 2)
    
    # 脸部
    draw_eyes(draw, cx, cy + 100, eye_size=24, pupil_size=12)
    draw_cute_beak(draw, cx, cy + 140, 18)
    draw_cute_eyebrows(draw, cx, cy + 70, 'angry')
    
    # 岩石纹理
    for _ in range(15):
        import random
        rx = cx + random.randint(-100, 100)
        ry = cy + random.randint(50, 300)
        draw_circle(draw, (rx, ry), random.randint(5, 12), volcano_dark, (30, 30, 30), 1)
    
    # 腮红
    draw_circle(draw, (cx - 60, cy + 110), 13, (255, 150, 150))
    draw_circle(draw, (cx + 60, cy + 110), 13, (255, 150, 150))
    
    return img

def create_batam_tower():
    """廖内 - 巴淡岛：现代港口/工业风格塔"""
    img = create_gradient_background(800, 1200)
    draw = ImageDraw.Draw(img)
    
    cx, cy = 400, 600
    
    # 工业蓝和银色
    industrial_blue = (70, 130, 180)
    silver = (192, 192, 192)
    steel = (119, 136, 153)
    container_colors = [(200, 50, 50), (50, 150, 50), (50, 50, 200), (200, 180, 50)]
    
    # 主体建筑（港口控制塔）
    draw_rounded_rect(draw, [cx - 80, cy + 150, cx + 80, cy + 350], 15, industrial_blue, (50, 100, 150), 3)
    
    # 塔身（细长）
    draw_rounded_rect(draw, [cx - 30, cy - 50, cx + 30, cy + 150], 10, steel, (80, 100, 120), 2)
    
    # 顶部控制室
    draw_rounded_rect(draw, [cx - 70, cy - 100, cx + 70, cy - 20], 15, silver, (100, 120, 140), 3)
    
    # 顶部天线
    draw.line([(cx, cy - 150), (cx, cy - 100)], fill=(80, 100, 120), width=4)
    draw_circle(draw, (cx, cy - 155), 8, (255, 50, 50), (150, 30, 30), 2)
    
    # 脸部在控制室
    draw_eyes(draw, cx, cy - 60, eye_size=18, pupil_size=9)
    draw_cute_beak(draw, cx, cy - 35, 12)
    draw_cute_eyebrows(draw, cx, cy - 80, 'normal')
    
    # 集装箱装饰
    for i, color in enumerate(container_colors):
        x_pos = cx - 60 + i * 35
        draw_rounded_rect(draw, [x_pos - 15, cy + 280, x_pos + 15, cy + 330], 3, 
                         color, (150, 150, 150), 2)
        # 集装箱线条
        for j in range(3):
            draw.line([(x_pos - 12 + j * 8, cy + 285), (x_pos - 12 + j * 8, cy + 325)], 
                     fill=(200, 200, 200), width=1)
    
    # 起重机
    crane_x = cx + 120
    draw.line([(crane_x, cy + 350), (crane_x, cy + 150)], fill=(180, 180, 180), width=6)
    draw.line([(crane_x, cy + 150), (crane_x + 80, cy + 100)], fill=(180, 180, 180), width=4)
    draw.line([(crane_x + 80, cy + 100), (crane_x + 80, cy + 180)], fill=(150, 150, 150), width=2)
    
    # 腮红
    draw_circle(draw, (cx - 45, cy - 50), 10, (255, 150, 150))
    draw_circle(draw, (cx + 45, cy - 50), 10, (255, 150, 150))
    
    return img

# 主函数
def main():
    output_dir = "/Users/moutai/Desktop/toweroffate_v1.0/assets/towers/states/indonesia/"
    os.makedirs(output_dir, exist_ok=True)
    
    towers = [
        ("west-java-bandung.png", create_bandung_tower, "西爪哇 - 万隆"),
        ("east-java-bromo.png", create_bromo_tower, "东爪哇 - 布罗莫火山"),
        ("central-java-borobudur.png", create_borobudur_tower, "中爪哇 - 婆罗浮屠"),
        ("north-sumatra-toba.png", create_toba_tower, "北苏门答腊 - 多巴湖"),
        ("jakarta-national-monument.png", create_monas_tower, "雅加达 - 民族纪念碑"),
        ("south-sulawesi-toraja.png", create_toraja_tower, "南苏拉威西 - 托拉查"),
        ("bali-tanah-lot.png", create_tanah_lot_tower, "巴厘岛 - 海神庙"),
        ("east-nusa-komodo.png", create_komodo_tower, "东努沙登加拉 - 科莫多岛"),
        ("lampung-krakatau.png", create_krakatau_tower, "楠榜 - 喀拉喀托火山"),
        ("riau-batam.png", create_batam_tower, "廖内 - 巴淡岛"),
    ]
    
    for filename, create_func, name in towers:
        print(f"正在生成: {name} -> {filename}")
        img = create_func()
        filepath = os.path.join(output_dir, filename)
        img.save(filepath, "PNG")
        print(f"  ✓ 已保存: {filepath}")
    
    print("\n✅ 全部10个印尼省份卡通塔图片生成完成！")

if __name__ == "__main__":
    main()
