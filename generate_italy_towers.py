#!/usr/bin/env python3
"""
生成意大利大区卡通塔图片
风格：愤怒的小鸟卡通风格，可爱表情
"""

from PIL import Image, ImageDraw, ImageFilter
import os
import math

# 输出目录
OUTPUT_DIR = "/Users/moutai/Desktop/toweroffate_v1.0/assets/towers/states/italy/"

# 图片尺寸
WIDTH, HEIGHT = 800, 1200

def create_gradient_background(width, height):
    """创建天蓝色渐变背景"""
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    
    # 天蓝色渐变：从浅蓝到稍深的蓝色
    for y in range(height):
        # 渐变比例
        ratio = y / height
        # 浅天蓝 (135, 206, 235) 到 稍深的天蓝 (70, 130, 180)
        r = int(135 - ratio * 65)
        g = int(206 - ratio * 76)
        b = int(235 - ratio * 55)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    return img

def draw_circle_eye(draw, x, y, size, looking_direction="front"):
    """绘制卡通眼睛"""
    # 眼白
    draw.ellipse([x-size, y-size, x+size, y+size], fill=(255, 255, 255), outline=(0, 0, 0), width=3)
    # 瞳孔
    if looking_direction == "left":
        draw.ellipse([x-size//3, y, x+size//3, y+size//2], fill=(0, 0, 0))
    elif looking_direction == "right":
        draw.ellipse([x-size//3, y, x+size//3, y+size//2], fill=(0, 0, 0))
    else:
        draw.ellipse([x-size//4, y-size//4, x+size//4, y+size//4], fill=(0, 0, 0))

def draw_cute_mouth(draw, x, y, size, happy=True):
    """绘制可爱的嘴巴"""
    if happy:
        # 微笑
        draw.arc([x-size, y-size//2, x+size, y+size], start=0, end=180, fill=(0, 0, 0), width=3)
    else:
        # 小圆圈嘴
        draw.ellipse([x-size//2, y, x+size//2, y+size], fill=(200, 50, 50), outline=(0, 0, 0), width=2)

def draw_blush(draw, x, y, size):
    """绘制腮红"""
    draw.ellipse([x-size, y-size//2, x+size, y+size//2], fill=(255, 150, 150, 128))

def draw_rounded_rect(draw, xy, radius, fill, outline=None, width=1):
    """绘制圆角矩形"""
    x1, y1, x2, y2 = xy
    # 主体矩形
    draw.rectangle([x1+radius, y1, x2-radius, y2], fill=fill)
    draw.rectangle([x1, y1+radius, x2, y2-radius], fill=fill)
    # 四个角
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

def draw_cloud(draw, x, y, size):
    """绘制云朵"""
    color = (255, 255, 255, 200)
    draw.ellipse([x-size, y-size//2, x+size, y+size//2], fill=color)
    draw.ellipse([x-size//2, y-size, x+size//2, y+size], fill=color)
    draw.ellipse([x, y-size//2, x+size, y+size//2], fill=color)

# ==================== 1. 伦巴第 - 米兰大教堂 ====================
def draw_lombardy():
    """绘制伦巴第塔 - 米兰大教堂"""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    
    # 绘制几朵云
    draw_cloud(draw, 150, 150, 60)
    draw_cloud(draw, 600, 200, 50)
    draw_cloud(draw, 400, 100, 40)
    
    cx, cy = WIDTH // 2, HEIGHT // 2 + 100
    
    # 塔身 - 教堂风格，卡通化
    base_color = (180, 160, 140)  # 石质颜色
    roof_color = (139, 69, 19)    # 棕色屋顶
    
    # 主体建筑 - 圆角卡通风格
    body_width, body_height = 300, 350
    draw_rounded_rect(draw, [cx-body_width//2, cy-body_height//2+100, 
                              cx+body_width//2, cy+body_height//2+100], 
                      30, base_color, (0, 0, 0), 3)
    
    # 教堂尖顶
    draw.polygon([(cx-80, cy-75), (cx, cy-250), (cx+80, cy-75)], 
                 fill=roof_color, outline=(0, 0, 0), width=3)
    
    # 小尖塔装饰
    for i in range(-2, 3):
        x = cx + i * 50
        draw.polygon([(x-15, cy-75), (x, cy-150), (x+15, cy-75)], 
                     fill=roof_color, outline=(0, 0, 0), width=2)
    
    # 大门
    draw.arc([cx-60, cy+50, cx+60, cy+200], 0, 180, fill=(80, 50, 30), width=40)
    
    # 窗户（可爱的表情区域）
    # 左眼
    draw_circle_eye(draw, cx-50, cy-20, 25, "left")
    # 右眼
    draw_circle_eye(draw, cx+50, cy-20, 25, "right")
    # 微笑
    draw_cute_mouth(draw, cx, cy+30, 30, happy=True)
    
    # 腮红
    draw.ellipse([cx-90, cy-10, cx-60, cy+15], fill=(255, 150, 150))
    draw.ellipse([cx+60, cy-10, cx+90, cy+15], fill=(255, 150, 150))
    
    # 十字架
    draw.line([(cx, cy-250), (cx, cy-290)], fill=(255, 215, 0), width=8)
    draw.line([(cx-20, cy-270), (cx+20, cy-270)], fill=(255, 215, 0), width=8)
    
    img.save(os.path.join(OUTPUT_DIR, "lombardy-milan.png"))
    print("✓ lombardy-milan.png 已生成")

# ==================== 2. 拉齐奥 - 斗兽场 ====================
def draw_lazio():
    """绘制拉齐奥塔 - 斗兽场"""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    
    draw_cloud(draw, 200, 180, 55)
    draw_cloud(draw, 650, 150, 45)
    
    cx, cy = WIDTH // 2, HEIGHT // 2 + 100
    
    # 斗兽场颜色
    stone_color = (210, 180, 140)
    arch_color = (60, 40, 30)
    
    # 椭圆形主体 - 简化卡通版本
    # 底部
    draw.ellipse([cx-200, cy+100, cx+200, cy+250], fill=stone_color, outline=(0, 0, 0), width=4)
    # 顶部
    draw.ellipse([cx-180, cy-50, cx+180, cy+100], fill=stone_color, outline=(0, 0, 0), width=4)
    
    # 层叠效果
    draw.ellipse([cx-160, cy-100, cx+160, cy+50], fill=stone_color, outline=(0, 0, 0), width=3)
    draw.ellipse([cx-140, cy-150, cx+140, cy], fill=stone_color, outline=(0, 0, 0), width=3)
    
    # 拱门（作为眼睛和嘴巴的装饰）
    arches = [-100, -40, 20, 80, 140]
    for ax in arches:
        draw.arc([cx+ax-25, cy-30, cx+ax+25, cy+30], 0, 180, fill=arch_color, width=15)
    
    # 大拱门作为嘴巴
    draw.arc([cx-50, cy+20, cx+50, cy+100], 0, 180, fill=(80, 50, 40), width=20)
    
    # 可爱的眼睛 - 在斗兽场两侧
    draw_circle_eye(draw, cx-120, cy-80, 30, "left")
    draw_circle_eye(draw, cx+120, cy-80, 30, "right")
    
    # 微笑
    draw_cute_mouth(draw, cx, cy+60, 40, happy=True)
    
    # 腮红
    draw.ellipse([cx-150, cy-60, cx-120, cy-30], fill=(255, 150, 150))
    draw.ellipse([cx+120, cy-60, cx+150, cy-30], fill=(255, 150, 150))
    
    img.save(os.path.join(OUTPUT_DIR, "lazio-colosseum.png"))
    print("✓ lazio-colosseum.png 已生成")

# ==================== 3. 威尼托 - 圣马可广场 ====================
def draw_veneto():
    """绘制威尼托塔 - 圣马可广场钟楼"""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    
    draw_cloud(draw, 180, 120, 50)
    draw_cloud(draw, 620, 180, 55)
    
    cx, cy = WIDTH // 2, HEIGHT // 2 + 50
    
    # 钟楼颜色
    brick_color = (220, 180, 130)
    roof_color = (160, 82, 45)
    
    # 钟楼主体 - 高大矩形
    tower_width, tower_height = 180, 450
    draw_rounded_rect(draw, [cx-tower_width//2, cy-tower_height//2, 
                              cx+tower_width//2, cy+tower_height//2], 
                      15, brick_color, (0, 0, 0), 3)
    
    # 钟楼顶部屋顶
    draw.polygon([(cx-100, cy-225), (cx, cy-350), (cx+100, cy-225)], 
                 fill=roof_color, outline=(0, 0, 0), width=3)
    
    # 顶部小尖塔
    draw.polygon([(cx-10, cy-350), (cx, cy-420), (cx+10, cy-350)], 
                 fill=(255, 215, 0), outline=(0, 0, 0), width=2)
    
    # 金色天使/风向标
    draw.ellipse([cx-15, cy-440, cx+15, cy-400], fill=(255, 215, 0), outline=(0, 0, 0), width=2)
    
    # 钟楼拱形窗户（可爱的眼睛）
    # 左眼拱
    draw.arc([cx-60, cy-100, cx-20, cy-40], 0, 180, fill=(80, 60, 40), width=20)
    draw_circle_eye(draw, cx-40, cy-50, 15, "left")
    
    # 右眼拱
    draw.arc([cx+20, cy-100, cx+60, cy-40], 0, 180, fill=(80, 60, 40), width=20)
    draw_circle_eye(draw, cx+40, cy-50, 15, "right")
    
    # 嘴巴 - 小拱形门
    draw.arc([cx-30, cy+50, cx+30, cy+120], 0, 180, fill=(100, 70, 50), width=25)
    draw_cute_mouth(draw, cx, cy+100, 20, happy=True)
    
    # 腮红
    draw.ellipse([cx-80, cy-20, cx-50, cy+10], fill=(255, 150, 150))
    draw.ellipse([cx+50, cy-20, cx+80, cy+10], fill=(255, 150, 150))
    
    # 钟楼底部装饰条纹
    for i in range(-3, 4):
        x = cx + i * 25
        draw.line([(x, cy+180), (x, cy+225)], fill=(180, 140, 100), width=8)
    
    img.save(os.path.join(OUTPUT_DIR, "veneto-san-marco.png"))
    print("✓ veneto-san-marco.png 已生成")

# ==================== 4. 坎帕尼亚 - 维苏威火山 ====================
def draw_campania():
    """绘制坎帕尼亚塔 - 维苏威火山"""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    
    draw_cloud(draw, 150, 200, 60)
    draw_cloud(draw, 650, 250, 50)
    
    cx, cy = WIDTH // 2, HEIGHT // 2 + 150
    
    # 火山颜色
    mountain_color = (120, 80, 60)
    top_color = (80, 60, 50)
    lava_color = (255, 80, 30)
    
    # 火山主体 - 三角形/山形
    draw.polygon([(cx-200, cy+200), (cx, cy-200), (cx+200, cy+200)], 
                 fill=mountain_color, outline=(0, 0, 0), width=4)
    
    # 火山口
    draw.ellipse([cx-60, cy-220, cx+60, cy-160], fill=top_color, outline=(0, 0, 0), width=3)
    
    # 熔岩
    draw.ellipse([cx-40, cy-210, cx+40, cy-170], fill=lava_color, outline=(255, 100, 50), width=2)
    
    # 熔岩流动效果
    draw.polygon([(cx-20, cy-180), (cx-30, cy-100), (cx-10, cy-180)], fill=lava_color)
    draw.polygon([(cx+10, cy-180), (cx+20, cy-120), (cx+30, cy-180)], fill=lava_color)
    
    # 烟雾
    smoke_color = (150, 150, 150)
    draw.ellipse([cx-40, cy-280, cx+40, cy-220], fill=smoke_color, outline=(100, 100, 100), width=2)
    draw.ellipse([cx-30, cy-320, cx+30, cy-260], fill=(180, 180, 180), outline=(120, 120, 120), width=2)
    draw.ellipse([cx-20, cy-360, cx+20, cy-300], fill=(200, 200, 200), outline=(140, 140, 140), width=2)
    
    # 眼睛 - 在山体上
    draw_circle_eye(draw, cx-80, cy, 30, "left")
    draw_circle_eye(draw, cx+80, cy, 30, "right")
    
    # 嘴巴 - 在山体下方
    draw_cute_mouth(draw, cx, cy+80, 35, happy=True)
    
    # 腮红
    draw.ellipse([cx-120, cy+20, cx-90, cy+50], fill=(255, 150, 150))
    draw.ellipse([cx+90, cy+20, cx+120, cy+50], fill=(255, 150, 150))
    
    # 火山纹理
    for i in range(5):
        y = cy - 100 + i * 50
        draw.line([(cx-100+i*10, y), (cx-50+i*10, y)], fill=(100, 70, 50), width=5)
        draw.line([(cx+50-i*10, y), (cx+100-i*10, y)], fill=(100, 70, 50), width=5)
    
    img.save(os.path.join(OUTPUT_DIR, "campania-vesuvius.png"))
    print("✓ campania-vesuvius.png 已生成")

# ==================== 5. 西西里 - 神殿谷 ====================
def draw_sicily():
    """绘制西西里塔 - 神殿谷古希腊神庙"""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    
    draw_cloud(draw, 200, 150, 55)
    draw_cloud(draw, 600, 200, 50)
    
    cx, cy = WIDTH // 2, HEIGHT // 2 + 100
    
    # 神庙颜色
    stone_color = (200, 190, 170)
    roof_color = (180, 160, 140)
    column_color = (210, 200, 180)
    
    # 神庙基座
    draw_rounded_rect(draw, [cx-200, cy+150, cx+200, cy+200], 10, stone_color, (0, 0, 0), 3)
    
    # 神庙屋顶 - 三角形
    draw.polygon([(cx-180, cy-100), (cx, cy-250), (cx+180, cy-100)], 
                 fill=roof_color, outline=(0, 0, 0), width=3)
    
    # 内部填充
    draw.polygon([(cx-160, cy-100), (cx, cy-230), (cx+160, cy-100)], 
                 fill=(190, 180, 160), outline=(0, 0, 0), width=2)
    
    # 柱子
    num_columns = 6
    column_spacing = 300 // (num_columns - 1)
    for i in range(num_columns):
        x = cx - 150 + i * column_spacing
        draw.rectangle([x-12, cy-100, x+12, cy+150], fill=column_color, outline=(0, 0, 0), width=2)
        # 柱头
        draw.rectangle([x-15, cy-110, x+15, cy-100], fill=stone_color, outline=(0, 0, 0), width=2)
        # 柱底
        draw.rectangle([x-15, cy+140, x+15, cy+150], fill=stone_color, outline=(0, 0, 0), width=2)
    
    # 可爱的脸 - 在神庙三角墙上
    draw_circle_eye(draw, cx-50, cy-170, 20, "left")
    draw_circle_eye(draw, cx+50, cy-170, 20, "right")
    draw_cute_mouth(draw, cx, cy-130, 25, happy=True)
    
    # 腮红
    draw.ellipse([cx-80, cy-160, cx-60, cy-140], fill=(255, 150, 150))
    draw.ellipse([cx+60, cy-160, cx+80, cy-140], fill=(255, 150, 150))
    
    img.save(os.path.join(OUTPUT_DIR, "sicily-valley.png"))
    print("✓ sicily-valley.png 已生成")

# ==================== 6. 托斯卡纳 - 比萨斜塔 ====================
def draw_tuscany():
    """绘制托斯卡纳塔 - 比萨斜塔"""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    
    draw_cloud(draw, 200, 180, 50)
    draw_cloud(draw, 600, 120, 45)
    
    # 倾斜的塔
    cx, cy = WIDTH // 2 - 50, HEIGHT // 2 + 50
    lean = 40  # 倾斜角度
    
    # 塔颜色
    tower_color = (220, 210, 190)
    roof_color = (160, 140, 120)
    
    # 塔身 - 倾斜的圆柱体效果
    # 底部（较宽）
    draw.ellipse([cx-80, cy+180, cx+80, cy+220], fill=tower_color, outline=(0, 0, 0), width=3)
    # 中部
    draw.polygon([(cx-80, cy+200), (cx+80, cy+200), 
                  (cx-60+lean, cy-50), (cx+60+lean, cy-50)], 
                 fill=tower_color, outline=(0, 0, 0), width=3)
    # 顶部
    draw.ellipse([cx-60+lean, cy-70, cx+60+lean, cy-30], fill=tower_color, outline=(0, 0, 0), width=3)
    
    # 塔顶钟楼
    bell_color = (180, 170, 150)
    draw.polygon([(cx-50+lean, cy-50), (cx+50+lean, cy-50), 
                  (cx-40+lean, cy-120), (cx+40+lean, cy-120)], 
                 fill=bell_color, outline=(0, 0, 0), width=3)
    
    # 塔顶
    draw.polygon([(cx-45+lean, cy-120), (cx+45+lean, cy-120), 
                  (cx+lean, cy-160)], fill=roof_color, outline=(0, 0, 0), width=3)
    
    # 装饰拱廊
    for i in range(4):
        y = cy + 120 - i * 50
        x_offset = 15 - i * 10 + lean * (200 - i * 50) / 250
        draw.arc([cx-40+x_offset, y-20, cx+40+x_offset, y+20], 0, 180, 
                 fill=(150, 140, 120), width=8)
    
    # 可爱的脸 - 在钟楼上
    eye_cx = cx + lean
    eye_cy = cy - 85
    draw_circle_eye(draw, eye_cx-20, eye_cy, 15, "left")
    draw_circle_eye(draw, eye_cx+20, eye_cy, 15, "right")
    draw_cute_mouth(draw, eye_cx, eye_cy+25, 18, happy=True)
    
    # 腮红
    draw.ellipse([eye_cx-40, eye_cy-5, eye_cx-25, eye_cy+10], fill=(255, 150, 150))
    draw.ellipse([eye_cx+25, eye_cy-5, eye_cx+40, eye_cy+10], fill=(255, 150, 150))
    
    img.save(os.path.join(OUTPUT_DIR, "tuscany-pisa.png"))
    print("✓ tuscany-pisa.png 已生成")

# ==================== 7. 皮埃蒙特 - 都灵 ====================
def draw_piedmont():
    """绘制皮埃蒙特塔 - 都灵风格建筑"""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    
    draw_cloud(draw, 180, 160, 55)
    draw_cloud(draw, 620, 180, 50)
    
    cx, cy = WIDTH // 2, HEIGHT // 2 + 80
    
    # 都灵建筑风格 - 优雅的巴洛克风格
    building_color = (200, 190, 180)
    dome_color = (160, 150, 140)
    gold_color = (218, 165, 32)
    
    # 主体建筑
    draw_rounded_rect(draw, [cx-180, cy-50, cx+180, cy+200], 20, building_color, (0, 0, 0), 3)
    
    # 中央大圆顶
    draw.ellipse([cx-100, cy-180, cx+100, cy-20], fill=dome_color, outline=(0, 0, 0), width=3)
    # 圆顶上的小塔
    draw.rectangle([cx-15, cy-220, cx+15, cy-180], fill=building_color, outline=(0, 0, 0), width=2)
    draw.polygon([(cx-20, cy-220), (cx+20, cy-220), (cx, cy-260)], fill=dome_color, outline=(0, 0, 0), width=2)
    
    # 两侧小塔
    for offset in [-150, 150]:
        draw.rectangle([cx+offset-25, cy-100, cx+offset+25, cy+200], fill=building_color, outline=(0, 0, 0), width=2)
        draw.polygon([(cx+offset-30, cy-100), (cx+offset+30, cy-100), (cx+offset, cy-150)], 
                     fill=dome_color, outline=(0, 0, 0), width=2)
    
    # 金色装饰
    draw.ellipse([cx-10, cy-260, cx+10, cy-240], fill=gold_color, outline=(0, 0, 0), width=2)
    
    # 拱形门廊作为嘴巴
    draw.arc([cx-50, cy+80, cx+50, cy+160], 0, 180, fill=(100, 80, 60), width=30)
    
    # 可爱的脸
    draw_circle_eye(draw, cx-70, cy-20, 25, "left")
    draw_circle_eye(draw, cx+70, cy-20, 25, "right")
    draw_cute_mouth(draw, cx, cy+40, 25, happy=True)
    
    # 腮红
    draw.ellipse([cx-100, cy, cx-75, cy+20], fill=(255, 150, 150))
    draw.ellipse([cx+75, cy, cx+100, cy+20], fill=(255, 150, 150))
    
    img.save(os.path.join(OUTPUT_DIR, "piedmont-turin.png"))
    print("✓ piedmont-turin.png 已生成")

# ==================== 8. 利古里亚 - 五渔村 ====================
def draw_liguria():
    """绘制利古里亚塔 - 五渔村彩色房屋"""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    
    draw_cloud(draw, 200, 150, 50)
    draw_cloud(draw, 600, 200, 55)
    
    cx, cy = WIDTH // 2, HEIGHT // 2 + 150
    
    # 五渔村颜色 - 多彩的房屋
    colors = [
        (255, 150, 100),  # 橙色
        (255, 220, 100),  # 黄色
        (150, 220, 150),  # 绿色
        (150, 180, 255),  # 蓝色
        (255, 150, 200),  # 粉色
    ]
    
    # 悬崖/山丘
    cliff_color = (120, 140, 100)
    draw.polygon([(cx-250, cy+200), (cx, cy-100), (cx+250, cy+200)], fill=cliff_color, outline=(0, 0, 0), width=3)
    
    # 层层叠叠的彩色房屋
    house_width, house_height = 70, 60
    positions = [
        (cx-180, cy+50), (cx-100, cy+20), (cx-20, cy+40), (cx+60, cy+10), (cx+140, cy+50),
        (cx-140, cy-40), (cx-60, cy-70), (cx+20, cy-50), (cx+100, cy-80),
        (cx-100, cy-120), (cx-20, cy-150), (cx+60, cy-130),
    ]
    
    for i, (hx, hy) in enumerate(positions):
        color = colors[i % len(colors)]
        # 房屋主体
        draw.rounded_rectangle([hx-house_width//2, hy-house_height, hx+house_width//2, hy], 
                               radius=5, fill=color, outline=(0, 0, 0), width=2)
        # 屋顶
        draw.polygon([(hx-house_width//2-5, hy-house_height), (hx+house_width//2+5, hy-house_height), 
                      (hx, hy-house_height-20)], fill=(180, 100, 80), outline=(0, 0, 0), width=2)
        # 小窗户
        draw.rectangle([hx-15, hy-40, hx+15, hy-15], fill=(200, 230, 255), outline=(0, 0, 0), width=1)
    
    # 大海
    sea_color = (100, 150, 200)
    draw.rectangle([cx-300, cy+180, cx+300, cy+250], fill=sea_color, outline=(0, 0, 0), width=2)
    
    # 波浪
    for i in range(-2, 3):
        wx = cx + i * 80
        draw.arc([wx-30, cy+190, wx+30, cy+210], 180, 360, fill=(150, 200, 255), width=5)
    
    # 可爱的脸 - 在中间大房子上
    face_x, face_y = cx-20, cy-120
    draw_circle_eye(draw, face_x-20, face_y-40, 15, "left")
    draw_circle_eye(draw, face_x+20, face_y-40, 15, "right")
    draw_cute_mouth(draw, face_x, face_y-15, 15, happy=True)
    
    # 腮红
    draw.ellipse([face_x-35, face_y-30, face_x-25, face_y-20], fill=(255, 150, 150))
    draw.ellipse([face_x+25, face_y-30, face_x+35, face_y-20], fill=(255, 150, 150))
    
    img.save(os.path.join(OUTPUT_DIR, "liguria-cinque-terre.png"))
    print("✓ liguria-cinque-terre.png 已生成")

# ==================== 9. 艾米利亚 - 法拉利 ====================
def draw_emilia():
    """绘制艾米利亚塔 - 法拉利主题"""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    
    draw_cloud(draw, 200, 150, 50)
    draw_cloud(draw, 600, 200, 55)
    
    cx, cy = WIDTH // 2, HEIGHT // 2 + 100
    
    # 法拉利红色
    ferrari_red = (220, 30, 30)
    black = (30, 30, 30)
    silver = (180, 180, 180)
    yellow = (255, 220, 50)
    
    # 赛道塔基座
    draw_rounded_rect(draw, [cx-200, cy+150, cx+200, cy+200], 10, (100, 100, 100), (0, 0, 0), 3)
    
    # 赛道格子线
    for i in range(-4, 5):
        x = cx + i * 40
        draw.line([(x, cy+150), (x, cy+200)], fill=(240, 240, 240), width=20)
    
    # 主塔身 - 流线型
    draw.polygon([(cx-100, cy+150), (cx+100, cy+150), (cx+80, cy-50), (cx-80, cy-50)], 
                 fill=ferrari_red, outline=(0, 0, 0), width=3)
    
    # 顶部流线
    draw.polygon([(cx-80, cy-50), (cx+80, cy-50), (cx, cy-200)], 
                 fill=ferrari_red, outline=(0, 0, 0), width=3)
    
    # 跃马标志背景
    draw.ellipse([cx-60, cy-100, cx+60, cy+20], fill=yellow, outline=(0, 0, 0), width=3)
    
    # 简化的跃马
    # 马头
    draw.ellipse([cx-30, cy-80, cx+10, cy-40], fill=black, outline=(0, 0, 0), width=2)
    # 马身
    draw.polygon([(cx-20, cy-50), (cx+40, cy-50), (cx+30, cy-10), (cx-10, cy-10)], 
                 fill=black, outline=(0, 0, 0), width=2)
    # 马腿
    draw.rectangle([cx-10, cy-10, cx, cy+15], fill=black, outline=(0, 0, 0), width=1)
    draw.rectangle([cx+10, cy-10, cx+20, cy+15], fill=black, outline=(0, 0, 0), width=1)
    
    # 法拉利标志性的进气口条纹
    draw.rectangle([cx-60, cy+50, cx-40, cy+150], fill=black, outline=(0, 0, 0), width=2)
    draw.rectangle([cx-30, cy+50, cx-10, cy+150], fill=black, outline=(0, 0, 0), width=2)
    draw.rectangle([cx+10, cy+50, cx+30, cy+150], fill=black, outline=(0, 0, 0), width=2)
    draw.rectangle([cx+40, cy+50, cx+60, cy+150], fill=black, outline=(0, 0, 0), width=2)
    
    # 银色边框
    draw.line([(cx-100, cy+150), (cx-80, cy-50)], fill=silver, width=5)
    draw.line([(cx+100, cy+150), (cx+80, cy-50)], fill=silver, width=5)
    
    # 可爱的脸 - 在塔上方
    draw_circle_eye(draw, cx-40, cy-140, 20, "left")
    draw_circle_eye(draw, cx+40, cy-140, 20, "right")
    draw_cute_mouth(draw, cx, cy-100, 20, happy=True)
    
    # 腮红
    draw.ellipse([cx-60, cy-130, cx-45, cy-115], fill=(255, 150, 150))
    draw.ellipse([cx+45, cy-130, cx+60, cy-115], fill=(255, 150, 150))
    
    img.save(os.path.join(OUTPUT_DIR, "emilia-ferrari.png"))
    print("✓ emilia-ferrari.png 已生成")

# ==================== 10. 普利亚 - 特鲁利 ====================
def draw_apulia():
    """绘制普利亚塔 - 特鲁利石屋"""
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    
    draw_cloud(draw, 200, 180, 50)
    draw_cloud(draw, 600, 150, 55)
    
    cx, cy = WIDTH // 2, HEIGHT // 2 + 100
    
    # 特鲁利石屋颜色
    stone_color = (220, 210, 190)
    roof_color = (180, 170, 160)
    symbol_color = (100, 150, 100)
    
    # 地面
    ground_color = (150, 180, 120)
    draw.ellipse([cx-250, cy+180, cx+250, cy+300], fill=ground_color, outline=(0, 0, 0), width=3)
    
    # 主要特鲁利房屋 - 圆锥形屋顶
    # 主房屋
    draw.ellipse([cx-100, cy+100, cx+100, cy+180], fill=stone_color, outline=(0, 0, 0), width=3)
    # 圆锥屋顶
    draw.polygon([(cx-80, cy+140), (cx+80, cy+140), (cx, cy-100)], 
                 fill=roof_color, outline=(0, 0, 0), width=3)
    
    # 屋顶上神秘的符号（普利亚特鲁利的传统）
    # 十字符号
    draw.line([(cx, cy-80), (cx, cy-50)], fill=symbol_color, width=8)
    draw.line([(cx-15, cy-65), (cx+15, cy-65)], fill=symbol_color, width=8)
    
    # 较小的特鲁利
    small_positions = [(cx-180, cy+120), (cx+180, cy+120)]
    for sx, sy in small_positions:
        draw.ellipse([sx-50, sy+40, sx+50, sy+100], fill=stone_color, outline=(0, 0, 0), width=2)
        draw.polygon([(sx-40, sy+70), (sx+40, sy+70), (sx, sy-40)], 
                     fill=roof_color, outline=(0, 0, 0), width=2)
        # 小窗户
        draw.ellipse([sx-10, sy+50, sx+10, sy+80], fill=(80, 60, 40), outline=(0, 0, 0), width=2)
    
    # 主房屋门
    draw.ellipse([cx-30, cy+120, cx+30, cy+180], fill=(80, 60, 40), outline=(0, 0, 0), width=3)
    
    # 可爱的脸 - 在屋顶上
    draw_circle_eye(draw, cx-40, cy, 25, "left")
    draw_circle_eye(draw, cx+40, cy, 25, "right")
    draw_cute_mouth(draw, cx, cy+40, 25, happy=True)
    
    # 腮红
    draw.ellipse([cx-70, cy+10, cx-50, cy+30], fill=(255, 150, 150))
    draw.ellipse([cx+50, cy+10, cx+70, cy+30], fill=(255, 150, 150))
    
    # 橄榄树装饰
    for i in range(3):
        tx = cx - 150 + i * 150
        ty = cy + 220
        # 树干
        draw.rectangle([tx-5, ty-30, tx+5, ty], fill=(139, 90, 43), outline=(0, 0, 0), width=1)
        # 树冠
        draw.ellipse([tx-25, ty-60, tx+25, ty-20], fill=(150, 180, 100), outline=(0, 0, 0), width=2)
    
    img.save(os.path.join(OUTPUT_DIR, "apulia-trulli.png"))
    print("✓ apulia-trulli.png 已生成")

# 主函数
def main():
    print("🏰 开始生成意大利大区卡通塔图片...")
    print(f"📁 输出目录: {OUTPUT_DIR}")
    print()
    
    draw_lombardy()       # 1. 伦巴第 - 米兰大教堂
    draw_lazio()          # 2. 拉齐奥 - 斗兽场
    draw_veneto()         # 3. 威尼托 - 圣马可广场
    draw_campania()       # 4. 坎帕尼亚 - 维苏威火山
    draw_sicily()         # 5. 西西里 - 神殿谷
    draw_tuscany()        # 6. 托斯卡纳 - 比萨斜塔
    draw_piedmont()       # 7. 皮埃蒙特 - 都灵
    draw_liguria()        # 8. 利古里亚 - 五渔村
    draw_emilia()         # 9. 艾米利亚 - 法拉利
    draw_apulia()         # 10. 普利亚 - 特鲁利
    
    print()
    print("✅ 所有10个意大利大区卡通塔图片生成完成！")

if __name__ == "__main__":
    main()
