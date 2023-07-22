from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=20)
    desc=models.TextField(max_length=100)
    val=models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Product(models.Model):
    pname=models.CharField(max_length=20)
    cost=models.IntegerField()
    pdesc=models.TextField(max_length=100)
    key=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.pname