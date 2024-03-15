from django.contrib import admin
from .models import Category, Option
import cloudinary
from cloudinary.models import CloudinaryField


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_displsy = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}