"""LP用にスクショをリサイズして保存"""
from PIL import Image
import os

DOWNLOADS = os.path.expanduser("~/Downloads")
OUTPUT = os.path.dirname(__file__)

# (元ファイル, 出力ファイル名)
FILES = [
    ("ホーム.PNG", "ss_home.png"),
    ("散歩.PNG", "ss_walk.png"),
    ("散歩GPS.PNG", "ss_walk_gps.png"),
    ("体重.PNG", "ss_weight.png"),
    ("カルテ.PNG", "ss_carte.png"),
]

for src_name, dst_name in FILES:
    src = os.path.join(DOWNLOADS, src_name)
    img = Image.open(src)
    # ステータスバーカット（上5%）
    crop_top = int(img.height * 0.05)
    img = img.crop((0, crop_top, img.width, img.height))
    # AdMobバナー消し（ホームのみ）
    if src_name == "ホーム.PNG":
        from PIL import ImageDraw
        draw = ImageDraw.Draw(img)
        admob_top = 2050 - int(Image.open(src).height * 0.05)
        draw.rectangle([(0, admob_top), (img.width, admob_top + 240)], fill=(250, 248, 245))
    # リサイズ（横380px、phoneコンポーネント用）
    target_w = 380
    ratio = target_w / img.width
    target_h = int(img.height * ratio)
    img = img.resize((target_w, target_h), Image.LANCZOS)
    dst = os.path.join(OUTPUT, dst_name)
    img.save(dst, "PNG", quality=90)
    print(f"OK: {dst_name} ({target_w}x{target_h})")
