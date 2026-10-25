from pathlib import Path
from PIL import Image

base_dir = Path(__file__).resolve().parent
images_dir = base_dir / "merge"
out_pdf = base_dir / "ikonografiki.pdf"

image_paths = sorted(images_dir.glob("*.png"), key=lambda p: int(p.stem))
if not image_paths:
    raise FileNotFoundError(f"No PNG files found in {images_dir}")

images = [Image.open(path).convert("RGB") for path in image_paths]

images[0].save(
    out_pdf,
    "PDF",
    resolution=200.0,
    save_all=True,
    append_images=images[1:],
)

print(f"Saved merged PDF to: {out_pdf}")
