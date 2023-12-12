from django.contrib import admin
from .models import TextContent, ImageContent
# Register your models here.

admin.site.register([TextContent, ImageContent])
