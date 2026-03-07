#!/usr/bin/env python3
"""
生成7个国家主题的卡通游戏头像图标
愤怒的小鸟风格，512x512像素，圆形，渐变背景
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math
import os

OUTPUT_DIR = "/Users/moutai/Desktop/toweroffate_v1.0/assets/avatars"
SIZE = 512
CIRCLE_RADIUS = 240

def create_gradient_background(draw, size, colors):
    """创建渐变背景"""
    for y in range(size):
        ratio = y / size
        r = int(colors[0][0] * (1 - ratio) + colors[1][0] * ratio)
        g = int(colors[0][1] * (1 - ratio) + colors[1][1] * ratio)
        b = int(colors[0][2] * (1 - ratio) + colors[1][2] * ratio)
        draw.line([(0, y), (size, y)], fill=(r, g, b))

def draw_circle_mask(img, center, radius):
    """创建圆形遮罩"""
    mask = Image.new('L', img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse([center[0] - radius, center[1] - radius, 
                  center[0] + radius, center[1] + radius], fill=255)
    return mask

def create_circular_image(img):
    """将图片裁剪为圆形并添加透明背景"""
    # 创建透明背景
    circular = Image.new('RGBA', img.size, (0, 0, 0, 0))
    
    # 创建圆形遮罩
    mask = Image.new('L', img.size, 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.ellipse([16, 16, SIZE-16, SIZE-16], fill=255)
    
    # 应用遮罩
    circular.paste(img, (0, 0), mask)
    return circular

def draw_cartoon_eyes(draw, cx, cy, size=40):
    """绘制卡通大眼睛"""
    # 左眼白
    draw.ellipse([cx - size - 25, cy - size//2, cx - 25, cy + size//2], fill=(255, 255, 255), outline=(0,0,0), width=3)
    # 左眼珠
    draw.ellipse([cx - size//2 - 25, cy - size//4, cx - 25, cy + size//4], fill=(0, 0, 0))
    # 左眼高光
    draw.ellipse([cx - size//3 - 25, cy - size//6, cx - size//6 - 25, cy], fill=(255, 255, 255))
    
    # 右眼白
    draw.ellipse([cx + 25, cy - size//2, cx + size + 25, cy + size//2], fill=(255, 255, 255), outline=(0,0,0), width=3)
    # 右眼珠
    draw.ellipse([cx + 25, cy - size//4, cx + size//2 + 25, cy + size//4], fill=(0, 0, 0))
    # 右眼高光
    draw.ellipse([cx + size//6 + 25, cy - size//6, cx + size//3 + 25, cy], fill=(255, 255, 255))

def draw_angry_eyebrows(draw, cx, cy, size=50):
    """绘制愤怒的小鸟风格的眉毛"""
    # 左眉
    draw.polygon([(cx - 70, cy - 20), (cx - 10, cy + 10), (cx - 5, cy - 5), (cx - 65, cy - 35)], fill=(60, 30, 10))
    # 右眉
    draw.polygon([(cx + 10, cy + 10), (cx + 70, cy - 20), (cx + 65, cy - 35), (cx + 5, cy - 5)], fill=(60, 30, 10))

def draw_cartoon_beak(draw, cx, cy):
    """绘制卡通鸟嘴"""
    # 上嘴
    draw.polygon([(cx, cy - 10), (cx + 40, cy + 20), (cx, cy + 25)], fill=(255, 200, 50), outline=(200, 150, 0), width=3)
    # 下嘴
    draw.polygon([(cx, cy + 25), (cx + 35, cy + 35), (cx, cy + 40)], fill=(255, 180, 30), outline=(200, 150, 0), width=3)

def thailand_elephant():
    """泰国 - 大象+大皇宫风格"""
    img = Image.new('RGB', (SIZE, SIZE), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # 渐变背景 - 泰式金红
    create_gradient_background(draw, SIZE, [(255, 215, 0), (220, 50, 50)])
    
    cx, cy = SIZE // 2, SIZE // 2
    
    # 大象头部（愤怒的小鸟风格）
    # 身体
    draw.ellipse([cx - 140, cy - 120, cx + 140, cy + 120], fill=(150, 150, 160), outline=(100, 100, 110), width=4)
    
    # 大耳朵
    draw.ellipse([cx - 180, cy - 80, cx - 80, cy + 40], fill=(140, 140, 150), outline=(100, 100, 110), width=3)
    draw.ellipse([cx + 80, cy - 80, cx + 180, cy + 40], fill=(140, 140, 150), outline=(100, 100, 110), width=3)
    
    # 象鼻
    trunk_points = [
        (cx - 20, cy + 80), (cx - 30, cy + 150), (cx - 10, cy + 180),
        (cx + 10, cy + 180), (cx + 30, cy + 150), (cx + 20, cy + 80)
    ]
    draw.polygon(trunk_points, fill=(150, 150, 160), outline=(100, 100, 110), width=3)
    
    # 眼睛
    draw_cartoon_eyes(draw, cx, cy - 20, 35)
    draw_angry_eyebrows(draw, cx, cy - 40)
    
    # 象牙
    draw.polygon([(cx - 50, cy + 70), (cx - 70, cy + 110), (cx - 40, cy + 85)], fill=(255, 255, 240), outline=(220, 220, 200), width=2)
    draw.polygon([(cx + 50, cy + 70), (cx + 70, cy + 110), (cx + 40, cy + 85)], fill=(255, 255, 240), outline=(220, 220, 200), width=2)
    
    # 金色头饰（大皇宫风格）
    crown_points = [(cx, cy - 140), (cx - 30, cy - 110), (cx - 15, cy - 115), 
                    (cx, cy - 105), (cx + 15, cy - 115), (cx + 30, cy - 110)]
    draw.polygon(crown_points, fill=(255, 215, 0), outline=(200, 170, 0), width=3)
    draw.ellipse([cx - 10, cy - 130, cx + 10, cy - 110], fill=(255, 50, 50))
    
    return create_circular_image(img)

def vietnam_hat():
    """越南 - 斗笠+下龙湾风格"""
    img = Image.new('RGB', (SIZE, SIZE), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # 渐变背景 - 越南绿
    create_gradient_background(draw, SIZE, [(50, 150, 100), (30, 100, 180)])
    
    cx, cy = SIZE // 2, SIZE // 2
    
    # 头部
    draw.ellipse([cx - 130, cy - 100, cx + 130, cy + 100], fill=(255, 220, 177), outline=(230, 190, 140), width=4)
    
    # 斗笠
    hat_points = [(cx, cy - 160), (cx - 160, cy - 80), (cx + 160, cy - 80)]
    draw.polygon(hat_points, fill=(139, 90, 43), outline=(100, 60, 20), width=4)
    draw.ellipse([cx - 160, cy - 90, cx + 160, cy - 70], fill=(160, 110, 60), outline=(100, 60, 20), width=3)
    # 笠顶
    draw.ellipse([cx - 15, cy - 170, cx + 15, cy - 140], fill=(139, 90, 43), outline=(100, 60, 20), width=2)
    
    # 眼睛
    draw_cartoon_eyes(draw, cx, cy - 10, 38)
    draw_angry_eyebrows(draw, cx, cy - 30)
    
    # 嘴巴
    draw.arc([cx - 30, cy + 30, cx + 30, cy + 70], 0, 180, fill=(200, 100, 80), width=4)
    
    # 越南国旗星星在帽子上
    star_points = []
    for i in range(5):
        angle = math.pi/2 + i * 2 * math.pi / 5
        outer_x = cx + 25 * math.cos(angle)
        outer_y = cy - 115 + 25 * math.sin(angle)
        star_points.append((outer_x, outer_y))
        angle += math.pi / 5
        inner_x = cx + 10 * math.cos(angle)
        inner_y = cy - 115 + 10 * math.sin(angle)
        star_points.append((inner_x, inner_y))
    draw.polygon(star_points, fill=(255, 50, 50))
    
    return create_circular_image(img)

def greece_olive():
    """希腊 - 橄榄枝+帕特农风格"""
    img = Image.new('RGB', (SIZE, SIZE), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # 渐变背景 - 希腊蓝白
    create_gradient_background(draw, SIZE, [(0, 100, 200), (255, 255, 255)])
    
    cx, cy = SIZE // 2, SIZE // 2
    
    # 头部 - 古希腊陶罐风格
    draw.ellipse([cx - 130, cy - 100, cx + 130, cy + 100], fill=(220, 180, 140), outline=(180, 140, 100), width=4)
    
    # 头发（卷发风格）
    for i in range(-3, 4):
        x = cx + i * 35
        y = cy - 90
        draw.ellipse([x - 25, y - 25, x + 25, y + 15], fill=(100, 80, 60), outline=(70, 50, 40), width=2)
    
    # 月桂冠
    for i in range(-4, 5):
        angle = i * 0.3
        lx = cx + int(130 * math.sin(angle))
        ly = cy - 80 + int(20 * abs(math.sin(angle * 2)))
        # 橄榄叶
        draw.ellipse([lx - 20, ly - 15, lx + 20, ly + 15], fill=(80, 150, 60), outline=(50, 120, 40), width=2)
    
    # 眼睛
    draw_cartoon_eyes(draw, cx, cy - 10, 36)
    draw_angry_eyebrows(draw, cx, cx - 30)
    
    # 鼻子
    draw.polygon([(cx, cy + 10), (cx - 10, cy + 40), (cx + 10, cy + 40)], fill=(210, 170, 130), outline=(180, 140, 100), width=2)
    
    # 嘴巴
    draw.arc([cx - 25, cy + 45, cx + 25, cy + 75], 0, 180, fill=(180, 100, 80), width=4)
    
    return create_circular_image(img)

def sweden_viking():
    """瑞典 - 维京船+极光风格"""
    img = Image.new('RGB', (SIZE, SIZE), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # 渐变背景 - 极光绿紫
    create_gradient_background(draw, SIZE, [(50, 255, 150), (100, 50, 180)])
    
    cx, cy = SIZE // 2, SIZE // 2
    
    # 维京头盔
    draw.ellipse([cx - 140, cy - 130, cx + 140, cy + 50], fill=(180, 180, 190), outline=(120, 120, 130), width=4)
    
    # 护鼻
    draw.polygon([(cx - 15, cy - 80), (cx + 15, cy - 80), (cx + 10, cy + 20), (cx - 10, cy + 20)], 
                 fill=(160, 160, 170), outline=(120, 120, 130), width=3)
    
    # 牛角
    draw.polygon([(cx - 100, cy - 100), (cx - 160, cy - 180), (cx - 130, cy - 90)], 
                 fill=(255, 240, 200), outline=(200, 180, 150), width=3)
    draw.polygon([(cx + 100, cy - 100), (cx + 160, cy - 180), (cx + 130, cy - 90)], 
                 fill=(255, 240, 200), outline=(200, 180, 150), width=3)
    
    # 眼睛
    draw_cartoon_eyes(draw, cx, cy - 30, 35)
    draw_angry_eyebrows(draw, cx, cy - 50)
    
    # 胡须
    for i in range(-4, 5):
        x = cx + i * 20
        y = cy + 40 + abs(i) * 5
        draw.ellipse([x - 12, y - 10, x + 12, y + 30], fill=(220, 200, 150), outline=(180, 160, 120), width=2)
    
    # 脸部
    draw.ellipse([cx - 100, cy + 10, cx + 100, cy + 80], fill=(255, 220, 177), outline=(230, 190, 140), width=3)
    
    # 嘴巴
    draw.arc([cx - 30, cy + 40, cx + 30, cy + 70], 0, 180, fill=(180, 100, 80), width=4)
    
    return create_circular_image(img)

def mexico_skull():
    """墨西哥 - 骷髅+草帽风格"""
    img = Image.new('RGB', (SIZE, SIZE), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # 渐变背景 - 墨西哥热烈色彩
    create_gradient_background(draw, SIZE, [(255, 100, 50), (255, 200, 50)])
    
    cx, cy = SIZE // 2, SIZE // 2
    
    # 墨西哥草帽
    hat_points = [(cx, cy - 160), (cx - 180, cy - 60), (cx + 180, cy - 60)]
    draw.polygon(hat_points, fill=(200, 150, 80), outline=(150, 100, 50), width=4)
    draw.ellipse([cx - 180, cy - 70, cx + 180, cy - 50], fill=(220, 170, 100), outline=(150, 100, 50), width=3)
    # 帽顶
    draw.ellipse([cx - 70, cy - 140, cx + 70, cy - 60], fill=(210, 160, 90), outline=(150, 100, 50), width=3)
    # 帽带装饰
    draw.ellipse([cx - 75, cy - 90, cx + 75, cy - 70], fill=(255, 50, 50), outline=(200, 30, 30), width=2)
    
    # 骷髅头
    draw.ellipse([cx - 100, cy - 30, cx + 100, cy + 130], fill=(255, 255, 240), outline=(220, 220, 200), width=4)
    
    # 眼睛（骷髅眼窝）
    draw.ellipse([cx - 50, cy + 10, cx - 10, cy + 50], fill=(30, 30, 30), outline=(0, 0, 0), width=3)
    draw.ellipse([cx + 10, cy + 10, cx + 50, cy + 50], fill=(30, 30, 30), outline=(0, 0, 0), width=3)
    # 眼睛里的光点
    draw.ellipse([cx - 40, cy + 20, cx - 25, cy + 35], fill=(255, 100, 100))
    draw.ellipse([cx + 20, cy + 20, cx + 35, cy + 35], fill=(255, 100, 100))
    
    # 眉毛（愤怒）
    draw_angry_eyebrows(draw, cx, cy - 10)
    
    # 鼻子
    draw.polygon([(cx, cy + 50), (cx - 15, cy + 80), (cx + 15, cy + 80)], fill=(30, 30, 30), outline=(0, 0, 0), width=2)
    
    # 嘴巴（牙齿）
    for i in range(-2, 3):
        x = cx + i * 20
        draw.rectangle([x - 8, cy + 95, x + 8, cy + 115], fill=(255, 255, 255), outline=(150, 150, 150), width=2)
    
    # 彩色装饰花纹
    colors = [(255, 50, 100), (50, 200, 255), (100, 255, 100), (255, 200, 50)]
    for i, color in enumerate(colors):
        angle = i * math.pi / 2
        fx = cx + int(120 * math.cos(angle))
        fy = cy + 50 + int(60 * math.sin(angle))
        draw.ellipse([fx - 15, fy - 15, fx + 15, fy + 15], fill=color, outline=(255, 255, 255), width=2)
    
    return create_circular_image(img)

def portugal_ship():
    """葡萄牙 - 帆船+贝伦塔风格"""
    img = Image.new('RGB', (SIZE, SIZE), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # 渐变背景 - 葡萄牙海洋蓝
    create_gradient_background(draw, SIZE, [(50, 150, 220), (50, 80, 150)])
    
    cx, cy = SIZE // 2, SIZE // 2
    
    # 头部
    draw.ellipse([cx - 120, cy - 100, cx + 120, cy + 80], fill=(255, 220, 177), outline=(230, 190, 140), width=4)
    
    # 航海帽（贝雷帽风格）
    draw.ellipse([cx - 130, cy - 130, cx + 130, cy - 50], fill=(30, 80, 150), outline=(20, 60, 120), width=4)
    # 帽檐
    draw.arc([cx - 140, cy - 110, cx + 140, cy - 30], 0, 180, fill=(20, 60, 120), width=15)
    # 帽子徽章
    draw.ellipse([cx - 25, cy - 110, cx + 25, cy - 70], fill=(255, 50, 50), outline=(200, 30, 30), width=3)
    # 徽章上的十字
    draw.rectangle([cx - 5, cy - 105, cx + 5, cy - 75], fill=(255, 255, 255))
    draw.rectangle([cx - 20, cy - 95, cx + 20, cy - 85], fill=(255, 255, 255))
    
    # 眼睛
    draw_cartoon_eyes(draw, cx, cy - 30, 35)
    draw_angry_eyebrows(draw, cx, cy - 50)
    
    # 胡子（葡萄牙风格）- 修正语法错误
    draw.ellipse([cx - 80, cy + 20, cx + 80, cy + 90], fill=(100, 60, 40), outline=(80, 50, 30), width=3)
    
    # 修正：重新画胡子
    img2 = Image.new('RGB', (SIZE, SIZE), (255, 255, 255))
    draw2 = ImageDraw.Draw(img2)
    create_gradient_background(draw2, SIZE, [(50, 150, 220), (50, 80, 150)])
    
    # 重新绘制
    draw2.ellipse([cx - 120, cy - 100, cx + 120, cy + 80], fill=(255, 220, 177), outline=(230, 190, 140), width=4)
    draw2.ellipse([cx - 130, cy - 130, cx + 130, cy - 50], fill=(30, 80, 150), outline=(20, 60, 120), width=4)
    draw2.arc([cx - 140, cy - 110, cx + 140, cy - 30], 0, 180, fill=(20, 60, 120), width=15)
    draw2.ellipse([cx - 25, cy - 110, cx + 25, cy - 70], fill=(255, 50, 50), outline=(200, 30, 30), width=3)
    draw2.rectangle([cx - 5, cy - 105, cx + 5, cy - 75], fill=(255, 255, 255))
    draw2.rectangle([cx - 20, cy - 95, cx + 20, cy - 85], fill=(255, 255, 255))
    
    draw_cartoon_eyes(draw2, cx, cy - 30, 35)
    draw_angry_eyebrows(draw2, cx, cy - 50)
    
    # 胡子
    draw2.ellipse([cx - 70, cy + 30, cx + 70, cy + 80], fill=(100, 60, 40), outline=(80, 50, 30), width=3)
    # 胡子线条
    for i in range(-3, 4):
        x = cx + i * 20
        draw2.line([(x, cy + 40), (x, cy + 75)], fill=(80, 50, 30), width=3)
    
    # 嘴巴
    draw2.arc([cx - 30, cy + 50, cx + 30, cy + 80], 0, 180, fill=(180, 100, 80), width=4)
    
    return create_circular_image(img2)

def belgium_chocolate():
    """比利时 - 巧克力+原子塔风格"""
    img = Image.new('RGB', (SIZE, SIZE), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # 渐变背景 - 比利时黑红黄
    for y in range(SIZE):
        ratio = y / SIZE
        if ratio < 0.33:
            color = (30, 30, 30)  # 黑
        elif ratio < 0.66:
            color = (255, 220, 50)  # 黄
        else:
            color = (255, 50, 50)  # 红
        draw.line([(0, y), (SIZE, y)], fill=color)
    
    cx, cy = SIZE // 2, SIZE // 2
    
    # 巧克力色圆形头部
    draw.ellipse([cx - 130, cy - 110, cx + 130, cy + 110], fill=(120, 80, 60), outline=(80, 50, 40), width=4)
    
    # 眼睛（白色带棕色）
    draw.ellipse([cx - 55, cy - 30, cx - 15, cy + 10], fill=(255, 255, 255), outline=(80, 50, 40), width=3)
    draw.ellipse([cx + 15, cy - 30, cx + 55, cy + 10], fill=(255, 255, 255), outline=(80, 50, 40), width=3)
    # 眼珠
    draw.ellipse([cx - 45, cy - 20, cx - 25, cy], fill=(60, 40, 30))
    draw.ellipse([cx + 25, cy - 20, cx + 45, cy], fill=(60, 40, 30))
    # 高光
    draw.ellipse([cx - 40, cy - 18, cx - 30, cy - 8], fill=(255, 255, 255))
    draw.ellipse([cx + 30, cy - 18, cx + 40, cy - 8], fill=(255, 255, 255))
    
    # 眉毛
    draw_angry_eyebrows(draw, cx, cy - 40)
    
    # 嘴巴（吃到巧克力的满足感）
    draw.arc([cx - 40, cy + 30, cx + 40, cy + 70], 0, 180, fill=(80, 50, 40), width=5)
    # 巧克力渍
    draw.ellipse([cx - 15, cy + 50, cx + 15, cy + 80], fill=(100, 60, 50), outline=(80, 50, 40), width=2)
    
    # 原子塔造型装饰（顶部）
    # 中心球
    draw.ellipse([cx - 30, cy - 150, cx + 30, cy - 100], fill=(180, 180, 190), outline=(120, 120, 130), width=3)
    # 支撑结构
    draw.line([(cx, cy - 100), (cx - 50, cy - 50)], fill=(180, 180, 190), width=8)
    draw.line([(cx, cy - 100), (cx + 50, cy - 50)], fill=(180, 180, 190), width=8)
    draw.line([(cx, cy - 100), (cx, cy - 50)], fill=(180, 180, 190), width=8)
    # 小球
    draw.ellipse([cx - 60, cy - 60, cx - 40, cy - 40], fill=(160, 160, 170), outline=(120, 120, 130), width=2)
    draw.ellipse([cx + 40, cy - 60, cx + 60, cy - 40], fill=(160, 160, 170), outline=(120, 120, 130), width=2)
    draw.ellipse([cx - 10, cy - 60, cx + 10, cy - 40], fill=(160, 160, 170), outline=(120, 120, 130), width=2)
    
    return create_circular_image(img)

def main():
    """生成所有头像"""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    avatars = [
        ("thailand-elephant.png", thailand_elephant),
        ("vietnam-hat.png", vietnam_hat),
        ("greece-olive.png", greece_olive),
        ("sweden-viking.png", sweden_viking),
        ("mexico-skull.png", mexico_skull),
        ("portugal-ship.png", portugal_ship),
        ("belgium-chocolate.png", belgium_chocolate),
    ]
    
    for filename, func in avatars:
        filepath = os.path.join(OUTPUT_DIR, filename)
        print(f"Generating {filename}...")
        img = func()
        img.save(filepath, "PNG")
        print(f"  Saved to {filepath}")
    
    print("\nAll avatars generated successfully!")

if __name__ == "__main__":
    main()
