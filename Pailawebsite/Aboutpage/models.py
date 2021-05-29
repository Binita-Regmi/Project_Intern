from django.db import models

# Create your models here.
class I_About_Us_Top_Content(models.Model):
    heading=models.TextField(max_length=100)
    description=models.TextField(max_length=100)

    def __str__(self):
        return self.heading

class Ii_Aboutus_Odd_Even_Content(models.Model):
    image=models.ImageField(upload_to='photos/about')
    push_image=models.BooleanField(default=False,null=True)#if true, push image left
    #if false, push image right
    title=models.TextField(max_length=200)
    description=models.TextField(max_length=700)

    def __str__(self):
        return self.title

class Iii_Company_Progress(models.Model):
    title=models.TextField(max_length=200,blank=True)
    progress_percentage=models.IntegerField(null=True,blank=True)
    progress_title=models.TextField(max_length=50)
    description=models.TextField(max_length=150)
    

    def __str__(self):
        return self.description

class Iv_Working_Steps(models.Model):
    heading=models.TextField(max_length=150,blank=True)
    steps_left=models.TextField(max_length=50,null=True)
    description_left=models.TextField(max_length=150,null=True)
    steps_right=models.TextField(max_length=50)
    description_right=models.TextField(max_length=150)
    image=models.ImageField(upload_to='photos/about',blank=True)
    is_available=models.BooleanField()


    def __str__(self):
        return self.steps_right

class V_Team_Box(models.Model):
    profile=models.ImageField(upload_to='photos/about')
    name=models.TextField(max_length=150,blank=True)
    profession=models.TextField(max_length=150,blank=True)
    description=models.TextField(max_length=150,blank=True)
    hyperlink=models.TextField(max_length=500, blank=True,null=True)
   
    def __str__(self):
        return self.name

class Vi_Subscribe_To_Our_Newsletter(models.Model):
    image_name=models.TextField(max_length=100)
    image=models.ImageField(upload_to='photos/about')
    description=models.TextField(max_length=150)

    def __str__(self):
        return self.image_name




