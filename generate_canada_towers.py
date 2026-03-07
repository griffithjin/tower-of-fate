#!/usr/bin/env python3
"""
生成加拿大各省卡通塔图片 - 愤怒的小鸟风格
尺寸：800x1200像素
"""

from PIL import Image, ImageDraw, ImageFont
import math
import os

# 输出目录
OUTPUT_DIR = "/Users/moutai/Desktop/toweroffate_v1.0/assets/towers/states/canada/"

# 图片尺寸
WIDTH = 800
HEIGHT = 1200

def create_gradient_background(draw, width, height):
    """创建天蓝色渐变背景"""
    for y in range(height):
        # 从天蓝色渐变到浅蓝色
        ratio = y / height
        r = int(135 - ratio * 40)  # 135 -> 95
        g = int(206 - ratio * 30)  # 206 -> 176
        b = int(235 - ratio * 20)  # 235 -> 215
        draw.line([(0, y), (width, y)], fill=(r, g, b))

def draw_angry_eyes(draw, x, y, size=30, look_direction=(0, 0)):
    """绘制愤怒的小鸟风格的眼睛"""
    # 左眼
    draw.ellipse([x-size, y-size, x+size, y+size], fill="white", outline="black", width=2)
    draw.ellipse([x-size*0.3+look_direction[0]*5, y-size*0.3+look_direction[1]*5, 
                  x+size*0.3+look_direction[0]*5, y+size*0.3+look_direction[1]*5], fill="black")
    
    # 右眼
    draw.ellipse([x+size*2, y-size, x+size*4, y+size], fill="white", outline="black", width=2)
    draw.ellipse([x+size*2.7+look_direction[0]*5, y-size*0.3+look_direction[1]*5, 
                  x+size*3.3+look_direction[0]*5, y+size*0.3+look_direction[1]*5], fill="black")

def draw_cute_eyebrows(draw, x, y, size=35):
    """绘制可爱的粗眉毛"""
    # 左眉毛
    draw.polygon([
        (x-size, y-size*0.5), (x+size*0.5, y-size), (x+size*0.8, y-size*0.3)
    ], fill="black")
    # 右眉毛
    draw.polygon([
        (x+size*2.5, y-size*0.3), (x+size*3.5, y-size), (x+size*4.5, y-size*0.5)
    ], fill="black")

def draw_cute_beak(draw, x, y, size=25):
    """绘制可爱的鸟嘴"""
    draw.polygon([
        (x, y), (x-size, y+size), (x+size, y+size)
    ], fill="orange", outline="black")
    draw.polygon([
        (x-size*0.5, y+size), (x+size*0.5, y+size), (x, y+size*1.5)
    ], fill="darkorange", outline="black")

def draw_cute_mouth(draw, x, y, size=20):
    """绘制可爱的微笑嘴巴"""
    draw.arc([x-size, y-size, x+size, y+size], start=0, end=180, fill="black", width=3)

def draw_rosy_cheeks(draw, x, y, size=15):
    """绘制腮红"""
    draw.ellipse([x-size, y-size, x+size, y+size], fill=(255, 182, 193, 128))

def draw_clouds(draw):
    """绘制装饰云朵"""
    clouds = [
        (100, 150, 60), (300, 100, 80), (600, 200, 50),
        (150, 400, 45), (650, 500, 70), (200, 800, 55)
    ]
    for cx, cy, size in clouds:
        draw.ellipse([cx-size, cy-size*0.6, cx+size, cy+size*0.6], fill=(255, 255, 255, 180))
        draw.ellipse([cx-size*0.7, cy-size, cx+size*0.7, cy+size], fill=(255, 255, 255, 180))

def create_base_image():
    """创建带渐变背景的基础图片"""
    img = Image.new('RGBA', (WIDTH, HEIGHT), (135, 206, 235))
    draw = ImageDraw.Draw(img)
    create_gradient_background(draw, WIDTH, HEIGHT)
    draw_clouds(draw)
    return img, draw

# ============ 各省塔绘制函数 ============

def draw_ontario_cn_tower():
    """安大略 - CN塔"""
    img, draw = create_base_image()
    cx, cy = WIDTH // 2, HEIGHT // 2 + 100
    
    # CN塔主体 - 圆润卡通风格
    # 塔基
    draw.rounded_rectangle([cx-80, cy+200, cx+80, cy+350], radius=20, fill="lightgray", outline="black", width=3)
    # 塔身 - 逐渐变细
    draw.polygon([
        (cx-60, cy+200), (cx+60, cy+200), (cx+40, cy-100), (cx-40, cy-100)
    ], fill="silver", outline="black", width=3)
    # 观景台
    draw.rounded_rectangle([cx-70, cy-120, cx+70, cy-80], radius=15, fill="lightblue", outline="black", width=3)
    # 天线
    draw.rectangle([cx-5, cy-300, cx+5, cy-120], fill="red", outline="black", width=2)
    draw.ellipse([cx-15, cy-320, cx+15, cy-290], fill="red", outline="black", width=2)
    
    # 可爱的脸
    draw_angry_eyes(draw, cx-35, cy, look_direction=(0.5, -0.3))
    draw_cute_eyebrows(draw, cx-35, cy-40)
    draw_cute_beak(draw, cx, cy+20, size=20)
    draw_rosy_cheeks(draw, cx-55, cy+10)
    draw_rosy_cheeks(draw, cx+55, cy+10)
    
    return img

def draw_quebec_old_city():
    """魁北克 - 老城塔楼"""
    img, draw = create_base_image()
    cx, cy = WIDTH // 2, HEIGHT // 2 + 50
    
    # 复古欧洲风格塔楼
    # 塔身
    draw.rounded_rectangle([cx-70, cy, cx+70, cy+300], radius=15, fill="tan", outline="black", width=3)
    # 石砖纹理
    for i in range(8):
        y = cy + 30 + i * 35
        draw.line([(cx-65, y), (cx+65, y)], fill="saddlebrown", width=1)
    # 塔顶 - 蓝色尖顶
    draw.polygon([
        (cx-90, cy), (cx+90, cy), (cx, cy-180)
    ], fill="darkblue", outline="black", width=3)
    # 尖顶装饰
    draw.ellipse([cx-10, cy-200, cx+10, cy-180], fill="gold", outline="black", width=2)
    
    # 可爱的脸
    draw_angry_eyes(draw, cx-30, cy+80, look_direction=(-0.3, 0))
    draw_cute_eyebrows(draw, cx-30, cy+40)
    draw_cute_mouth(draw, cx, cy+120)
    draw_rosy_cheeks(draw, cx-50, cy+90)
    draw_rosy_cheeks(draw, cx+50, cy+90)
    
    # 旗帜
    draw.line([(cx, cy-180), (cx, cy-220)], fill="brown", width=3)
    draw.polygon([
        (cx, cy-220), (cx+40, cy-210), (cx, cy-200)
    ], fill="blue", outline="black", width=1)
    
    return img

def draw_bc_banff():
    """不列颠哥伦比亚 - 班夫山脉塔"""
    img, draw = create_base_image()
    cx, cy = WIDTH // 2, HEIGHT // 2 + 100
    
    # 山形塔 - 班夫风格
    # 主峰
    draw.polygon([
        (cx-100, cy+250), (cx+100, cy+250), (cx, cy-150)
    ], fill="darkgreen", outline="black", width=3)
    # 雪顶
    draw.polygon([
        (cx-40, cy-50), (cx+40, cy-50), (cx, cy-150)
    ], fill="white", outline="black", width=2)
    # 侧峰
    draw.polygon([
        (cx-150, cy+250), (cx-50, cy+250), (cx-100, cy+50)
    ], fill="forestgreen", outline="black", width=3)
    draw.polygon([
        (cx+50, cy+250), (cx+150, cy+250), (cx+100, cy+50)
    ], fill="forestgreen", outline="black", width=3)
    
    # 可爱的脸 - 在主峰上
    draw_angry_eyes(draw, cx-30, cy+50, size=25, look_direction=(0, 0.3))
    draw_cute_eyebrows(draw, cx-30, cy+15)
    draw_cute_mouth(draw, cx, cy+85)
    draw_rosy_cheeks(draw, cx-45, cy+60)
    draw_rosy_cheeks(draw, cx+45, cy+60)
    
    # 松树装饰
    for px in [cx-120, cx-80, cx+80, cx+120]:
        draw.polygon([
            (px, cy+200), (px-15, cy+250), (px+15, cy+250)
        ], fill="darkgreen", outline="black", width=1)
    
    return img

def draw_alberta_stampede():
    """阿尔伯塔 - 牛仔节塔"""
    img, draw = create_base_image()
    cx, cy = WIDTH // 2, HEIGHT // 2 + 80
    
    # 牛仔竞技场塔
    # 主塔身 - 红色谷仓风格
    draw.rounded_rectangle([cx-90, cy, cx+90, cy+280], radius=20, fill="firebrick", outline="black", width=3)
    # 屋顶
    draw.polygon([
        (cx-110, cy), (cx+110, cy), (cx, cy-80)
    ], fill="darkred", outline="black", width=3)
    # 白色装饰条
    draw.rectangle([cx-90, cy+80, cx+90, cy+100], fill="white", outline="black", width=1)
    draw.rectangle([cx-90, cy+180, cx+90, cy+200], fill="white", outline="black", width=1)
    
    # 可爱的脸
    draw_angry_eyes(draw, cx-35, cy+50, look_direction=(0.2, -0.2))
    draw_cute_eyebrows(draw, cx-35, cy+10)
    draw_cute_beak(draw, cx, cy+70, size=22)
    draw_rosy_cheeks(draw, cx-55, cy+60)
    draw_rosy_cheeks(draw, cx+55, cy+60)
    
    # 牛仔帽
    draw.ellipse([cx-70, cy-60, cx+70, cy-20], fill="saddlebrown", outline="black", width=2)
    draw.ellipse([cx-40, cy-90, cx+40, cy-30], fill="saddlebrown", outline="black", width=2)
    
    return img

def draw_manitoba_polar_bear():
    """曼尼托巴 - 北极熊塔"""
    img, draw = create_base_image()
    cx, cy = WIDTH // 2, HEIGHT // 2 + 50
    
    # 北极熊形状塔
    # 身体
    draw.rounded_rectangle([cx-100, cy, cx+100, cy+280], radius=50, fill="white", outline="black", width=3)
    # 头部
    draw.ellipse([cx-70, cy-100, cx+70, cy+40], fill="white", outline="black", width=3)
    # 耳朵
    draw.ellipse([cx-80, cy-110, cx-40, cy-70], fill="white", outline="black", width=2)
    draw.ellipse([cx+40, cy-110, cx+80, cy-70], fill="white", outline="black", width=2)
    # 内耳
    draw.ellipse([cx-70, cy-105, cx-50, cy-85], fill="pink")
    draw.ellipse([cx+50, cy-105, cx+70, cy-85], fill="pink")
    
    # 可爱的脸
    draw_angry_eyes(draw, cx-25, cy-30, size=22, look_direction=(0, 0))
    draw_cute_eyebrows(draw, cx-25, cy-60)
    # 熊鼻子
    draw.ellipse([cx-12, cy+5, cx+12, cy+25], fill="black")
    draw.ellipse([cx-5, cy+8, cx+5, cy+18], fill="gray")
    draw_cute_mouth(draw, cx, cy+30)
    draw_rosy_cheeks(draw, cx-40, cy-10)
    draw_rosy_cheeks(draw, cx+40, cy-10)
    
    # 爪子
    draw.ellipse([cx-90, cy+200, cx-40, cy+250], fill="white", outline="black", width=2)
    draw.ellipse([cx+40, cy+200, cx+90, cy+250], fill="white", outline="black", width=2)
    
    return img

def draw_saskatchewan_wheat():
    """萨斯喀彻温 - 麦田塔"""
    img, draw = create_base_image()
    cx, cy = WIDTH // 2, HEIGHT // 2 + 80
    
    # 麦穗塔
    # 主茎
    draw.rounded_rectangle([cx-30, cy-100, cx+30, cy+250], radius=15, fill="gold", outline="black", width=3)
    draw.line([(cx-10, cy-100), (cx-10, cy+250)], fill="orange", width=2)
    draw.line([(cx+10, cy-100), (cx+10, cy+250)], fill="orange", width=2)
    
    # 麦粒 - 螺旋排列
    for i in range(12):
        y = cy + 200 - i * 28
        offset = (i % 2) * 15
        # 左麦粒
        draw.ellipse([cx-55-offset, y-12, cx-15-offset, y+12], fill="gold", outline="black", width=1)
        # 右麦粒
        draw.ellipse([cx+15+offset, y-12, cx+55+offset, y+12], fill="gold", outline="black", width=1)
        # 中间麦粒
        draw.ellipse([cx-18, y-12, cx+18, y+12], fill="goldenrod", outline="black", width=1)
    
    # 顶部麦芒
    for angle in [-30, -15, 0, 15, 30]:
        rad = math.radians(angle)
        x2 = cx + math.sin(rad) * 80
        y2 = cy - 100 - math.cos(rad) * 80
        draw.line([(cx, cy-100), (x2, y2)], fill="gold", width=3)
    
    # 可爱的脸
    draw_angry_eyes(draw, cx-25, cy+100, size=25, look_direction=(0, 0))
    draw_cute_eyebrows(draw, cx-25, cy+65)
    draw_cute_mouth(draw, cx, cy+140)
    draw_rosy_cheeks(draw, cx-45, cy+110)
    draw_rosy_cheeks(draw, cx+45, cy+110)
    
    return img

def draw_nova_scotia_peggy():
    """新斯科舍 - 佩吉湾灯塔"""
    img, draw = create_base_image()
    cx, cy = WIDTH // 2, HEIGHT // 2 + 80
    
    # 佩吉湾灯塔
    # 塔身 - 八边形效果（用圆润矩形）
    draw.rounded_rectangle([cx-75, cy, cx+75, cy+280], radius=20, fill="white", outline="black", width=3)
    # 红白相间条纹
    for i, y in enumerate([cy+40, cy+120, cy+200]):
        color = "firebrick" if i % 2 == 0 else "white"
        draw.rounded_rectangle([cx-75, y, cx+75, y+60], radius=10, fill=color, outline="black", width=2)
    
    # 灯室
    draw.rounded_rectangle([cx-50, cy-60, cx+50, cy], radius=10, fill="lightblue", outline="black", width=2)
    # 屋顶
    draw.polygon([
        (cx-60, cy-60), (cx+60, cy-60), (cx, cy-120)
    ], fill="darkred", outline="black", width=2)
    
    # 灯光效果
    draw.polygon([
        (cx, cy-30), (cx-80, cy-150), (cx+80, cy-150)
    ], fill=(255, 255, 200, 100))
    
    # 可爱的脸
    draw_angry_eyes(draw, cx-25, cy+80, size=22, look_direction=(0.3, 0))
    draw_cute_eyebrows(draw, cx-25, cy+45)
    draw_cute_beak(draw, cx, cy+100, size=18)
    draw_rosy_cheeks(draw, cx-45, cy+90)
    draw_rosy_cheeks(draw, cx+45, cy+90)
    
    return img

def draw_newfoundland_iceberg():
    """纽芬兰 - 冰山塔"""
    img, draw = create_base_image()
    cx, cy = WIDTH // 2, HEIGHT // 2 + 100
    
    # 冰山形状塔
    # 主体冰山
    points = [
        (cx-120, cy+300),  # 左底
        (cx-80, cy+150),   # 左中
        (cx-100, cy+50),   # 左上凹
        (cx-60, cy-50),    # 左上峰
        (cx-20, cy+20),    # 中间凹
        (cx, cy-100),      # 最高峰
        (cx+30, cy+10),    # 右中凹
        (cx+90, cy-30),    # 右上峰
        (cx+70, cy+100),   # 右上凹
        (cx+130, cy+300),  # 右底
    ]
    draw.polygon(points, fill="lightcyan", outline="black", width=3)
    
    # 冰蓝色阴影
    shadow_points = [
        (cx-80, cy+300),
        (cx-40, cy+200),
        (cx-60, cy+100),
        (cx-20, cy+150),
        (cx, cy+80),
        (cx+40, cy+200),
        (cx+80, cy+300)
    ]
    draw.polygon(shadow_points, fill=(173, 216, 230))
    
    # 可爱的脸
    draw_angry_eyes(draw, cx-25, cy+80, size=25, look_direction=(-0.2, -0.2))
    draw_cute_eyebrows(draw, cx-25, cy+45)
    draw_cute_mouth(draw, cx, cy+120)
    draw_rosy_cheeks(draw, cx-45, cy+90)
    draw_rosy_cheeks(draw, cx+45, cy+90)
    
    return img

def draw_new_brunswick_fundy():
    """新不伦瑞克 - 芬迪湾潮汐塔"""
    img, draw = create_base_image()
    cx, cy = WIDTH // 2, HEIGHT // 2 + 80
    
    # 潮汐观测塔
    # 塔基 - 在水中
    draw.rounded_rectangle([cx-90, cy+150, cx+90, cy+300], radius=20, fill="slategray", outline="black", width=3)
    # 塔身
    draw.rounded_rectangle([cx-60, cy-50, cx+60, cy+150], radius=15, fill="lightsteelblue", outline="black", width=3)
    # 观测台
    draw.rounded_rectangle([cx-80, cy-100, cx+80, cy-50], radius=10, fill="steelblue", outline="black", width=3)
    # 屋顶
    draw.polygon([
        (cx-70, cy-100), (cx+70, cy-100), (cx, cy-160)
    ], fill="darkslategray", outline="black", width=2)
    
    # 水波纹
    for i, wy in enumerate([cy+220, cy+250, cy+280]):
        for wx in [cx-60, cx, cx+60]:
            draw.arc([wx-30, wy-10, wx+30, wy+10], start=0, end=180, fill="blue", width=2)
    
    # 可爱的脸
    draw_angry_eyes(draw, cx-25, cy+20, size=25, look_direction=(0, 0.2))
    draw_cute_eyebrows(draw, cx-25, cy-15)
    draw_cute_beak(draw, cx, cy+45, size=20)
    draw_rosy_cheeks(draw, cx-45, cy+30)
    draw_rosy_cheeks(draw, cx+45, cy+30)
    
    return img

def draw_pei_green_gables():
    """爱德华王子岛 - 绿山墙"""
    img, draw = create_base_image()
    cx, cy = WIDTH // 2, HEIGHT // 2 + 80
    
    # 绿山墙房子塔
    # 主房
    draw.rounded_rectangle([cx-100, cy, cx+100, cy+280], radius=15, fill="wheat", outline="black", width=3)
    # 绿色屋顶（山墙）
    draw.polygon([
        (cx-130, cy), (cx+130, cy), (cx, cy-100)
    ], fill="forestgreen", outline="black", width=3)
    # 屋顶窗
    draw.ellipse([cx-25, cy-60, cx+25, cy-20], fill="lightyellow", outline="black", width=2)
    # 窗户
    draw.rectangle([cx-60, cy+50, cx-20, cy+120], fill="lightyellow", outline="black", width=2)
    draw.rectangle([cx+20, cy+50, cx+60, cy+120], fill="lightyellow", outline="black", width=2)
    draw.line([(cx-40, cy+50), (cx-40, cy+120)], fill="black", width=1)
    draw.line([(cx-60, cy+85), (cx-20, cy+85)], fill="black", width=1)
    draw.line([(cx+40, cy+50), (cx+40, cy+120)], fill="black", width=1)
    draw.line([(cx+20, cy+85), (cx+60, cy+85)], fill="black", width=1)
    
    # 门
    draw.rounded_rectangle([cx-25, cy+160, cx+25, cy+280], radius=5, fill="sienna", outline="black", width=2)
    draw.ellipse([cx+10, cy+220, cx+18, cy+228], fill="gold")
    
    # 可爱的脸 - 在屋顶下方
    draw_angry_eyes(draw, cx-30, cy+30, size=22, look_direction=(0, 0))
    draw_cute_eyebrows(draw, cx-30, cy-5)
    draw_cute_mouth(draw, cx, cy+65)
    draw_rosy_cheeks(draw, cx-50, cy+40)
    draw_rosy_cheeks(draw, cx+50, cy+40)
    
    # 烟囱
    draw.rectangle([cx+60, cy-80, cx+90, cy-40], fill="firebrick", outline="black", width=2)
    # 炊烟
    for i, (sx, sy) in enumerate([(cx+75, cy-100), (cx+85, cy-130), (cx+70, cy-160)]):
        size = 8 + i * 3
        draw.ellipse([sx-size, sy-size, sx+size, sy+size], fill=(200, 200, 200, 150))
    
    return img

# ============ 主程序 ============

def main():
    towers = [
        ("ontario-cn-tower.png", draw_ontario_cn_tower),
        ("quebec-old-city.png", draw_quebec_old_city),
        ("bc-banff.png", draw_bc_banff),
        ("alberta-stampede.png", draw_alberta_stampede),
        ("manitoba-polar-bear.png", draw_manitoba_polar_bear),
        ("saskatchewan-wheat.png", draw_saskatchewan_wheat),
        ("nova-scotia-peggy.png", draw_nova_scotia_peggy),
        ("newfoundland-iceberg.png", draw_newfoundland_iceberg),
        ("new-brunswick-fundy.png", draw_new_brunswick_fundy),
        ("pei-green-gables.png", draw_pei_green_gables),
    ]
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    for filename, draw_func in towers:
        print(f"正在生成: {filename}")
        img = draw_func()
        filepath = os.path.join(OUTPUT_DIR, filename)
        # 转换为RGB保存为PNG（去除透明通道）
        img_rgb = Image.new('RGB', img.size, (135, 206, 235))
        img_rgb.paste(img, mask=img.split()[3] if img.mode == 'RGBA' else None)
        img_rgb.save(filepath, 'PNG')
        print(f"  ✓ 已保存: {filepath}")
    
    print(f"\n完成！共生成 {len(towers)} 个塔图片")
    print(f"保存位置: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
