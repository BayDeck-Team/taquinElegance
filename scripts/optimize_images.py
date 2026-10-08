"""Generate small, correctly sized website images from the original artwork.

Run from any directory: python3 scripts/optimize_images.py
Requires Pillow: python3 -m pip install Pillow
"""
from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "public" / "assets"


def export(image, name, width, quality=83):
    height = round(image.height * width / image.width)
    image.resize((width, height), Image.Resampling.LANCZOS).save(
        OUTPUT / name, "WEBP", quality=quality, method=6
    )


def main():
    OUTPUT.mkdir(parents=True, exist_ok=True)
    classic = Image.open(ROOT / "02-classic-iphone-1920x886.png").convert("RGB")
    phone = classic.crop((1155, 8, 1613, 874))
    for width in (240, 320, 480):
        export(phone, f"classic-{width}.webp", width)
    challenge = Image.open(ROOT / "01-challenge-iphone-1920x886.png").convert("RGB")
    export(challenge.crop((1030, 1, 1478, 869)), "challenge.webp", 448)
    export(challenge.crop((1030, 1, 1478, 869)), "challenge-240.webp", 240)
    pictures = Image.open(ROOT / "04-pictures-iphone-1920x886.png").convert("RGB")
    export(pictures.crop((1135, 9, 1645, 874)), "pictures.webp", 510)
    export(pictures.crop((1135, 9, 1645, 874)), "pictures-260.webp", 260)
    ipad = Image.open(ROOT / "02-your-pace-ipad-2732x2048.png").convert("RGB")
    for width in (400, 800, 1400):
        export(ipad, f"ipad-{width}.webp", width)
    ImageOps.pad(classic, (1200, 630), color="#faf7f0").save(
        OUTPUT / "social.jpg", "JPEG", quality=85, optimize=True
    )
    for path in sorted(OUTPUT.iterdir()):
        print(f"{path.name}: {path.stat().st_size / 1024:.1f} KiB")


if __name__ == "__main__":
    main()
