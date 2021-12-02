from django.db import models
from django.urls import reverse
# Create your models here

# model API
class API(models.Model):
    img_path = models.ImageField(null=False, blank=False)
    
    def __str__(self):
        return str(self.img_path)
    
    #url pk
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})