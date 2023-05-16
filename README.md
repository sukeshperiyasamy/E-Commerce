# Django-Ecommerce
Creating an E-Commerce with the tools of Python and Django with My-sql

==========================================================================================================
1.To check the python version(python --v)
2.Create the Virtual Environment(pip install pipenv)
{
	my files in : Virtualenv location: C:\Users\ADMIN\.virtualenvs\Django-XWvVScuO
}
3.To activate the Virtual environment (pipenv shell)=>It Created and it tells the exact location of Virtual environment
4.To check the current Virtual environment location (pipenv --venv) of path
5.To start the project (django-admin startproject Firstproject)==>It will create the Project
6.view->Command Palette->Interpreter => In that select Virtual env file 
7.To Start the Server (python manage.py runserver)
8.Then we need to connect the my-sql 
ne to change som commands in settings.py like{
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',//Default
        'NAME': 'djangokavin',//Database name
        'HOST':'localhost',//Localhost is default
        'USER':'root',//Root is also default
        'PASSWORD':'1421@Kavin',//Password depend upon the user 
        'PORT':'3306',//Port is also the default
    }
}
}
after that so  much work has been done!!!!!!!in the ==>'''Settings.py'''
9.Then create an seperate urls.py to that particular app
10.In views.py ==>
	command is=>def home(request):
			return render(request,'shop/index.html')
11.In Current App having urls.py=>
    from django.urls import path
    from .import views
    urlpatterns = [
	command is=>path('home/',views.home)
		]===>Then Start the Server

then we can proceed same way that similae on this projects 
12.To extends the parent file we can be use those files like
it should be in parent file==>
   {%block content%}
	-------
   {%endblock content%}

//It is similar to the contents we extends like files script is for js files!
    {%block scripts%}
	---------
    {%endblock scripts%}

it should be in child files==>
	{%extends 'shop/layout/main.html'%}
	<!-- Its an Main Content of Inherting the Parent File -->
	{%block content%}
	<!-- block is keyword and the content userdefined word-->
	<h1>registerd ra balu</h1>
	<!-- endblock is an keyword and the content is userdefined word -->
	{%endblock content%}
13.Then it is similar to the include funn but we add that in parent file
		   {%include 'shop/inc/navbar.html'%}
14.Then we can load the nav bar in the new folder and also used in the rest of the folder 
15.Then we create the models like thses format in given below

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
    created_at=models.DateTimeField(auto_now_add=True)#it will shown a tiuploadingme of  picture
    # trending=models.BooleanField(default=False,help_text="0-default,1-Trending")#It is also similar to status it tick means default and not tick means shows an trending products


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
    created_at=models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.name


16.Then ==>'python manage.py makemigrations'
it will shows like
===================
Migrations for 'shop':
  shop\migrations\0001_initial.py
    - Create model Catagory
    - Create model Products
    Then give=>'python manage.py migrate' --> it will create an table automatically

17.Then create an Super User==>
 
            ===>("python  manage.py createsuperuser")
Username (leave blank to use 'admin'): Kavin
Email address: kkavinkumar24@gmail.com
Password: 1421@Kavin
Password (again):  1421@Kavin
Superuser created successfully.

18.Then we will podcast the classes in admin page like==>
from .models import * #it will import all the classes from models.py

# class Categoryadmin(admin.ModelAdmin):
#     list_display = ('fname','image','desc')
# admin.site.register(Catagory,Categoryadmin)

class Categoryadmin(admin.ModelAdmin):#it will inherits an Admin module from admin
    list_display = ('fname',) #list_display is an keyword to display in front of the admin page
admin.site.register(Catagory,Categoryadmin)#it will send the Category class with the Catagoryadmin to the admin page
admin.site.register(Products)#it will returns asusuall like before

19.And also we can change the theme of the admin-page
            ==> pip install django-jazzmin
            then add'jazzmin' to the settings.py in installed apps
            then restart the server to makes the changes of themes in django-admin

20.Then add images means to write an command in settings.py like 
        ==> STATICFILES_DIRS=[
          BASE_DIR/'static'
            ]                       then only we will add an images to the our html pages


