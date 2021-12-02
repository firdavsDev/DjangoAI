from django.db.models import fields

from rest_framework import  serializers
from .model import API


# Img2Num
class ImagetoNumberSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = API
        fields = ['pk', 'img_path']
