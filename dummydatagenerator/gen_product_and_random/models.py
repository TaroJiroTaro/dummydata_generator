from django.db import models
from django.core.validators import FileExtensionValidator
from django.shortcuts import render, get_object_or_404

# Create your models here.

class Post(models.Model):
    title = models.CharField(default='json file', max_length=50)
    document = models.FileField(upload_to='uploads/%Y/%m/%d/', validators=[FileExtensionValidator(['json',])])
    uploaded_at = models.DateTimeField(auto_now_add=True)