from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parent.parent D:\
# BASE_DIR = Path(__file__).resolve().parent D:\yolo
# BASE_DIR = Path(__file__).resolve() D:\yolo\pa.py
# BASE_DIR = Path(__file__) D:\yolo\pa.py

BASE_DIR = Path(__file__).resolve(strict=True).parent  #D:\yolo

print(BASE_DIR)