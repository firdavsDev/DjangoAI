from datetime import date
from rest_framework import viewsets
from rest_framework.response import Response
from .model import API
from .serializers import ImagetoNumberSerializer

#folder path
from pathlib import Path
BASE_DIR = Path(__file__).parent #d:\yolo\Yolov\yolov5
BASE_DIR = str(BASE_DIR)

# AI imports
import os 
import shutil
import time
import numpy as np
import pandas as pd
import cv2 as cv

from django.http import HttpResponse
import json

ALLOWED_EXTENSIONS = {'jpg', 'jpeg'}


def sort_out_summary(data):
    try:
        output = data.sort_values(1)
        output = np.array(output.iloc[:, 0])
        return output
    except Exception as e:
        pass

# paths
def yolo_script(filename):
    try:
        cmd =  f'python {BASE_DIR}\detect.py --weights {BASE_DIR}\\best.pt --img 256 --save-txt --conf 0.4 --source '+filename
        os.system(cmd)
        path = os.path.splitext(os.path.basename(filename))[0]
        data = pd.read_csv(f'D:/yolo/Yolov/yolov5/runs/detect/exp/labels/{path}.txt', sep = ' ', header = None)
        #time
        time.sleep(1)
        #remove folder
        shutil.rmtree(f'{BASE_DIR}\\runs\detect\exp')
        return data
    except Exception as e:
        print(e)

def preprocess(img):
    try:
        size = (256, 256)
        src = cv.imread(img)
        gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
        resized = cv.resize(gray, size, interpolation = cv.INTER_LINEAR)
        cv.imwrite(img, resized)
        return
    except:
        pass

def image_to_numbers(file):
    try:
        preprocess(file)
        data = yolo_script(file)
        return sort_out_summary(data)
    except:
        pass

# Np encoder
class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            if isinstance(obj, np.integer):
                return int(obj)
            if isinstance(obj, np.floating):
                return float(obj)
            if isinstance(obj, np.ndarray):
                value_list = obj.tolist()
                return ''.join(str(v) for v in value_list)
        except:
            return 'Error'
        return super(NpEncoder, self).default(obj)


# ModelViewSet
class ImagetoNumberviewset(viewsets.ModelViewSet):
    try:
        queryset = API.objects.all().order_by('-id')
        serializer_class = ImagetoNumberSerializer
    except:
       pass
   
   # Post create
    def create(self, request, *args, **kwargs):
        try:
            #img file
            uploaded_file = request.FILES['img_path']
            #save upload pic
            new_obj = API.objects.create(img_path=uploaded_file)
            new_obj.save()
            # get last pic
            BASE_DIR = Path(__file__).resolve().parent.parent
            BASE_DIR = str(BASE_DIR)
            path = f'{BASE_DIR}{new_obj.img_path.url}'
            # responses
            numbers = image_to_numbers(path)
            paths = f'http://127.0.0.1:8000{new_obj.img_path.url}'
            
            ImagetoNumberSerializer(new_obj)
            #response
            responseData = {
            'numbers': numbers,
            'img_path': paths,
            }
        except Exception as e:
            return HttpResponse('e')
            # return Response(serializer.data)
        return HttpResponse(json.dumps(responseData, cls=NpEncoder), content_type="application/json")
            