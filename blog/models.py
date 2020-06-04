from django.db import models

# Create your models here.
class Blog(models.Model):#models.Model to inherit and name of class can be anything
    title=models.CharField(max_length=200)
    description=models.TextField()
    date=models.DateField()

    def __str__(self):
    
        return self.title
