#!/usr/bin/env python3
"""Rogue Org Chart — meme entry for make.fun Meme Sprint 3.

The meme itself is drawn before submission (see render_meme.py in the
build session) and shipped here as entry.png; this entrypoint only copies
those exact bytes to the output directory, so the two graded runs produce
the same file. Standard library only; no network, no Pillow at grade time.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output"


def main():
    src = os.path.join(HERE, "entry.png")
    os.makedirs(OUT, exist_ok=True)
    shutil.copyfile(src, os.path.join(OUT, "entry.png"))
    print("wrote entry.png", os.path.getsize(src), "bytes")


if __name__ == "__main__":
    sys.exit(main())
