import os
import shutil
import argparse
import sys

def copy_and_sort(src_dir, dest_dir="dist"):
    try:
        for item in os.listdir(src_dir):
            src_path = os.path.join(src_dir, item)

            if os.path.isdir(src_path):
                copy_and_sort(src_path, dest_dir)  
            else:
                ext = os.path.splitext(item)[1][1:] or "no_extension"
                ext_dir = os.path.join(dest_dir, ext)

                os.makedirs(ext_dir, exist_ok=True)

                dest_path = os.path.join(ext_dir, item)

                shutil.copy2(src_path, dest_path)
    except Exception as e:
        print(f"Помилка при обробці {src_dir}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Recursive file sorter",
        usage="python task1.py <source_dir> [destination_dir]\n\n"
              "Приклади:\n"
              "  python task1.py ./source\n"
              "  python task1.py ./source ./dist"
    )

    parser.add_argument("src", nargs="?", help="Шлях до вихідної директорії")
    parser.add_argument("dest", nargs="?", default="dist", help="Шлях до директорії призначення")

    args = parser.parse_args()

    if not args.src:
        parser.print_help(sys.stderr)
        sys.exit(1)

    if not os.path.exists(args.src):
        print(f"❌ Вказана директорія '{args.src}' не існує.")
        sys.exit(1)

    copy_and_sort(args.src, args.dest)
    print(f"✅ Файли скопійовані та відсортовані у '{args.dest}'")


