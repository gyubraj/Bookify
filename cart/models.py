from django.db import models

# Create your models here.

class Cart(models.Model):
    userid=models.IntegerField()
    bookid=models.IntegerField()
    bookname=models.CharField(max_length=100)
    price=models.IntegerField()
    image=models.ImageField(upload_to='bphoto',blank=True,null=True)
    

