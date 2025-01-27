from django.db import models
from django.contrib.auth.models import User

import os

# Create your models here.
def student_directory_path(instance, filename):
    # return 'students/{0}/{1}'.format(instance.name, filename)
    # return os.path.join('Student/images', instance.name, filename)
    return os.path.join('images', instance.name, filename)



class Students(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=50)
    photo = models.ImageField(upload_to=student_directory_path)
    checked = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name