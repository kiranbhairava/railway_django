

# Create your models here.
from django.db import models

class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    sex = models.CharField(max_length=10)
    place = models.TextField(max_length=10)



    def __str__(self):
        return self.name

# class script(models.Model):
#     name = models.CharField(max_length=255)
#     role = models.CharField(max_length=255)
#     sex = models.CharField(max_length=10)

#     def __str__(self):
#         return self.name
    
# class Person(models.Model):
#     name = models.CharField(max_length=255)
#     role = models.CharField(max_length=255)
#     sex = models.CharField(max_length=10)

#     def __str__(self):
#         return self.name