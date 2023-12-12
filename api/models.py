from django.db import models

# Create your models here.
 
class TextContent(models.Model):
    id = models.AutoField(primary_key=True)
    product_title = models.CharField(max_length=500)
    description = models.TextField()
    keywords = models.TextField()

class ImageContent(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='images')
    