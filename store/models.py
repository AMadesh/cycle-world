from django.db import models

import datetime
from itertools import cycle
from django.contrib.auth.models import User



import os



# Create your models here.




    

    

class contacted(models.Model):
    select_choice=(('Enquiry','ENQUIRY'),('Services','SERVICES'),('Quality Base','QUALITY BASE'))
    Name=models.CharField(max_length=150,default='')
    Mail=models.CharField(max_length=150,default='')
    Select=models.CharField(max_length=20,choices = select_choice,default='1')
    Contact=models.IntegerField(default='')
    Message=models.CharField(max_length=150,default='')

class buy(models.Model):
    Sku=models.IntegerField(blank=False,null=False,default=None)
    Name=models.CharField(max_length=150)
    Number=models.IntegerField(blank=True,null=True,default=None)
    Door=models.CharField(max_length=150)
    Address=models.CharField(max_length=150)
    City=models.CharField(max_length=150)
    


def getFileName(request,filename):
  now_time=datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
  new_filename="%s%s"%(now_time,filename)
  return os.path.join('upload/',new_filename)


class cycles(models.Model):
    name=models.CharField(max_length=150,null=False,blank=False)
    quantity=models.IntegerField(null=False,blank=False)
    show=models.CharField(max_length=20,null=False,blank=False)
    product_image=models.ImageField(upload_to=getFileName,null=True,blank=True)  
    sku=models.IntegerField(null=False,blank=False)
    chase=models.CharField(max_length=150,default='')
    original_price=models.FloatField(null=False,blank=False)
    selling_price=models.FloatField(null=False,blank=False)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")




    def __str__(self):
        return self.name
    

class Cart(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  product=models.ForeignKey(cycles,on_delete=models.CASCADE)
  product_qty=models.IntegerField(null=False,blank=False)
  created_at=models.DateTimeField(auto_now_add=True)

  @property
  def total_cost(self):
    return self.product_qty*self.product.selling_price
