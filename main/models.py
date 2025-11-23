from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
    
    def __str__(self):
        return self.name

"""
path
name
description
category
"""
    
class Picture(models.Model):
    category = models.ForeignKey(Category,related_name='picture',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    path = models.CharField(max_length=200,unique=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class meta():
        ordering = ('name',)

    def __str__(self):
        return self.name
        
