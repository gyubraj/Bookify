from django.db import models

# Create your models here.
class HomeSlide(models.Model):
    image=models.ImageField(upload_to='homeSlide')
    text1=models.CharField(max_length=200, null=True, blank=True)
    text2=models.CharField(max_length=200, null=True, blank=True)
    show=models.BooleanField(default=True)
