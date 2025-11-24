#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
import os

w, h = 1200, 630
bg = (24, 52, 88)
img = Image.new("RGB", (w, h), bg)
draw = ImageDraw.Draw(img)

colors = [(43, 160, 89), (237, 28, 36), (255, 153, 0), (0, 168, 255)]
size = 90
spacing = 20
start_x = w // 2 - ((size * 4) + (spacing * 3)) // 2
start_y = h // 2 - 180

for i, color in enumerate(colors):
    x = start_x + i * (size + spacing)
    draw.rounded_rectangle([x, start_y, x + size, start_y + size], radius=15, fill=color)
    draw.rectangle([x, start_y + size - 15, x + size, start_y + size], fill=bg)

font_paths = [
    "C:/Windows/Fonts/arialbd.ttf",
    "C:/Windows/Fonts/malgunbd.ttf",
]

def load_font(size, fallback=ImageFont.load_default()):
    for path in font_paths:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                continue
    return fallback

def text_size(text, font):
    bbox = draw.textbbox((0, 0), text, font=font)
    return bbox[2] - bbox[0], bbox[3] - bbox[1]

title_font = load_font(80)
title = "DOCU Co., Ltd."
text_w, text_h = text_size(title, title_font)
draw.text(((w - text_w) // 2, start_y + size + 40), title, font=title_font, fill=(255, 255, 255))

big_font = load_font(200)
big_text = "DOCU"
text_w, text_h = text_size(big_text, big_font)
draw.text(((w - text_w) // 2, (h + 60) // 2), big_text, font=big_font, fill=(255, 255, 255))

small_font = load_font(48)
desc = u"기업 소개만 하면 현금 페이백"
desc_w, desc_h = text_size(desc, small_font)
draw.text(((w - desc_w) // 2, h - 150), desc, font=small_font, fill=(255, 214, 0))

output_dir = os.path.join("officehub.kr", "event", "img")
os.makedirs(output_dir, exist_ok=True)
img_path = os.path.join(output_dir, "docu-og.png")
img.save(img_path)

print("OG image created at", img_path)

