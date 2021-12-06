from django.db import models
from django.utils.text import slugify

class prodCategory(models.Model):
    name = models.CharField(max_length=20)
    slug= models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def title_slug(self):
        return slugify(self.name)


# Create your models here.
