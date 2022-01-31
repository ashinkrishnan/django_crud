from turtle import title
from django.db import models

# Create your models here.
class blogs(models.Model):
    name = models.CharField(max_length=50)
    title=models.CharField(max_length=250)
    content=models.TextField()

    def __str__(self) :
        return self.name,self.title

