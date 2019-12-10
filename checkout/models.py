from django.db import models



# Create your models here.
class CheckOut(models.Model):
    sellerid=models.IntegerField()
    buyerid=models.IntegerField()
    bookid=models.IntegerField()
    status=models.CharField(max_length=100, default="available")
    transaction_date=models.DateField(auto_now_add=True)

   

  



    

