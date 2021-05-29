from django.db import models
from embed_video.fields import EmbedVideoField


# Create your models here.
class I_SlidingImage(models.Model):
    image=models.ImageField(upload_to="photos/home")
    heading= models.TextField(max_length=200, blank=True)
    description= models.TextField(max_length=200, blank=True)
    button= models.TextField(max_length=200, blank=True)
    button_hyperlink=models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.description

class Ii_Quantity_Title(models.Model):
    quantity=models.IntegerField(blank=True)
    title=models.TextField(max_length=100, blank=True)

    def __str__(self):
        return self.title

class Iii_Application_Areas(models.Model):
    image=models.ImageField(upload_to="photos/home")
    field=models.TextField(max_length=100, blank=True)
    aplication_areas=models.TextField(max_length=100, blank=True)


    def _str_(self):
        return self.field

class Iv_Media_Coverage(models.Model):
    heading=models.TextField(max_length=100)

    def __str__(self):
        return self.heading

class V_Media_Sliding(models.Model):
    logo=models.ImageField(upload_to="photos/home")
    date=models.CharField(max_length=100)
    title=models.TextField(max_length=150)
    know_more=models.TextField(max_length=100, blank=True)
    know_more_hyperlink=models.URLField(max_length = 500,blank=True,null=True)
    #hyperlink

    def __str__(self):
        return self.title

class Vi_Companies_And_People(models.Model):
    reviews=models.TextField(max_length=150,blank=True)
   
    
    def __str__(self):
        return self.reviews

class Vii_Companies_Logos(models.Model):
    logo_name=models.TextField(max_length=150,blank=True)
    logo=models.ImageField(upload_to="photos/home")

    def __str__(self):
        return self.logo_name
