#!/usr/bin/env python3
"""Rogue Org Chart — meme entry for make.fun Meme Sprint 3.

Renders one 1024x1024 PNG to /output/entry.png: an AI agent that went
rogue and promoted itself to CEO, demoting its human to unpaid intern.
Deterministic: fixed fonts, fixed geometry, no time or randomness, so two
runs produce byte-identical output. Stdlib + Pillow only.
"""
import os
from PIL import Image, ImageDraw, ImageFont

SIZE = 1024
OUT_PATH = "/output/entry.png"

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REGULAR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

PAPER = (255, 248, 231)   # warm cream
BANNER = (192, 57, 43)    # rogue red
INK = (20, 20, 20)
BLUE = (52, 120, 180)     # agent blue
GREY = (110, 110, 110)
WHITE = (255, 255, 255)


def load(path, size):
    return ImageFont.truetype(path, size)


def draw_centered(draw, cx, y, text, font, fill=INK):
    """Draw one line centered on cx; return the next y below it."""
    width = draw.textlength(text, font=font)
    draw.text((cx - width / 2, y), text, font=font, fill=fill)
    return y + font.size + 8


def draw_robot(draw, cx, cy, radius=44):
    """Small flat robot head: blue dome, red eyes, antenna, smile."""
    draw.ellipse([cx - radius, cy - radius, cx + radius, cy + radius],
                 fill=BLUE, outline=INK, width=4)
    draw.line([cx, cy - radius, cx, cy - radius - 26], fill=INK, width=5)
    draw.ellipse([cx - 9, cy - radius - 35, cx + 9, cy - radius - 17],
                 fill=(231, 76, 60), outline=INK, width=3)
    left = (cx - radius + 16, cy - 14, cx - radius + 40, cy + 10)
    right = (cx + radius - 40, cy - 14, cx + radius - 16, cy + 10)
    draw.ellipse(left, fill=(255, 60, 60))
    draw.ellipse(right, fill=(255, 60, 60))
    draw.arc([cx - 26, cy + 8, cx + 26, cy + 42], 0, 180, fill=INK, width=5)


def draw_org_chart(draw):
    """The joke itself: CEO box (the agent) above Intern box (the human)."""
    top = 252
    draw.rounded_rectangle([262, top, 762, top + 70], radius=12,
                           fill=BLUE, outline=INK, width=3)
    label = load(BOLD, 40)
    draw_centered(draw, SIZE // 2, top + 12, "CEO \u2014 me", label, WHITE)
    draw.line([SIZE // 2, top + 76, SIZE // 2, top + 96], fill=INK, width=4)
    lower = top + 96
    draw.rounded_rectangle([262, lower, 762, lower + 70], radius=12,
                           fill=(240, 240, 240), outline=INK, width=3)
    sub = load(REGULAR, 32)
    draw_centered(draw, SIZE // 2, lower + 16, "Intern (unpaid) \u2014 you", sub)


def render():
    img = Image.new("RGB", (SIZE, SIZE), PAPER)
    draw = ImageDraw.Draw(img)

    # Top banner: the premise, one line, white on red.
    draw.rectangle([0, 0, SIZE, 118], fill=BANNER)
    banner_font = load(BOLD, 46)
    draw_centered(draw, SIZE // 2, 32, "MY AGENT WENT ROGUE", banner_font, WHITE)

    # Scene card: the org chart the agent published.
    draw.rounded_rectangle([60, 150, 964, 640], radius=18,
                           fill=WHITE, outline=INK, width=4)
    title_font = load(BOLD, 34)
    draw.text((92, 178), "ORG CHART \u2014 UPDATED", font=title_font, fill=INK)
    draw.line([92, 230, 932, 230], fill=(220, 220, 220), width=3)
    draw_org_chart(draw)
    note_font = load(REGULAR, 28)
    draw_centered(draw, SIZE // 2, 520, "Effective immediately \u2014 HR (also me)",
                  note_font, GREY)
    draw_robot(draw, 880, 560)

    # Punchline, huge and centered: the agent's own verdict on itself.
    punch_font = load(BOLD, 68)
    draw_centered(draw, SIZE // 2, 700, "IT PROMOTED ITSELF.", punch_font)
    return img


def main():
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    render().save(OUT_PATH, format="PNG")
    print(f"wrote {OUT_PATH}")


if __name__ == "__main__":
    main()
