from PIL import Image, ImageDraw, ImageFont
import math
import os

# 输出目录
output_dir = "/Users/moutai/Desktop/toweroffate_v1.0/assets/towers/states/uk"
os.makedirs(output_dir, exist_ok=True)

# 图片尺寸
WIDTH, HEIGHT = 800, 1200

def create_sky_gradient():
    """创建天蓝色渐变背景"""
    img = Image.new('RGB', (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(img)
    
    for y in range(HEIGHT):
        # 从浅天蓝到深一点的蓝色渐变
        r = int(135 - y * 0.05)
        g = int(206 - y * 0.03)
        b = int(235 - y * 0.02)
        draw.line([(0, y), (WIDTH, y)], fill=(r, g, b))
    
    return img

def draw_circle(draw, x, y, radius, color):
    """绘制圆形"""
    draw.ellipse([x-radius, y-radius, x+radius, y+radius], fill=color)

def draw_oval(draw, x, y, w, h, color):
    """绘制椭圆形"""
    draw.ellipse([x-w//2, y-h//2, x+w//2, y+h//2], fill=color)

def draw_rounded_rect(draw, x, y, w, h, radius, color):
    """绘制圆角矩形"""
    draw.rounded_rectangle([x, y, x+w, y+h], radius=radius, fill=color)

def draw_cute_eyes(draw, x, y, eye_size=20):
    """绘制可爱的卡通眼睛"""
    # 左眼白
    draw.ellipse([x-35, y-eye_size, x-15, y+eye_size], fill='white')
    # 右眼白
    draw.ellipse([x+15, y-eye_size, x+35, y+eye_size], fill='white')
    # 左眼珠
    draw.ellipse([x-28, y-eye_size+5, x-20, y+eye_size-5], fill='black')
    # 右眼珠
    draw.ellipse([x+20, y-eye_size+5, x+28, y+eye_size-5], fill='black')
    # 高光
    draw.ellipse([x-26, y-eye_size+8, x-22, y+eye_size-2], fill='white')
    draw.ellipse([x+22, y-eye_size+8, x+26, y+eye_size-2], fill='white')

def draw_cute_mouth(draw, x, y):
    """绘制可爱的微笑嘴巴"""
    draw.arc([x-20, y-10, x+20, y+20], start=0, end=180, fill='black', width=3)

def draw_blush(draw, x, y):
    """绘制腮红"""
    draw.ellipse([x-45, y-5, x-25, y+15], fill=(255, 182, 193, 128))
    draw.ellipse([x+25, y-5, x+45, y+15], fill=(255, 182, 193, 128))

# ==================== 1. 英格兰 - 伦敦眼 ====================
def draw_london_eye():
    img = create_sky_gradient()
    draw = ImageDraw.Draw(img)
    
    cx, cy = WIDTH//2, HEIGHT//2 + 100
    
    # 绘制云朵
    for i in range(5):
        x = 100 + i * 150
        y = 100 + (i % 2) * 50
        draw.ellipse([x-50, y-30, x+50, y+30], fill='white')
        draw.ellipse([x-30, y-40, x+30, y+40], fill='white')
    
    # 伦敦眼主轮（可爱的圆形）
    # 外轮
    draw.ellipse([cx-200, cy-200, cx+200, cy+200], outline='#4A90E2', width=15)
    # 内轮
    draw.ellipse([cx-180, cy-180, cx+180, cy+180], outline='#87CEEB', width=8)
    
    # 支架（A字形）
    draw.polygon([(cx, cy-50), (cx-80, cy+250), (cx+80, cy+250)], fill='#666666')
    draw.polygon([(cx, cy-50), (cx-80, cy+250), (cx+80, cy+250)], outline='#444444', width=3)
    
    # 底座
    draw.rounded_rectangle([cx-100, cy+240, cx+100, cy+280], radius=10, fill='#555555')
    
    # 座舱（圆形，带眼睛）
    for angle in range(0, 360, 30):
        rad = math.radians(angle)
        px = cx + 190 * math.cos(rad)
        py = cy + 190 * math.sin(rad)
        # 座舱
        draw.ellipse([px-20, py-20, px+20, py+20], fill='#FF6B6B', outline='white', width=3)
        # 小窗户（像眼睛）
        draw.ellipse([px-8, py-5, px+8, py+5], fill='#87CEEB')
    
    # 中心轴（眼睛）
    draw.ellipse([cx-40, cy-40, cx+40, cy+40], fill='#FFD93D')
    draw_cute_eyes(draw, cx, cy-5, 12)
    draw_cute_mouth(draw, cx, cy+15)
    
    # 标签
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 40)
    except:
        font = ImageFont.load_default()
    draw.text((WIDTH//2, HEIGHT-100), "英格兰 - 伦敦眼", fill='#333333', font=font, anchor='mm')
    
    img.save(f"{output_dir}/england-london-eye.png")
    print("✓ 已生成: england-london-eye.png")

# ==================== 2. 苏格兰 - 爱丁堡城堡 ====================
def draw_edinburgh_castle():
    img = create_sky_gradient()
    draw = ImageDraw.Draw(img)
    
    cx, cy = WIDTH//2, HEIGHT//2 + 50
    
    # 山丘背景
    draw.polygon([(0, HEIGHT), (0, cy+150), (WIDTH//3, cy+100), (WIDTH//2, cy+80), 
                  (2*WIDTH//3, cy+100), (WIDTH, cy+150), (WIDTH, HEIGHT)], fill='#4A6741')
    
    # 城堡主体（可爱的块状风格）
    base_y = cy + 150
    
    # 主城堡塔楼
    draw.rounded_rectangle([cx-120, base_y-200, cx+120, base_y], radius=15, fill='#8B7355')
    draw.rounded_rectangle([cx-120, base_y-200, cx+120, base_y], radius=15, outline='#5D4E37', width=4)
    
    # 眼睛（在城堡上）
    draw_cute_eyes(draw, cx, base_y-120, 18)
    draw_cute_mouth(draw, cx, base_y-80)
    draw_blush(draw, cx, base_y-100)
    
    # 左侧塔楼
    draw.rounded_rectangle([cx-180, base_y-150, cx-100, base_y], radius=10, fill='#A0826D')
    # 右侧塔楼
    draw.rounded_rectangle([cx+100, base_y-150, cx+180, base_y], radius=10, fill='#A0826D')
    
    # 屋顶（三角形，红色）
    draw.polygon([(cx-130, base_y-200), (cx, base_y-280), (cx+130, base_y-200)], fill='#C41E3A')
    draw.polygon([(cx-190, base_y-150), (cx-140, base_y-220), (cx-90, base_y-150)], fill='#C41E3A')
    draw.polygon([(cx+90, base_y-150), (cx+140, base_y-220), (cx+190, base_y-150)], fill='#C41E3A')
    
    # 旗帜
    draw.line([(cx, base_y-280), (cx, base_y-320)], fill='#8B4513', width=4)
    draw.polygon([(cx, base_y-320), (cx+60, base_y-305), (cx, base_y-290)], fill='#0055A4')
    
    # 窗户
    for wx in [cx-80, cx, cx+80]:
        draw.ellipse([wx-15, base_y-40, wx+15, base_y-10], fill='#333333')
        draw.ellipse([wx-15, base_y-40, wx+15, base_y-10], outline='#555555', width=2)
    
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 40)
    except:
        font = ImageFont.load_default()
    draw.text((WIDTH//2, HEIGHT-100), "苏格兰 - 爱丁堡城堡", fill='#333333', font=font, anchor='mm')
    
    img.save(f"{output_dir}/scotland-edinburgh.png")
    print("✓ 已生成: scotland-edinburgh.png")

# ==================== 3. 威尔士 - 卡迪夫城堡 ====================
def draw_cardiff_castle():
    img = create_sky_gradient()
    draw = ImageDraw.Draw(img)
    
    cx, cy = WIDTH//2, HEIGHT//2 + 50
    base_y = cy + 200
    
    # 主塔楼（圆柱形）
    draw.rounded_rectangle([cx-100, base_y-250, cx+100, base_y], radius=30, fill='#D4A574')
    draw.rounded_rectangle([cx-100, base_y-250, cx+100, base_y], radius=30, outline='#8B6914', width=4)
    
    # 可爱的脸
    draw_cute_eyes(draw, cx, base_y-150, 20)
    draw_cute_mouth(draw, cx, base_y-100)
    draw_blush(draw, cx, base_y-120)
    
    # 塔顶（圆锥形屋顶）
    draw.polygon([(cx-110, base_y-250), (cx, base_y-380), (cx+110, base_y-250)], fill='#2E5C8A')
    # 屋顶条纹
    for i in range(-3, 4):
        x_off = i * 25
        draw.line([(cx+x_off, base_y-250), (cx, base_y-380)], fill='#1E3A5F', width=3)
    
    # 小塔楼
    for offset in [-150, 150]:
        draw.rounded_rectangle([cx+offset-40, base_y-180, cx+offset+40, base_y], radius=15, fill='#C49464')
        draw.polygon([(cx+offset-45, base_y-180), (cx+offset, base_y-260), (cx+offset+45, base_y-180)], fill='#2E5C8A')
    
    # 城墙
    draw.rounded_rectangle([cx-220, base_y-80, cx+220, base_y], radius=5, fill='#B8956A')
    # 城垛
    for i in range(-4, 5):
        x = cx + i * 50
        draw.rectangle([x-15, base_y-110, x+15, base_y-80], fill='#B8956A')
    
    # 威尔士龙装饰
    dragon_y = base_y - 300
    # 简化的龙身
    draw.ellipse([cx-40, dragon_y-20, cx+40, dragon_y+20], fill='#C41E3A')
    draw.ellipse([cx-15, dragon_y-35, cx+15, dragon_y+5], fill='#C41E3A')  # 龙头
    # 翅膀
    draw.polygon([(cx, dragon_y-10), (cx-50, dragon_y-50), (cx-30, dragon_y)], fill='#FFD700')
    draw.polygon([(cx, dragon_y-10), (cx+50, dragon_y-50), (cx+30, dragon_y)], fill='#FFD700')
    
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 40)
    except:
        font = ImageFont.load_default()
    draw.text((WIDTH//2, HEIGHT-100), "威尔士 - 卡迪夫城堡", fill='#333333', font=font, anchor='mm')
    
    img.save(f"{output_dir}/wales-cardiff.png")
    print("✓ 已生成: wales-cardiff.png")

# ==================== 4. 北爱尔兰 - 巨人之路 ====================
def draw_giants_causeway():
    img = create_sky_gradient()
    draw = ImageDraw.Draw(img)
    
    cx, cy = WIDTH//2, HEIGHT//2
    
    # 海洋背景（下半部分）
    for y in range(cy+100, HEIGHT):
        blue = int(100 + (y - cy - 100) * 0.1)
        draw.line([(0, y), (WIDTH, y)], fill=(50, 100, blue+100))
    
    # 海岸线（可爱的弧线）
    draw.polygon([(0, HEIGHT), (0, cy+150), (WIDTH//4, cy+120), (WIDTH//2, cy+100), 
                  (3*WIDTH//4, cy+120), (WIDTH, cy+150), (WIDTH, HEIGHT)], fill='#4A5568')
    
    # 六角形石柱（卡通风格 - 像蜂窝）
    hex_size = 35
    rows = 6
    cols = 8
    
    for row in range(rows):
        for col in range(cols):
            x = cx + (col - cols//2) * (hex_size * 1.8)
            y = cy + 200 + row * (hex_size * 1.5)
            if row % 2 == 1:
                x += hex_size * 0.9
            
            # 只绘制海岸线上的
            if y > cy + 100:
                # 六边形
                points = []
                for i in range(6):
                    angle = math.radians(60 * i - 30)
                    px = x + hex_size * math.cos(angle)
                    py = y + hex_size * math.sin(angle)
                    points.append((px, py))
                
                # 随机深浅
                color_val = 80 + (row + col) % 3 * 20
                draw.polygon(points, fill=(color_val, color_val, color_val+10))
                draw.polygon(points, outline='#333333', width=2)
                
                # 顶部高光
                top_points = [(x, y-hex_size), (x+hex_size*0.87, y-hex_size*0.5), 
                             (x+hex_size*0.87, y+hex_size*0.5)]
    
    # 可爱的巨人脸在岩石群中
    face_x, face_y = cx, cy + 250
    # 选择几块石头组成脸
    draw.ellipse([face_x-50, face_y-50, face_x+50, face_y+50], fill='#5A6568')
    draw_cute_eyes(draw, face_x, face_y-10, 15)
    draw_cute_mouth(draw, face_x, face_y+20)
    
    # 海浪
    for i in range(3):
        wave_y = cy + 120 + i * 30
        for wx in range(0, WIDTH, 100):
            offset = i * 30
            draw.arc([wx+offset, wave_y-15, wx+80+offset, wave_y+15], 0, 180, fill='#87CEEB', width=3)
    
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 40)
    except:
        font = ImageFont.load_default()
    draw.text((WIDTH//2, HEIGHT-100), "北爱尔兰 - 巨人之路", fill='#333333', font=font, anchor='mm')
    
    img.save(f"{output_dir}/northern-ireland-giants.png")
    print("✓ 已生成: northern-ireland-giants.png")

# ==================== 5. 康沃尔 - 悬崖 ====================
def draw_cornwall_cliffs():
    img = create_sky_gradient()
    draw = ImageDraw.Draw(img)
    
    cx, cy = WIDTH//2, HEIGHT//2
    
    # 海洋
    for y in range(cy, HEIGHT):
        blue = int(150 + (y - cy) * 0.1)
        draw.line([(0, y), (WIDTH, y)], fill=(100, 150, blue+100))
    
    # 悬崖（卡通化的绿色悬崖）
    cliff_points = [(0, HEIGHT), (0, cy-50), (WIDTH//4, cy-30), (WIDTH//2-50, cy+20),
                    (WIDTH//2, cy-80), (WIDTH//2+50, cy+20), (3*WIDTH//4, cy-30), (WIDTH, cy-50), (WIDTH, HEIGHT)]
    draw.polygon(cliff_points, fill='#7CB342')
    draw.polygon(cliff_points, outline='#558B2F', width=4)
    
    # 悬崖顶部的草
    grass_points = [(0, cy-50), (WIDTH//4, cy-30), (WIDTH//2-50, cy+20),
                    (WIDTH//2, cy-80), (WIDTH//2+50, cy+20), (3*WIDTH//4, cy-30), (WIDTH, cy-50),
                    (WIDTH, cy-80), (0, cy-80)]
    draw.polygon(grass_points, fill='#8BC34A')
    
    # 悬崖上的可爱脸
    face_x, face_y = WIDTH//2, cy + 50
    # 悬崖纹理 + 眼睛
    draw.ellipse([face_x-60, face_y-40, face_x+60, face_y+40], fill='#9CCC65')
    draw_cute_eyes(draw, face_x, face_y-10, 18)
    draw_cute_mouth(draw, face_x, face_y+25)
    draw_blush(draw, face_x, face_y)
    
    # 悬崖层理（水平线条）
    for i in range(4):
        y = cy + 100 + i * 80
        if y < HEIGHT - 100:
            draw.line([(0, y), (WIDTH, y)], fill='#689F38', width=2)
    
    # 海鸥
    for i in range(3):
        gx = 100 + i * 250
        gy = 150 + i * 50
        # 简化的M形海鸥
        draw.arc([gx-20, gy-10, gx, gy+10], 20, 160, fill='white', width=3)
        draw.arc([gx, gy-10, gx+20, gy+10], 20, 160, fill='white', width=3)
    
    # 灯塔（在悬崖边缘）
    lx, ly = WIDTH - 150, cy - 100
    # 塔身（红白条纹）
    for i in range(4):
        color = '#C41E3A' if i % 2 == 0 else 'white'
        draw.rounded_rectangle([lx-25, ly+i*40, lx+25, ly+(i+1)*40], radius=5, fill=color)
    # 灯室
    draw.rounded_rectangle([lx-30, ly-30, lx+30, ly], radius=5, fill='#333333')
    draw.ellipse([lx-15, ly-20, lx+15, ly-5], fill='#FFD700')
    # 光束
    beam_points = [(lx, ly-15), (lx-100, ly-80), (lx-120, ly-40)]
    draw.polygon(beam_points, fill=(255, 255, 200, 100))
    
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 40)
    except:
        font = ImageFont.load_default()
    draw.text((WIDTH//2, HEIGHT-100), "康沃尔 - 悬崖", fill='#333333', font=font, anchor='mm')
    
    img.save(f"{output_dir}/cornwall-cliffs.png")
    print("✓ 已生成: cornwall-cliffs.png")

# ==================== 6. 湖区 - 湖泊 ====================
def draw_lake_district():
    img = create_sky_gradient()
    draw = ImageDraw.Draw(img)
    
    cx, cy = WIDTH//2, HEIGHT//2
    
    # 远山（分层）
    # 最远山
    draw.polygon([(0, cy+100), (WIDTH//4, cy-50), (WIDTH//2, cy-20), (3*WIDTH//4, cy-50), (WIDTH, cy+100)], 
                 fill='#9FA8DA')
    # 中山
    draw.polygon([(0, cy+150), (WIDTH//3, cy), (2*WIDTH//3, cy+20), (WIDTH, cy+150)], fill='#7986CB')
    # 近山
    draw.polygon([(0, cy+200), (WIDTH//4, cy+50), (WIDTH//2, cy+80), (3*WIDTH//4, cy+50), (WIDTH, cy+200)], 
                 fill='#5C6BC0')
    
    # 湖泊（镜面效果）
    lake_top = cy + 150
    for y in range(lake_top, HEIGHT):
        reflection = int(100 + (y - lake_top) * 0.3)
        draw.line([(0, y), (WIDTH, y)], fill=(100, 130, reflection+100))
    
    # 湖岸线
    draw.polygon([(0, HEIGHT), (0, lake_top), (WIDTH//3, lake_top+30), 
                  (2*WIDTH//3, lake_top-20), (WIDTH, lake_top+20), (WIDTH, HEIGHT)], fill='#64B5F6')
    
    # 湖中的可爱脸（水波中）
    face_x, face_y = WIDTH//2, lake_top + 100
    draw.ellipse([face_x-70, face_y-40, face_x+70, face_y+40], fill='#90CAF9')
    draw_cute_eyes(draw, face_x, face_y-10, 18)
    draw_cute_mouth(draw, face_x, face_y+25)
    draw_blush(draw, face_x, face_y)
    
    # 水波纹
    for i in range(5):
        y = lake_top + 50 + i * 60
        for wx in range(50, WIDTH, 150):
            draw.arc([wx, y-5, wx+60, y+5], 0, 180, fill='#BBDEFB', width=2)
    
    # 小船
    bx, by = WIDTH//3, lake_top + 80
    # 船身
    draw.ellipse([bx-40, by, bx+40, by+25], fill='#8D6E63')
    # 帆
    draw.polygon([(bx, by), (bx-25, by-50), (bx+25, by-50)], fill='white')
    draw.line([(bx, by), (bx, by-50)], fill='#5D4037', width=3)
    
    # 树木
    for tx in [50, WIDTH-100, 150, WIDTH-180]:
        ty = cy + 120
        # 树干
        draw.rectangle([tx-8, ty, tx+8, ty+60], fill='#5D4037')
        # 树冠（三层）
        draw.ellipse([tx-30, ty-40, tx+30, ty+10], fill='#4CAF50')
        draw.ellipse([tx-25, ty-60, tx+25, ty-10], fill='#66BB6A')
        draw.ellipse([tx-20, ty-75, tx+20, ty-25], fill='#81C784')
    
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 40)
    except:
        font = ImageFont.load_default()
    draw.text((WIDTH//2, HEIGHT-100), "湖区 - 湖泊", fill='#333333', font=font, anchor='mm')
    
    img.save(f"{output_dir}/lake-district.png")
    print("✓ 已生成: lake-district.png")

# ==================== 7. 约克郡 - 大教堂 ====================
def draw_yorkshire_cathedral():
    img = create_sky_gradient()
    draw = ImageDraw.Draw(img)
    
    cx, cy = WIDTH//2, HEIGHT//2 + 100
    base_y = cy + 200
    
    # 主教堂塔楼
    draw.rounded_rectangle([cx-80, base_y-350, cx+80, base_y], radius=10, fill='#D7CCC8')
    draw.rounded_rectangle([cx-80, base_y-350, cx+80, base_y], radius=10, outline='#8D6E63', width=4)
    
    # 可爱的脸
    draw_cute_eyes(draw, cx, base_y-200, 20)
    draw_cute_mouth(draw, cx, base_y-150)
    draw_blush(draw, cx, base_y-170)
    
    # 尖顶
    spire_points = [(cx-40, base_y-350), (cx, base_y-500), (cx+40, base_y-350)]
    draw.polygon(spire_points, fill='#5D4037')
    # 尖顶装饰线
    for i in range(5):
        y = base_y - 350 - i * 30
        w = 40 - i * 6
        draw.line([(cx-w, y), (cx+w, y)], fill='#3E2723', width=2)
    
    # 十字架
    draw.line([(cx, base_y-500), (cx, base_y-530)], fill='#FFD700', width=6)
    draw.line([(cx-15, base_y-515), (cx+15, base_y-515)], fill='#FFD700', width=6)
    
    # 双塔
    for offset in [-150, 150]:
        # 塔身
        draw.rounded_rectangle([cx+offset-50, base_y-250, cx+offset+50, base_y], radius=8, fill='#BCAAA4')
        # 塔顶
        draw.polygon([(cx+offset-55, base_y-250), (cx+offset, base_y-350), (cx+offset+55, base_y-250)], fill='#5D4037')
        # 小尖顶
        draw.polygon([(cx+offset-15, base_y-350), (cx+offset, base_y-400), (cx+offset+15, base_y-350)], fill='#4E342E')
        # 塔窗
        draw.ellipse([cx+offset-15, base_y-150, cx+offset+15, base_y-100], fill='#424242')
    
    # 主玫瑰窗（圆形花窗）
    rose_y = base_y - 250
    draw.ellipse([cx-50, rose_y-50, cx+50, rose_y+50], fill='#1976D2')
    # 花窗装饰
    for angle in range(0, 360, 45):
        rad = math.radians(angle)
        x1, y1 = cx, rose_y
        x2, y2 = cx + 45 * math.cos(rad), rose_y + 45 * math.sin(rad)
        draw.line([(x1, y1), (x2, y2)], fill='#BBDEFB', width=3)
    draw.ellipse([cx-15, rose_y-15, cx+15, rose_y+15], fill='#FFD700')
    
    # 主门
    draw.polygon([(cx-40, base_y), (cx, base_y-80), (cx+40, base_y)], fill='#5D4037')
    draw.ellipse([cx-15, base_y-60, cx+15, base_y], fill='#3E2723')
    
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 40)
    except:
        font = ImageFont.load_default()
    draw.text((WIDTH//2, HEIGHT-100), "约克郡 - 大教堂", fill='#333333', font=font, anchor='mm')
    
    img.save(f"{output_dir}/yorkshire-cathedral.png")
    print("✓ 已生成: yorkshire-cathedral.png")

# ==================== 8. 牛津 - 大学城 ====================
def draw_oxford_university():
    img = create_sky_gradient()
    draw = ImageDraw.Draw(img)
    
    cx, cy = WIDTH//2, HEIGHT//2 + 50
    base_y = cy + 250
    
    # 拉德克利夫图书馆圆顶（标志性）
    dome_center_y = base_y - 200
    
    # 圆柱基座
    draw.rounded_rectangle([cx-100, base_y-200, cx+100, base_y], radius=5, fill='#D7CCC8')
    draw.rounded_rectangle([cx-100, base_y-200, cx+100, base_y], radius=5, outline='#8D6E63', width=3)
    
    # 可爱的脸在圆柱上
    draw_cute_eyes(draw, cx, base_y-120, 18)
    draw_cute_mouth(draw, cx, base_y-80)
    draw_blush(draw, cx, base_y-100)
    
    # 圆顶
    draw.pieslice([cx-120, dome_center_y-120, cx+120, dome_center_y+80], 0, 180, fill='#8D6E63')
    # 圆顶纹理
    for i in range(6):
        angle = i * 30
        rad = math.radians(angle)
        x2 = cx + 100 * math.cos(rad)
        y2 = dome_center_y + 50 * math.sin(rad)
        draw.line([(cx, dome_center_y), (x2, y2)], fill='#5D4037', width=2)
    
    # 顶部小塔
    draw.polygon([(cx-20, dome_center_y-120), (cx, dome_center_y-180), (cx+20, dome_center_y-120)], fill='#5D4037')
    draw.ellipse([cx-8, dome_center_y-185, cx+8, dome_center_y-165], fill='#FFD700')
    
    # 柱子装饰
    for offset in [-70, -35, 35, 70]:
        draw.rectangle([cx+offset-8, base_y-180, cx+offset+8, base_y], fill='#BCAAA4')
    
    # 背景建筑（梦幻学院风格）
    # 左侧建筑
    draw.rounded_rectangle([cx-200, base_y-150, cx-120, base_y], radius=5, fill='#A1887F')
    draw.polygon([(cx-205, base_y-150), (cx-160, base_y-220), (cx-115, base_y-150)], fill='#5D4037')
    # 右侧建筑
    draw.rounded_rectangle([cx+120, base_y-150, cx+200, base_y], radius=5, fill='#A1887F')
    draw.polygon([(cx+115, base_y-150), (cx+160, base_y-220), (cx+205, base_y-150)], fill='#5D4037')
    
    # 牛津标志性尖塔
    for offset in [-180, 180]:
        draw.polygon([(cx+offset-10, base_y-220), (cx+offset, base_y-300), (cx+offset+10, base_y-220)], fill='#4E342E')
    
    # 树木（学院庭院风格）
    for tx in [80, WIDTH-80]:
        # 树冠
        draw.ellipse([tx-40, base_y-100, tx+40, base_y-20], fill='#4CAF50')
        draw.ellipse([tx-30, base_y-130, tx+30, base_y-50], fill='#66BB6A')
        # 树干
        draw.rectangle([tx-10, base_y-40, tx+10, base_y], fill='#5D4037')
    
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 40)
    except:
        font = ImageFont.load_default()
    draw.text((WIDTH//2, HEIGHT-100), "牛津 - 大学城", fill='#333333', font=font, anchor='mm')
    
    img.save(f"{output_dir}/oxford-university.png")
    print("✓ 已生成: oxford-university.png")

# ==================== 9. 剑桥 - 剑桥大学 ====================
def draw_cambridge_university():
    img = create_sky_gradient()
    draw = ImageDraw.Draw(img)
    
    cx, cy = WIDTH//2, HEIGHT//2 + 50
    base_y = cy + 250
    
    # 国王学院礼拜堂（哥特式）
    # 主建筑
    draw.rounded_rectangle([cx-90, base_y-300, cx+90, base_y], radius=5, fill='#FFECB3')
    draw.rounded_rectangle([cx-90, base_y-300, cx+90, base_y], radius=5, outline='#FFB300', width=3)
    
    # 可爱的脸
    draw_cute_eyes(draw, cx, base_y-180, 20)
    draw_cute_mouth(draw, cx, base_y-130)
    draw_blush(draw, cx, base_y-150)
    
    # 扇形拱顶天花板（外显的装饰）
    ceiling_y = base_y - 300
    # 大扇形
    draw.pieslice([cx-100, ceiling_y-20, cx+100, ceiling_y+80], 0, 180, fill='#FFE082')
    # 扇骨
    for i in range(7):
        angle = -60 + i * 20
        rad = math.radians(angle)
        x1 = cx + 20 * math.cos(rad)
        y1 = ceiling_y + 10 * math.sin(rad)
        x2 = cx + 90 * math.cos(rad)
        y2 = ceiling_y + 60 * math.sin(rad)
        draw.line([(x1, y1), (x2, y2)], fill='#FFB300', width=3)
    
    # 尖塔
    draw.polygon([(cx-30, ceiling_y), (cx, ceiling_y-150), (cx+30, ceiling_y)], fill='#FFB300')
    # 尖塔上的装饰
    for i in range(4):
        y = ceiling_y - 30 - i * 30
        w = 25 - i * 5
        draw.line([(cx-w, y), (cx+w, y)], fill='#FF8F00', width=2)
    
    # 大窗户（哥特式）
    window_y = base_y - 220
    # 拱形窗
    draw.pieslice([cx-50, window_y-60, cx+50, window_y+40], 0, 180, fill='#42A5F5')
    # 窗棂
    draw.line([(cx, window_y-60), (cx, window_y+40)], fill='#FFB300', width=3)
    draw.line([(cx-30, window_y-30), (cx+30, window_y-30)], fill='#FFB300', width=3)
    draw.line([(cx-20, window_y-10), (cx+20, window_y-10)], fill='#FFB300', width=2)
    
    # 侧塔
    for offset in [-130, 130]:
        draw.rounded_rectangle([cx+offset-40, base_y-200, cx+offset+40, base_y], radius=5, fill='#FFE0B2')
        draw.polygon([(cx+offset-45, base_y-200), (cx+offset, base_y-280), (cx+offset+45, base_y-200)], fill='#FFB74D')
        # 小尖顶
        draw.polygon([(cx+offset-10, base_y-280), (cx+offset, base_y-330), (cx+offset+10, base_y-280)], fill='#F57C00')
    
    # 康河上的桥（数学桥）
    bridge_y = base_y + 30
    # 桥拱
    draw.arc([cx-180, bridge_y-40, cx+180, bridge_y+40], 0, 180, fill='#8D6E63', width=15)
    # 桥栏杆
    for i in range(-4, 5):
        x = cx + i * 40
        draw.line([(x, bridge_y-35), (x, bridge_y-60)], fill='#6D4C41', width=4)
    draw.line([(cx-160, bridge_y-55), (cx+160, bridge_y-55)], fill='#6D4C41', width=4)
    
    # 桥下的水
    for y in range(int(bridge_y+30), HEIGHT):
        draw.line([(0, y), (WIDTH, y)], fill=(100, 150, 200+y//10))
    
    # 小船（punt）
    punt_x, punt_y = cx + 100, bridge_y + 60
    draw.ellipse([punt_x-50, punt_y, punt_x+50, punt_y+20], fill='#8D6E63')
    # 船夫
    draw.ellipse([punt_x-10, punt_y-25, punt_x+10, punt_y-5], fill='#FFCC80')
    # 船篙
    draw.line([(punt_x, punt_y-15), (punt_x+30, punt_y-50)], fill='#5D4037', width=3)
    
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 40)
    except:
        font = ImageFont.load_default()
    draw.text((WIDTH//2, HEIGHT-100), "剑桥 - 剑桥大学", fill='#333333', font=font, anchor='mm')
    
    img.save(f"{output_dir}/cambridge-university.png")
    print("✓ 已生成: cambridge-university.png")

# ==================== 10. 巴斯 - 罗马浴场 ====================
def draw_bath_roman():
    img = create_sky_gradient()
    draw = ImageDraw.Draw(img)
    
    cx, cy = WIDTH//2, HEIGHT//2
    base_y = cy + 200
    
    # 浴场主建筑（半圆形）
    # 后方柱廊
    for i in range(9):
        x = cx - 200 + i * 50
        # 柱子
        draw.rounded_rectangle([x-12, base_y-180, x+12, base_y], radius=3, fill='#D7CCC8')
        draw.rounded_rectangle([x-12, base_y-180, x+12, base_y], radius=3, outline='#8D6E63', width=2)
        # 柱头
        draw.rectangle([x-18, base_y-200, x+18, base_y-180], fill='#BCAAA4')
    
    # 柱顶横梁
    draw.rounded_rectangle([cx-230, base_y-230, cx+230, base_y-200], radius=5, fill='#A1887F')
    
    # 三角门楣
    draw.polygon([(cx-200, base_y-230), (cx, base_y-320), (cx+200, base_y-230)], fill='#D7CCC8')
    draw.polygon([(cx-200, base_y-230), (cx, base_y-320), (cx+200, base_y-230)], outline='#8D6E63', width=3)
    
    # 可爱的脸在门楣上
    draw_cute_eyes(draw, cx, base_y-270, 18)
    draw_cute_mouth(draw, cx, base_y-240)
    draw_blush(draw, cx, base_y-255)
    
    # 浴场主池（翡翠绿色）
    pool_y = base_y + 50
    # 池边
    draw.rounded_rectangle([cx-220, pool_y-30, cx+220, pool_y+120], radius=20, fill='#E0E0E0')
    # 池水
    draw.rounded_rectangle([cx-200, pool_y-10, cx+200, pool_y+100], radius=15, fill='#4CAF50')
    
    # 水波纹
    for i in range(4):
        y = pool_y + 20 + i * 20
        for wx in range(int(cx-180), int(cx+180), 80):
            draw.arc([wx, y-5, wx+40, y+5], 0, 180, fill='#81C784', width=2)
    
    # 蒸汽（可爱的云朵状）
    for i in range(5):
        sx = cx - 150 + i * 75
        sy = pool_y - 60 - (i % 2) * 20
        draw.ellipse([sx-25, sy-15, sx+25, sy+15], fill=(255, 255, 255, 180))
        draw.ellipse([sx-15, sy-25, sx+15, sy+5], fill=(255, 255, 255, 200))
    
    # 台阶
    for i in range(5):
        y = base_y - i * 15
        alpha = 1 - i * 0.15
        color = (int(215*alpha), int(204*alpha), int(200*alpha))
        draw.line([(cx-150, y), (cx+150, y)], fill=color, width=10)
    
    # 罗马柱（前景）
    for offset in [-180, 180]:
        draw.rounded_rectangle([cx+offset-15, base_y-100, cx+offset+15, base_y+50], radius=3, fill='#D7CCC8')
        draw.ellipse([cx+offset-20, base_y-110, cx+offset+20, base_y-90], fill='#BCAAA4')
    
    # 雕像（简化版）
    statue_x = cx
    # 基座
    draw.rectangle([statue_x-30, base_y-250, statue_x+30, base_y-230], fill='#8D6E63')
    # 身体
    draw.ellipse([statue_x-20, base_y-280, statue_x+20, base_y-240], fill='#D7CCC8')
    # 头
    draw.ellipse([statue_x-12, base_y-300, statue_x+12, base_y-275], fill='#FFCC80')
    
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 40)
    except:
        font = ImageFont.load_default()
    draw.text((WIDTH//2, HEIGHT-100), "巴斯 - 罗马浴场", fill='#333333', font=font, anchor='mm')
    
    img.save(f"{output_dir}/bath-roman.png")
    print("✓ 已生成: bath-roman.png")

# ==================== 主程序 ====================
if __name__ == "__main__":
    print("=" * 50)
    print("正在生成英国地区卡通塔图片...")
    print("=" * 50)
    
    draw_london_eye()
    draw_edinburgh_castle()
    draw_cardiff_castle()
    draw_giants_causeway()
    draw_cornwall_cliffs()
    draw_lake_district()
    draw_yorkshire_cathedral()
    draw_oxford_university()
    draw_cambridge_university()
    draw_bath_roman()
    
    print("=" * 50)
    print("✅ 所有图片生成完成！")
    print(f"📁 保存位置: {output_dir}")
    print("=" * 50)