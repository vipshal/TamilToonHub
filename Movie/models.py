from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, unique=True)
    slug = models.SlugField(unique=True)
    class Meta:
        ordering = ('-name',)

    def __str__(self):
        return self.name
    
        
class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    movie = models.FileField(upload_to="video/")
    poster = models.FileField(upload_to="poster/",blank=True)
    image = models.FileField(upload_to="FrontImage/",blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE , default=True)
    
    def __str__(self):
        return self.title