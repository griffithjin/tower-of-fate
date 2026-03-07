from PIL import Image, ImageDraw, ImageFont
import os

def create_gradient_background(width, height, color1, color2):
    """创建渐变背景"""
    image = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(image)
    
    r1, g1, b1 = tuple(int(color1[i:i+2], 16) for i in (1, 3, 5))
    r2, g2, b2 = tuple(int(color2[i:i+2], 16) for i in (1, 3, 5))
    
    for y in range(height):
        ratio = y / height
        r = int(r1 + (r2 - r1) * ratio)
        g = int(g1 + (g2 - g1) * ratio)
        b = int(b1 + (b2 - b1) * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    return image

def draw_eyes(draw, cx, cy, size=15, look_direction=(0, 0)):
    """绘制愤怒的小鸟风格的可爱眼睛"""
    # 眼白
    eye_spacing = size * 1.5
    left_eye_x = cx - eye_spacing
    right_eye_x = cx + eye_spacing
    
    # 大眼睛白
    draw.ellipse([left_eye_x - size, cy - size, left_eye_x + size, cy + size], fill='white', outline='black', width=2)
    draw.ellipse([right_eye_x - size, cy - size, right_eye_x + size, cy + size], fill='white', outline='black', width=2)
    
    # 瞳孔
    pupil_offset_x = look_direction[0] * size * 0.3
    pupil_offset_y = look_direction[1] * size * 0.3
    pupil_size = size * 0.5
    
    draw.ellipse([left_eye_x - pupil_size + pupil_offset_x, cy - pupil_size + pupil_offset_y, 
                  left_eye_x + pupil_size + pupil_offset_x, cy + pupil_size + pupil_offset_y], fill='black')
    draw.ellipse([right_eye_x - pupil_size + pupil_offset_x, cy - pupil_size + pupil_offset_y, 
                  right_eye_x + pupil_size + pupil_offset_x, cy + pupil_size + pupil_offset_y], fill='black')
    
    # 高光
    highlight_size = size * 0.2
    draw.ellipse([left_eye_x - pupil_size + pupil_offset_x - 3, cy - pupil_size + pupil_offset_y - 3,
                  left_eye_x - pupil_size + pupil_offset_x + highlight_size, cy - pupil_size + pupil_offset_y + highlight_size], fill='white')
    draw.ellipse([right_eye_x - pupil_size + pupil_offset_x - 3, cy - pupil_size + pupil_offset_y - 3,
                  right_eye_x - pupil_size + pupil_offset_x + highlight_size, cy - pupil_size + pupil_offset_y + highlight_size], fill='white')

def draw_cute_mouth(draw, cx, cy, size=10, happy=True):
    """绘制可爱的嘴巴"""
    if happy:
        # 微笑
        draw.arc([cx - size, cy - size, cx + size, cy + size], start=0, end=180, fill='black', width=3)
    else:
        # 小圆嘴
        draw.ellipse([cx - size*0.6, cy - size*0.6, cx + size*0.6, cy + size*0.6], fill='#FF6B6B')

def draw_blush(draw, cx, cy, size=12):
    """绘制腮红"""
    # 简单的粉色椭圆腮红
    color = (255, 150, 150)
    draw.ellipse([cx - size, cy - size//2, cx + size, cy + size//2], fill=color)

def draw_cloud(draw, cx, cy, size=50):
    """绘制卡通云朵"""
    color = 'white'
    draw.ellipse([cx - size, cy - size//2, cx + size, cy + size//2], fill=color)
    draw.ellipse([cx - size*1.5, cy - size//3, cx - size*0.3, cy + size//3], fill=color)
    draw.ellipse([cx + size*0.3, cy - size//3, cx + size*1.5, cy + size//3], fill=color)

def draw_tropical_leaf(draw, x, y, size=30, angle=0, color='#228B22'):
    """绘制热带叶子"""
    # 简化的叶子形状
    points = [
        (x, y - size),
        (x + size//2, y - size//3),
        (x + size//3, y),
        (x + size//2, y + size//3),
        (x, y + size),
        (x - size//2, y + size//3),
        (x - size//3, y),
        (x - size//2, y - size//3),
    ]
    draw.polygon(points, fill=color, outline='#1A6B1A')

def add_text(draw, text, y, width, font_size=48):
    """添加底部文字"""
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", font_size)
    except:
        try:
            font = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", font_size)
        except:
            font = ImageFont.load_default()
    
    # 获取文字尺寸
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (width - text_width) // 2
    
    # 添加文字阴影效果
    draw.text((x+2, y+2), text, font=font, fill='#333333')
    draw.text((x, y), text, font=font, fill='white')

def draw_machu_picchu(draw, width, height):
    """绘制马丘比丘 - 印加古城"""
    # 远山
    mountain_color = '#5D4E37'
    draw.polygon([(0, 600), (200, 300), (400, 450), (600, 250), (800, 500), (800, 800), (0, 800)], fill=mountain_color)
    
    # 主山体
    draw.polygon([(100, 800), (300, 400), (500, 450), (700, 800)], fill='#7A6B5A')
    
    # 石墙层（印加风格）
    wall_color = '#C4B5A0'
    for i, y in enumerate(range(480, 780, 40)):
        layer_width = 200 + i * 30
        x_start = 400 - layer_width // 2
        draw.rectangle([x_start, y, x_start + layer_width, y + 35], fill=wall_color, outline='#A09080', width=2)
        # 石块纹理
        for x in range(int(x_start) + 10, int(x_start + layer_width), 30):
            draw.line([(x, y), (x, y + 35)], fill='#A09080', width=1)
    
    # 主建筑 - 印加神庙风格
    temple_color = '#D4C5B0'
    # 底座
    draw.rectangle([320, 380, 480, 480], fill=temple_color, outline='#A09080', width=3)
    # 墙体纹理
    for y in range(390, 480, 20):
        for x in range(330, 470, 25):
            draw.rectangle([x, y, x + 20, y + 15], fill='#C4B5A0', outline='#A09080')
    
    # 梯形窗户（印加特色）
    window_color = '#4A4035'
    for wx in [360, 400, 440]:
        draw.polygon([(wx, 420), (wx + 20, 420), (wx + 18, 450), (wx + 2, 450)], fill=window_color)
    
    # 屋顶
    draw.polygon([(310, 380), (400, 320), (490, 380)], fill='#8B7355')
    
    # 眼睛和表情
    draw_eyes(draw, 400, 360, size=18, look_direction=(0, -0.3))
    draw_cute_mouth(draw, 400, 390, size=12, happy=True)
    draw_blush(draw, 350, 370)
    draw_blush(draw, 450, 370)

def draw_obelisk(draw, width, height):
    """绘制阿根廷方尖碑"""
    # 底座
    base_color = '#E8DCC8'
    draw.rectangle([280, 700, 520, 780], fill=base_color, outline='#C8B8A0', width=3)
    # 底座装饰线
    for y in [720, 740, 760]:
        draw.line([(290, y), (510, y)], fill='#C8B8A0', width=2)
    
    # 方尖碑主体
    obelisk_color = '#F5F0E8'
    # 使用梯形创造立体感
    draw.polygon([(320, 700), (480, 700), (430, 200), (370, 200)], fill=obelisk_color, outline='#D8CCC0', width=2)
    
    # 阴影面
    draw.polygon([(400, 700), (480, 700), (430, 200), (400, 200)], fill='#E8E0D8')
    
    # 顶部装饰
    draw.polygon([(370, 200), (430, 200), (415, 170), (385, 170)], fill='#D4C8B8')
    draw.polygon([(385, 170), (415, 170), (400, 150), (400, 150)], fill='#C8B8A0')
    
    # 刻字线条装饰
    for y in [250, 300, 350, 400, 450, 500, 550, 600, 650]:
        draw.line([(340 + (700-y)*0.08, y), (460 - (700-y)*0.08, y)], fill='#D0C8C0', width=1)
    
    # 阿根廷国旗元素装饰
    # 顶部的小旗
    flag_y = 145
    draw.line([(400, 150), (400, flag_y)], fill='#8B4513', width=3)
    draw.rectangle([400, flag_y, 450, flag_y + 20], fill='#87CEEB')
    draw.rectangle([400, flag_y + 7, 450, flag_y + 13], fill='white')
    # 太阳
    draw.ellipse([420, flag_y + 8, 430, flag_y + 12], fill='#FFD700')
    
    # 眼睛和表情（在方尖碑上部）
    draw_eyes(draw, 400, 280, size=20, look_direction=(0, 0))
    draw_cute_mouth(draw, 400, 315, size=10, happy=True)
    draw_blush(draw, 350, 290)
    draw_blush(draw, 450, 290)

def draw_easter_island(draw, width, height):
    """绘制复活节岛摩艾石像"""
    # 石像颜色
    stone_color = '#8B8680'
    stone_light = '#A8A298'
    stone_dark = '#6B6660'
    
    # 身体/底座
    draw.polygon([(250, 750), (550, 750), (520, 500), (280, 500)], fill=stone_color, outline='#5B5650', width=3)
    
    # 头部（摩艾风格 - 长脸）
    head_points = [(300, 500), (500, 500), (480, 250), (430, 220), (370, 220), (320, 250)]
    draw.polygon(head_points, fill=stone_light, outline='#5B5650', width=3)
    
    # 阴影面
    draw.polygon([(400, 500), (500, 500), (480, 250), (430, 220), (400, 220)], fill='#989088')
    
    # 额头
    draw.polygon([(320, 250), (480, 250), (460, 200), (340, 200)], fill=stone_color, outline='#5B5650', width=2)
    
    # 眉毛/突出的额头
    draw.polygon([(310, 280), (490, 280), (485, 300), (315, 300)], fill=stone_dark, outline='#5B5650')
    
    # 大眼睛（摩艾有深邃的眼眶）
    # 眼眶
    draw.ellipse([340, 320, 400, 370], fill='#4A4540', outline='#3A3530', width=2)
    draw.ellipse([410, 320, 470, 370], fill='#4A4540', outline='#3A3530', width=2)
    
    # 可爱的眼睛
    draw_eyes(draw, 400, 345, size=16, look_direction=(0.2, 0))
    
    # 大鼻子（摩艾特色）
    nose_points = [(370, 380), (430, 380), (420, 480), (380, 480)]
    draw.polygon(nose_points, fill=stone_dark, outline='#5B5650', width=2)
    # 鼻梁高光
    draw.line([(395, 385), (395, 475)], fill='#B8B2A8', width=3)
    
    # 嘴巴（薄唇）
    draw.line([(370, 490), (430, 490)], fill='#5B5650', width=3)
    draw.arc([370, 485, 430, 505], start=0, end=180, fill='#5B5650', width=2)
    
    # 耳朵
    draw.ellipse([280, 350, 310, 420], fill=stone_color, outline='#5B5650', width=2)
    draw.ellipse([490, 350, 520, 420], fill='#989088', outline='#5B5650', width=2)
    
    # 腮红
    draw_blush(draw, 330, 400, size=10)
    draw_blush(draw, 470, 400, size=10)
    
    # 地面
    draw.rectangle([0, 750, 800, 800], fill='#C4B5A0')

def draw_havana(draw, width, height):
    """绘制哈瓦那老城"""
    # 彩色建筑 - 典型的加勒比风格
    building_colors = ['#FF6B6B', '#4ECDC4', '#FFE66D', '#95E1D3', '#F38181']
    
    # 建筑1 - 粉色殖民建筑
    draw.rectangle([100, 400, 250, 700], fill='#FF8FA3', outline='#E06070', width=2)
    # 窗户
    for y in [450, 520, 590]:
        draw.rectangle([130, y, 170, y + 50], fill='#4A3C2A', outline='#6B5A40', width=2)
        draw.rectangle([180, y, 220, y + 50], fill='#4A3C2A', outline='#6B5A40', width=2)
        # 百叶窗
        for yy in range(y, y + 50, 10):
            draw.line([(130, yy), (170, yy)], fill='#3A2C1A', width=1)
            draw.line([(180, yy), (220, yy)], fill='#3A2C1A', width=1)
    # 阳台
    draw.rectangle([120, 500, 230, 520], fill='#8B7355')
    for x in range(125, 230, 15):
        draw.line([(x, 500), (x, 520)], fill='#6B5A40', width=2)
    # 眼睛
    draw_eyes(draw, 175, 420, size=14, look_direction=(0.3, 0))
    
    # 建筑2 - 黄色主建筑（中间）
    draw.rectangle([280, 350, 520, 700], fill='#FFD93D', outline='#E5C020', width=2)
    # 装饰性顶部
    draw.polygon([(270, 350), (400, 280), (530, 350)], fill='#FFA500')
    # 拱形窗户
    draw.arc([310, 400, 370, 480], start=0, end=180, fill='#5A4A3A', width=3)
    draw.arc([430, 400, 490, 480], start=0, end=180, fill='#5A4A3A', width=3)
    draw.rectangle([310, 440, 370, 480], fill='#6B5A4A')
    draw.rectangle([430, 440, 490, 480], fill='#6B5A4A')
    # 大门
    draw.arc([350, 550, 450, 700], start=0, end=180, fill='#4A3C2A', width=3)
    draw.rectangle([350, 625, 450, 700], fill='#5A4A3A')
    # 主眼睛
    draw_eyes(draw, 400, 390, size=18, look_direction=(0, 0))
    draw_cute_mouth(draw, 400, 425, size=12, happy=True)
    draw_blush(draw, 340, 400)
    draw_blush(draw, 460, 400)
    
    # 建筑3 - 蓝色建筑
    draw.rectangle([550, 420, 700, 700], fill='#5BC0DE', outline='#3AA0BE', width=2)
    for y in [470, 540, 610]:
        draw.rectangle([570, y, 620, y + 45], fill='#4A4A4A', outline='#3A3A3A', width=2)
        draw.rectangle([630, y, 680, y + 45], fill='#4A4A4A', outline='#3A3A3A', width=2)
    # 眼睛
    draw_eyes(draw, 625, 450, size=14, look_direction=(-0.3, 0))
    
    # 老爷车 - 古巴特色
    car_color = '#E74C3C'
    # 车身
    draw.polygon([(200, 680), (350, 680), (340, 640), (220, 640)], fill=car_color, outline='#C0392B', width=2)
    draw.rectangle([180, 650, 370, 700], fill=car_color, outline='#C0392B', width=2)
    # 车顶
    draw.polygon([(220, 640), (240, 610), (320, 610), (340, 640)], fill='#87CEEB', outline='#5DADE2', width=2)
    # 轮子
    draw.ellipse([190, 685, 230, 725], fill='#2C3E50', outline='#1A252F', width=3)
    draw.ellipse([320, 685, 360, 725], fill='#2C3E50', outline='#1A252F', width=3)
    draw.ellipse([200, 695, 220, 715], fill='#95A5A6')
    draw.ellipse([330, 695, 350, 715], fill='#95A5A6')
    # 车灯
    draw.ellipse([355, 660, 370, 675], fill='#F1C40F', outline='#F39C12')
    # 保险杠
    draw.rectangle([175, 680, 185, 700], fill='#95A5A6')
    
    # 街道
    draw.rectangle([0, 700, 800, 800], fill='#A0A0A0')
    # 人行道
    draw.rectangle([0, 700, 800, 720], fill='#C0C0C0')

def draw_dunn_river(draw, width, height):
    """绘制邓恩河瀑布"""
    # 背景山
    draw.polygon([(0, 500), (200, 300), (400, 450), (600, 280), (800, 500), (800, 800), (0, 800)], fill='#228B22', outline='#1A6B1A')
    
    # 瀑布水流 - 多层
    waterfall_color = '#87CEEB'
    foam_color = '#E0F7FF'
    
    # 瀑布主体
    waterfall_points = [(300, 250), (500, 250), (480, 750), (320, 750)]
    draw.polygon(waterfall_points, fill='#5DADE2', outline='#4A90D9', width=2)
    
    # 瀑布层次（梯田式）
    for i, y in enumerate(range(280, 750, 50)):
        width_factor = 1 - (y - 280) / 470
        left_x = 320 + (1 - width_factor) * 50
        right_x = 480 - (1 - width_factor) * 50
        
        # 水流纹理
        for x in range(int(left_x) + 10, int(right_x), 20):
            draw.line([(x, y), (x + 5, y + 40)], fill='#87CEEB', width=3)
        
        # 泡沫层
        foam_y = y + 45
        draw.ellipse([left_x - 10, foam_y, right_x + 10, foam_y + 15], fill=foam_color, outline='white')
    
    # 两侧岩石
    rock_color = '#7A6B5A'
    draw.polygon([(200, 800), (300, 250), (320, 280), (320, 750), (350, 800)], fill=rock_color, outline='#5A4B3A')
    draw.polygon([(600, 800), (500, 250), (480, 280), (480, 750), (450, 800)], fill='#8B7B6A', outline='#5A4B3A')
    
    # 热带植被
    for x, y in [(150, 550), (180, 500), (620, 520), (650, 480), (200, 350), (600, 330)]:
        # 棕榈树
        draw.line([(x, y), (x, y - 80)], fill='#8B4513', width=6)
        # 叶子
        for angle in range(0, 360, 45):
            lx = x + int(40 * (1 if angle < 180 else -1))
            ly = y - 80 + int(20 * ((angle % 180) / 90 - 1))
            draw.polygon([(x, y-80), (lx, ly), (x + int(lx-x)*0.7, ly - 10)], fill='#228B22', outline='#1A6B1A')
    
    # 瀑布脸
    draw_eyes(draw, 400, 400, size=20, look_direction=(0, -0.2))
    draw_cute_mouth(draw, 400, 440, size=14, happy=True)
    draw_blush(draw, 340, 410)
    draw_blush(draw, 460, 410)
    
    # 底部水花
    for i in range(20):
        x = 320 + (i % 10) * 18
        y = 730 + (i // 10) * 15
        size = 8 + (i % 5)
        draw.ellipse([x, y, x + size, y + size], fill=foam_color, outline='white')

def draw_panama_canal(draw, width, height):
    """绘制巴拿马运河船闸"""
    # 天空和背景
    
    # 运河墙体
    wall_color = '#A0A0A0'
    wall_dark = '#808080'
    
    # 左侧墙体
    draw.polygon([(0, 300), (250, 300), (250, 750), (0, 800)], fill=wall_color, outline='#707070', width=2)
    # 右侧墙体
    draw.polygon([(550, 300), (800, 300), (800, 800), (550, 750)], fill=wall_dark, outline='#707070', width=2)
    
    # 船闸大门
    gate_color = '#E74C3C'
    # 上闸门
    draw.polygon([(240, 350), (560, 350), (560, 450), (240, 450)], fill=gate_color, outline='#C0392B', width=3)
    # 闸门细节
    for y in [370, 390, 410, 430]:
        draw.line([(240, y), (560, y)], fill='#C0392B', width=2)
    for x in [300, 380, 460, 520]:
        draw.line([(x, 350), (x, 450)], fill='#C0392B', width=2)
    
    # 下闸门
    draw.polygon([(240, 600), (560, 600), (560, 700), (240, 700)], fill=gate_color, outline='#C0392B', width=3)
    for y in [620, 640, 660, 680]:
        draw.line([(240, y), (560, y)], fill='#C0392B', width=2)
    
    # 水体
    water_color = '#5DADE2'
    draw.polygon([(250, 450), (550, 450), (550, 600), (250, 600)], fill=water_color, outline='#4A90D9')
    # 水波纹
    for y in [470, 500, 530, 560]:
        draw.arc([280, y, 520, y + 20], start=0, end=180, fill='#87CEEB', width=2)
    
    # 货船
    ship_color = '#E8E8E8'
    draw.polygon([(300, 480), (500, 480), (480, 550), (320, 550)], fill=ship_color, outline='#C0C0C0', width=2)
    # 船舱
    draw.rectangle([340, 440, 460, 480], fill='#D0D0D0', outline='#B0B0B0', width=2)
    draw.rectangle([360, 410, 440, 440], fill='#E0E0E0', outline='#C0C0C0', width=2)
    # 船桥
    draw.rectangle([380, 380, 420, 410], fill='white', outline='#C0C0C0', width=2)
    # 烟囱
    draw.rectangle([390, 350, 400, 380], fill='#E74C3C', outline='#C0392B')
    draw.rectangle([405, 355, 415, 380], fill='#E74C3C', outline='#C0392B')
    # 烟雾
    draw_cloud(draw, 395, 330, size=20)
    draw_cloud(draw, 410, 310, size=15)
    
    # 船的眼睛
    draw_eyes(draw, 400, 510, size=15, look_direction=(0, 0))
    draw_cute_mouth(draw, 400, 540, size=10, happy=True)
    
    # 闸门眼睛
    draw_eyes(draw, 400, 390, size=14, look_direction=(0.2, 0))
    
    # 热带植被
    for x, y in [(50, 650), (100, 600), (700, 620), (750, 580), (150, 550)]:
        draw_tropical_leaf(draw, x, y, size=40, color='#228B22')
        draw_tropical_leaf(draw, x + 20, y + 10, size=30, color='#2E8B57')
    
    # 地面
    draw.rectangle([0, 750, 800, 800], fill='#8B7355')

def draw_arenal(draw, width, height):
    """绘制阿雷纳尔火山"""
    # 火山主体
    volcano_color = '#4A3728'
    volcano_light = '#6B5344'
    
    # 山体
    draw.polygon([(100, 750), (400, 150), (700, 750)], fill=volcano_color, outline='#3A2718', width=3)
    
    # 山体纹理/层次
    draw.polygon([(200, 750), (400, 250), (600, 750)], fill=volcano_light, outline='#5A4334')
    draw.polygon([(280, 750), (400, 350), (520, 750)], fill='#7B6354', outline='#6B5344')
    
    # 火山口
    draw.ellipse([360, 130, 440, 170], fill='#2A1A10', outline='#1A0A00', width=2)
    
    # 喷发的烟雾
    smoke_color = '#A0A0A0'
    for i, (sx, sy, ss) in enumerate([(400, 120, 30), (380, 90, 40), (420, 70, 35), (400, 40, 45), (390, 10, 50)]):
        alpha = 200 - i * 30
        draw.ellipse([sx - ss, sy - ss//2, sx + ss, sy + ss//2], fill='#D0D0D0', outline='#B0B0B0')
    
    # 岩浆流出
    lava_color = '#E74C3C'
    lava_points = [(380, 170), (420, 170), (410, 300), (390, 280)]
    draw.polygon(lava_points, fill=lava_color, outline='#C0392B', width=2)
    # 岩浆纹理
    draw.line([(395, 180), (395, 260)], fill='#FF6B6B', width=4)
    draw.line([(405, 190), (405, 270)], fill='#FF6B6B', width=3)
    
    # 火山眼睛
    draw_eyes(draw, 400, 350, size=22, look_direction=(0, -0.3))
    draw_cute_mouth(draw, 400, 395, size=12, happy=True)
    draw_blush(draw, 330, 360)
    draw_blush(draw, 470, 360)
    
    # 山脚下的植被
    for x in range(50, 800, 80):
        height_var = 50 + (x % 30)
        draw_tropical_leaf(draw, x, 730, size=35, color='#228B22')
        draw_tropical_leaf(draw, x + 25, 720, size=28, color='#2E8B57')
    
    # 森林
    for x in range(30, 800, 100):
        y = 680 + (x % 40)
        # 树冠
        draw.ellipse([x - 30, y - 50, x + 30, y + 10], fill='#228B22', outline='#1A6B1A')
        draw.ellipse([x - 20, y - 70, x + 20, y - 20], fill='#2E8B57', outline='#1E7B47')
        # 树干
        draw.rectangle([x - 8, y, x + 8, y + 80], fill='#8B4513', outline='#6B3510')
    
    # 地面
    draw.rectangle([0, 750, 800, 800], fill='#3A7A3A', outline='#2A6A2A')

def main():
    output_dir = '/Users/moutai/Desktop/toweroffate_v1.0/assets/towers'
    os.makedirs(output_dir, exist_ok=True)
    
    towers = [
        ('machu-picchu.png', '马丘比丘', draw_machu_picchu),
        ('obelisk.png', '方尖碑', draw_obelisk),
        ('easter-island.png', '复活节岛', draw_easter_island),
        ('havana.png', '哈瓦那老城', draw_havana),
        ('dunn-river.png', '邓恩河瀑布', draw_dunn_river),
        ('panama-canal.png', '巴拿马运河', draw_panama_canal),
        ('arenal.png', '阿雷纳尔火山', draw_arenal),
    ]
    
    width, height = 800, 1200
    
    for filename, name, draw_func in towers:
        print(f"Generating {filename}...")
        
        # 创建渐变背景
        img = create_gradient_background(width, height, '#87CEEB', '#E0F6FF')
        draw = ImageDraw.Draw(img)
        
        # 添加装饰云朵
        draw_cloud(draw, 100, 100, size=40)
        draw_cloud(draw, 650, 150, size=50)
        draw_cloud(draw, 700, 80, size=35)
        
        # 绘制主体
        draw_func(draw, width, height)
        
        # 添加文字
        add_text(draw, name, 1080, width, font_size=56)
        
        # 保存
        filepath = os.path.join(output_dir, filename)
        img.save(filepath, 'PNG')
        print(f"  Saved: {filepath}")
    
    print("\nAll towers generated successfully!")

if __name__ == '__main__':
    main()
