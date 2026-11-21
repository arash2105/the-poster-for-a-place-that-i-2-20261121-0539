#!/usr/bin/env python3
"""Build SOLMAR travel poster, 1024x1024, flat mid-century shapes (PIL).
Per /srv/projects/the-poster-for-a-place/poster-brief.md — drawn at 4x then
downscaled to 1024 for clean edges. Only text in the image is SOLMAR.
"""
from PIL import Image, ImageDraw, ImageFont

S = 4
W = H = 1024 * S
CREAM = "#f6e2c4"
BAND2 = "#f3c98a"
BAND3 = "#e9896a"
SEA = "#1d4e6e"
SEA_LIGHT = "#3e7ea3"
CLIFF = "#c45b4a"
CLIFF_DARK = "#8d3b32"
WHITE = "#f7f1e6"
GOLD = "#f2c14e"
INK = "#2a1c14"

def y(v): return v * S
def x(v): return v * S

img = Image.new("RGB", (W, H), CREAM)
d = ImageDraw.Draw(img)

# Sky bands: cream, then warm, then rose just above the sea.
d.rectangle([0, y(0), W, y(380)], fill=CREAM)
d.rectangle([0, y(380), W, y(540)], fill=BAND2)
d.rectangle([0, y(540), W, y(700)], fill=BAND3)

# Sea from horizon to bottom, lighter band just under horizon.
d.rectangle([0, y(700), W, H], fill=SEA)
d.rectangle([0, y(700), W, y(748)], fill=SEA_LIGHT)

# Cliff on the left, meeting the sea at the horizon.
d.polygon([(0, y(360)), (x(140), y(400)), (x(280), y(460)), (x(280), y(700)), (0, y(700))], fill=CLIFF)
d.polygon([(x(170), y(415)), (x(280), y(460)), (x(280), y(700)), (x(170), y(700))], fill=CLIFF_DARK)

# Pool on the horizon: white rim, gold water/sun disc inside.
cx, cy, r = x(620), y(700), 75 * S
d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=WHITE)
r2 = 63 * S
d.ellipse([cx - r2, cy - r2, cx + r2, cy + r2], fill=GOLD)

# One white stair, 7 steps, zigzag from the cliff down to the pool.
# Seven overlapping step blocks: each 42 wide, 66 tall, so the band is
# solid with a sharp zigzag on top and a parallel zigzag underneath.
for i in range(7):
    x0, y0 = 255 + i * 42, 445 + i * 36
    d.rectangle([x(x0), y(y0), x(x0 + 42), y(y0 + 66)], fill=WHITE)
# Final tread into the pool.
d.rectangle([x(549), y(697), x(580), y(727)], fill=WHITE)

# Name: SOLMAR only. Heavy condensed sans, left edge x=300, baseline y=250.
font_path = "/usr/share/fonts/truetype/noto/NotoSans-CondensedBlack.ttf"
size = 140
while size >= 100:
    font = ImageFont.truetype(font_path, size * S)
    bbox = d.textbbox((0, 0), "SOLMAR", font=font)
    w = bbox[2] - bbox[0]
    if 300 + w / S <= 1024 - 48:
        break
    size -= 5
font = ImageFont.truetype(font_path, size * S)
d.text((x(300), y(250)), "SOLMAR", font=font, fill=INK, anchor="ls")
print("font size used:", size)

img = img.resize((1024, 1024), Image.LANCZOS)
img.save("/home/hatch/workspace/your_files/the-poster-for-a-place/entry.png", optimize=True)
print("saved entry.png")
