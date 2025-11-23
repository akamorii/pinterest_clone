from django.contrib import admin
from .models import Category, Picture

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    
@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'path', 'description', 'created', ]
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['name', 'created', 'category']
