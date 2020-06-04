from django.db import models

# Create your models here.
class Project(models.Model):#models.Model to inherit and name of class can be anything
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    image=models.ImageField(upload_to='portfolio/images/')
    url=models.URLField(blank=True)#blank = true specifies we can unassign(if not allow to contain url) its value too

#user created 
#python manage.py changepassword username
    def __str__(self):
        return self.title
