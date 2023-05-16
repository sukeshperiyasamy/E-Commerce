from django.db import models
from django.contrib.auth.models import User
import datetime
import os


# For Uploading the Image with Filename like(Ex:Iphone11//2023y//04m//12d//10h//02m//22s)
def GetFileName(request,filename): #Function to create an filename with date for non-duplication images names
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")#it converts an date format into the string format
    new_filename="%s%s"%(now_time,filename)#To Concatenate with file name and Date time
    return os.path.join('uploads/',new_filename)#It send an Request to the Upload folder


class Catagory(models.Model):
    # In Catagory fileds that are consiter to the Primary Key defaultly
    fname=models.CharField(max_length=150,null=False,blank=False)#It covers an length of max 150 char and compolsaryly user enter the name and aslo the should not leave as blank 
    image=models.ImageField(upload_to=GetFileName,null=True,blank=True)#It concatenates the images with the Filename while uploading the images  
    desc=models.CharField(max_length=450,null=False,blank=False)#Asusual like name field
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")#Status for the file is tells about the like check boxes if it ticks means it will hide and not tick means it will be shown 
    created_at=models.DateTimeField(auto_now_add=True)#it will shown a timeuploading  of  picture
    # trending=models.BooleanField(default=False,help_text="0-default,1-Trending")#It is also similar to status it tick means default and not tick means shows an trending products

    def __str__(self):
        # print(self.fname)
        return self.fname
    # Its an Another class 
class Products(models.Model):
    catagory=models.ForeignKey(Catagory,on_delete=models.CASCADE) #To creating the Foreign key for that primary key and CASCATE is mainly used for the if we delete the id or any value in primary key field it will automatically delete in foreign key field
    fname=models.CharField(max_length=150,null=False,blank=False)
    vendor=models.CharField(max_length=150,null=False,blank=False)#It will shows an vendor name of the product
    product_image=models.ImageField(upload_to=GetFileName,null=True,blank=True)
    quantity=models.IntegerField(null=False,blank=False)
    original_price=models.IntegerField(null=False,blank=False)
    selling_price=models.IntegerField(null=False,blank=False)
    desc=models.CharField(max_length=450,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
    trending=models.BooleanField(default=False,help_text="0-default,1-Trending")#It is also similar to status it tick means default and not tick means shows an trending products
    created_at=models.DateTimeField(auto_now_add=True)#it will shown a timeuploading of products
 
    def __str__(self):
        return self.fname
    

class Cart(models.Model):#Inheriting the models from Model
    user=models.ForeignKey(User,on_delete=models.CASCADE)#Create an variable user passing usermodel as an parameter then ondelete command is to delete that  user in both table
    product=models.ForeignKey(Products,on_delete=models.CASCADE)#Crate an variable product and passing product class as an parameter  them similar to above
    product_qty=models.IntegerField(null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)#it will shown a timeuploading of Cart quantity

    @property
    def total_cost(self):
        return self.product_qty *self.product.selling_price

class Favourite(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)#Create an variable user passing usermodel as an parameter then ondelete command is to delete that  user in both table
    product=models.ForeignKey(Products,on_delete=models.CASCADE)#Crate an variable product and passing product class as an parameter  them similar to above
    created_at=models.DateTimeField(auto_now_add=True)#it will shown a timeuploading of Cart quantity

