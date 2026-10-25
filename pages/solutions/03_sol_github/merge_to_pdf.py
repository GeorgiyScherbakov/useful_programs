from pathlib import Path

from PIL import Image


def merge_images_to_pdf(output_pdf: Path, input_images: list[Path]) -> None:
    if not input_images:
        raise FileNotFoundError("No PNG files found in the merge folder.")

    images = [Image.open(path).convert("RGB") for path in input_images]
    first = images[0]
    remaining = images[1:]

    first.save(output_pdf, "PDF", resolution=100.0, save_all=True, append_images=remaining)


if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent
    merge_dir = base_dir / "merge"
    output_pdf = base_dir / "ikonografiki.pdf"

    png_files = sorted(merge_dir.glob("*.png"))
    merge_images_to_pdf(output_pdf, png_files)
    print(f"Zapisano PDF: {output_pdf}")
