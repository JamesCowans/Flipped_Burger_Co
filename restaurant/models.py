from django.db import models
from django.urls import reverse
from cloudinary.models import CloudinaryField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    
    
    
    def get_absolute_url(self):
        return reverse('restaurant:option_list_by_category', args=[self.slug])
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        indexes = [ models.Index(fields=['name']),
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'



    

class Option(models.Model):
    category = models.ForeignKey(Category, related_name='options', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = CloudinaryField('image', default='static/img/awaiting_image.png')
    description = models.TextField(blank=True)
    alt_tag = CloudinaryField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('restaurant:option_detail', args=[self.id, self.slug])

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]

    

            
