import os
import argparse
from PIL import Image, UnidentifiedImageError

SUPPORTED_FORMATS = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp')


def resize_image(img, width=None, height=None):
    if width is None and height is None:
        return img

    original_width, original_height = img.size

    if width and height:
        return img.resize((width, height), Image.LANCZOS)

    if width:
        ratio = width / original_width
        height = int(original_height * ratio)

    elif height:
        ratio = height / original_height
        width = int(original_width * ratio)

    return img.resize((width, height), Image.LANCZOS)


def convert_images(
    folder_path,
    prefix,
    quality,
    recursive,
    overwrite,
    keep_name,
    width,
    height
):
    if not os.path.exists(folder_path):
        print(f"[ERROR] Folder does not exist: {folder_path}")
        return

    counter = 1

    def process_file(file_path, output_dir):
        nonlocal counter

        try:
            with Image.open(file_path) as img:
                # Convert mode
                if img.mode in ("RGBA", "LA"):
                    img = img.convert("RGBA")
                else:
                    img = img.convert("RGB")

                # Resize if needed
                img = resize_image(img, width, height)

                # Naming
                if keep_name:
                    base = os.path.splitext(os.path.basename(file_path))[0]
                    filename = f"{base}.webp"
                else:
                    filename = f"{prefix}_{counter}.webp"

                output_path = os.path.join(output_dir, filename)

                # Avoid overwrite
                if not overwrite:
                    temp_counter = counter
                    while os.path.exists(output_path):
                        if keep_name:
                            filename = f"{base}_{temp_counter}.webp"
                        else:
                            filename = f"{prefix}_{temp_counter}.webp"
                        output_path = os.path.join(output_dir, filename)
                        temp_counter += 1

                img.save(output_path, "WEBP", quality=quality)
                print(f"[OK] {file_path} → {output_path}")
                counter += 1

        except UnidentifiedImageError:
            print(f"[SKIP] Not an image: {file_path}")
        except Exception as e:
            print(f"[ERROR] {file_path}: {e}")

    def process_dir(path):
        for item in os.listdir(path):
            full_path = os.path.join(path, item)

            if os.path.isdir(full_path) and recursive:
                process_dir(full_path)
            elif os.path.isfile(full_path):
                if item.lower().endswith(SUPPORTED_FORMATS):
                    process_file(full_path, path)
                else:
                    print(f"[SKIP] Unsupported: {full_path}")

    process_dir(folder_path)
    print("\n✅ Done!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert images to WebP format")

    parser.add_argument("folder", help="Folder path containing images")
    parser.add_argument("--prefix", default="img", help="Prefix for output filenames")
    parser.add_argument("--quality", type=int, default=85, help="WebP quality (0-100)")
    parser.add_argument("--recursive", action="store_true", help="Process subfolders")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing files")
    parser.add_argument("--keep-name", action="store_true", help="Keep original filenames")

    # Resize options
    parser.add_argument("--width", type=int, help="Resize width")
    parser.add_argument("--height", type=int, help="Resize height")

    args = parser.parse_args()

    convert_images(
        folder_path=args.folder,
        prefix=args.prefix,
        quality=args.quality,
        recursive=args.recursive,
        overwrite=args.overwrite,
        keep_name=args.keep_name,
        width=args.width,
        height=args.height
    )
