from django.db import models

# Create your models here.
class Todo(models.Model):
    num=models.IntegerField()
    name=models.CharField(max_length=20)
    desc=models.TextField()
    
    def __str__(self):
        return self.name 
