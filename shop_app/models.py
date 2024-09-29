from django.db import models
import datetime
import os 

def getFileName(request,filename):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename="%S%S"%(now_time,filename)
    return os.path.join('uploads/',new_filename)


class Category(models.Model):
    name=models.CharField(max_length=50,null=False,blank=False)
    description=models.TextField(max_length=500,null=False,blank=False)
    image=models.ImageField(upload_to=getFileName,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=50,null=False,blank=False)
    vender=models.CharField(max_length=50,null=False,blank=False)
    quantity=models.IntegerField(null=False,blank=False)
    old_price=models.FloatField(null=False,blank=False)
    new_price=models.FloatField (null=False,blank=False)
    description=models.TextField(max_length=500,null=False,blank=False)
    seller=models.FloatField (null=False,blank=False)
    product_image=models.ImageField(upload_to=getFileName,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
    trending=models.BooleanField(default=False,help_text="0-default,1-Hidden")
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    


