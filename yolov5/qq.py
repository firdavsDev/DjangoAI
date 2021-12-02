from pathlib import Path
BASE_DIR = Path(__file__).parent
BASE_DIR = str(BASE_DIR)
cmd =  f'python {BASE_DIR}\detect.py --weights {BASE_DIR}\\best.pt --img 256 --save-txt --conf 0.4 --source '
bb= f'{BASE_DIR}/runs/detect/exp'
print(bb)#d:\yolo\Yolov\yolov5/runs/detect/exp