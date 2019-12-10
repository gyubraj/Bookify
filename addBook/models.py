from django.db import models
from homepage.utils import unique_slug_generator
from django.db.models.signals import pre_save,post_save 


# Create your models here.
class Book(models.Model):
    slug=models.SlugField(blank=True, unique=True)
    bname=models.CharField(max_length=100)

    bookowner=models.IntegerField()
    
    category=models.CharField(max_length=100)
    writer=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='bphoto')
    condition=models.CharField(max_length=100)
    actual_price=models.IntegerField(null=True, blank=True)
    selling_price=models.IntegerField(null=True, blank=True)
    publication=models.CharField(max_length=100)
    # available=models.BooleanField(default=True)
    display_selling_price=models.IntegerField(null=True, blank=True)

    status=models.CharField(max_length=100, default='available')
    uploaddate=models.DateField(auto_now_add=True)
    solddate=models.DateField(null=True, blank=True)
    featured=models.BooleanField(default=False)
    buyerid=models.IntegerField(null=True,blank=True)

    donation=models.BooleanField(default=False)


    # discount=models.BooleanField(default=False)
    # discount_percent=models.IntegerField(null=True, blank=True)
    # discounted_selling_price=models.IntegerField(null=True, blank=True)


    def get_absolute_url(self):
        return "home/{slug}/".format(slug=self.slug)

    def __str__(self):
        return self.bname

    def __unicode__(self):
        return self.bname


def book_pre_save_reciever(sender, instance ,*args, **kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)     
pre_save.connect(book_pre_save_reciever,sender=Book)


  



    

