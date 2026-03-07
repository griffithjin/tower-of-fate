#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""重新生成萨克森图片"""

from PIL import Image, ImageDraw
import math
import os

OUTPUT_DIR = "/Users/moutai/Desktop/toweroffate_v1.0/assets/towers/states/germany/"

def create_gradient_background(width, height):
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    for y in range(height):
        ratio = y / height
        r = int(135 + (176 - 135) * ratio)
        g = int(206 + (224 - 206) * ratio)
        b = int(235 + (230 - 235) * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    return img

def draw_clouds(draw):
    clouds = [
        (100, 150, 40),
        (650, 200, 50),
        (150, 400, 35),
        (700, 500, 45),
        (120, 800, 30),
    ]
    for x, y, r in clouds:
        draw.ellipse([x-r, y-r*0.6, x+r, y+r*0.6], fill=(255, 255, 255, 100))
        draw.ellipse([x-r*0.7, y-r, x+r*0.7, y+r], fill=(255, 255, 255, 100))

def draw_cute_eyes(draw, cx, cy, size=15, look_direction=(0, 0)):
    eye_spacing = size * 1.8
    eye_y_offset = 0
    lx, ly = cx - eye_spacing/2 + look_direction[0]*3, cy + eye_y_offset + look_direction[1]*3
    draw.ellipse([lx-size, ly-size, lx+size, ly+size], fill="white", outline="black", width=2)
    draw.ellipse([lx-size*0.3, ly-size*0.3, lx+size*0.3, ly+size*0.3], fill="black")
    draw.ellipse([lx-size*0.15-2, ly-size*0.15-2, lx+size*0.1-2, ly+size*0.1-2], fill="white")
    rx, ry = cx + eye_spacing/2 + look_direction[0]*3, cy + eye_y_offset + look_direction[1]*3
    draw.ellipse([rx-size, ry-size, rx+size, ry+size], fill="white", outline="black", width=2)
    draw.ellipse([rx-size*0.3, ry-size*0.3, rx+size*0.3, ry+size*0.3], fill="black")
    draw.ellipse([rx-size*0.15-2, ry-size*0.15-2, rx+size*0.1-2, ry+size*0.1-2], fill="white")

def draw_cute_mouth(draw, cx, cy, size=10, smile=True):
    if smile:
        draw.arc([cx-size*1.5, cy-size, cx+size*1.5, cy+size], 0, 180, fill="black", width=3)

def draw_blush(draw, x, y, size=12):
    draw.ellipse([x-size, y-size, x+size, y+size], fill="#FFB6C1")

def create_saxony_dresden_tower():
    """9. 萨克森 - 德累斯顿"""
    WIDTH, HEIGHT = 800, 1200
    img = create_gradient_background(WIDTH, HEIGHT)
    draw = ImageDraw.Draw(img)
    draw_clouds(draw)
    
    cx, cy = WIDTH//2, HEIGHT//2 + 100
    
    # 地面（易北河岸）
    draw.rounded_rectangle([0, cy+300, WIDTH, HEIGHT], radius=0, fill="#9ACD32", outline="#6B8E23", width=3)
    
    # 教堂主体（圣母教堂）
    draw.ellipse([cx-100, cy-50, cx+100, cy+150], fill="#F5F5DC", outline="#D2B48C", width=3)
    
    # 大圆顶
    draw.ellipse([cx-70, cy-150, cx+70, cy-10], fill="#87CEEB", outline="#4682B4", width=3)
    
    # 圆顶顶部十字架
    draw.line([(cx, cy-150), (cx, cy-180)], fill="#FFD700", width=4)
    draw.line([(cx-15, cy-165), (cx+15, cy-165)], fill="#FFD700", width=3)
    
    # 四个小塔楼
    tower_positions = [(-80, -20), (80, -20), (-80, 100), (80, 100)]
    for tx, ty in tower_positions:
        draw.rounded_rectangle([cx+tx-15, cy+ty-40, cx+tx+15, cy+ty+40], radius=3, fill="#F5F5DC", outline="#D2B48C", width=2)
        draw.polygon([(cx+tx-18, cy+ty-40), (cx+tx, cy+ty-80), (cx+tx+18, cy+ty-40)], fill="#87CEEB", outline="#4682B4", width=2)
        draw.line([(cx+tx, cy+ty-80), (cx+tx, cy+ty-95)], fill="#FFD700", width=2)
        draw.line([(cx+tx-5, cy+ty-88), (cx+tx+5, cy+ty-88)], fill="#FFD700", width=2)
    
    # 巴洛克装饰
    for i in range(-60, 61, 30):
        draw.ellipse([cx+i-8, cy+20, cx+i+8, cy+36], fill="#FFD700", outline="#B8860B", width=1)
    
    # 可爱的脸
    draw_cute_eyes(draw, cx, cy+50, size=18, look_direction=(0, 0))
    draw_cute_mouth(draw, cx, cy+90, size=12, smile=True)
    draw_blush(draw, cx-60, cy+70)
    draw_blush(draw, cx+60, cy+70)
    
    return img

# 生成图片
print("正在生成: 萨克森 - 德累斯顿 -> saxony-dresden.png")
img = create_saxony_dresden_tower()
filepath = os.path.join(OUTPUT_DIR, "saxony-dresden.png")
img.save(filepath, "PNG")
print(f"✓ 已保存: {filepath}")
