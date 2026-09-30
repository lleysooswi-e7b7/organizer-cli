#!/usr/bin/env python3
"""organizer.py - sort files in a folder into subfolders by extension."""
import os, sys, shutil, argparse

MAP = {
      "pdf": "docs", "docx": "docs", "txt": "docs", "xlsx": "docs",
      "jpg": "images", "jpeg": "images", "png": "images", "gif": "images", "webp": "images",
      "mp4": "videos", "mkv": "videos", "mov": "videos",
      "zip": "archives", "rar": "archives", "7z": "archives",
      "mp3": "audio", "wav": "audio",
}

def main():
      ap = argparse.ArgumentParser(description="Sort files by extension")
      ap.add_argument("folder", help="folder to organize")
      ap.add_argument("--dry-run", action="store_true", help="preview only")
      args = ap.parse_args()
      folder = os.path.expanduser(args.folder)
      moved = skipped = 0
      for name in os.listdir(folder):
                path = os.path.join(folder, name)
                if not os.path.isfile(path):
                              continue
                          ext = name.rsplit(".", 1)[-1].lower() if "." in name else "others"
                dest_dir = os.path.join(folder, MAP.get(ext, "others"))
                os.makedirs(dest_dir, exist_ok=True)
                dest = os.path.join(dest_dir, name)
                if os.path.exists(dest):
                              skipped += 1
                              continue
                          if not args.dry_run:
                                        shutil.move(path, dest)
                                    moved += 1
            print(f"{'[DRY RUN] ' if args.dry_run else ''}moved={moved} skipped={skipped}")

if __name__ == "__main__":
      main()
