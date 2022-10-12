from distutils.command.upload import upload
from enum import unique
from hashlib import blake2b
from operator import mod
from tabnanny import verbose
from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=50,unique=True)
    slug=models.SlugField(max_length=50, unique=True)
    description=models.CharField(max_length=100,blank=True)
    cat_image=models.ImageField(upload_to='photos/categories',blank=True)

    class Meta:
        verbose_name='category'
        verbose_name_plural='categories'


    def __str__(self):
        return self.category_name
        