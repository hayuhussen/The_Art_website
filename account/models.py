
from django.db import models

class Banner(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    
    background_image = models.ImageField(upload_to='banner_images/')

    def __str__(self):
        return self.title

# models.py
from django.db import models

class NFTItem(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='nft_images/')
    author_name = models.CharField(max_length=100)
    author_image = models.ImageField(upload_to='author_images/')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title
class Category(models.Model):
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255, blank=True, null=True)  # for storing icon HTML if needed
    image = models.ImageField(upload_to='icon/')

    def __str__(self):
        return self.name
    

class AboutSectionItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='about_section_images/')

    def __str__(self):
        return self.title    