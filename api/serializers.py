from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from api.models import TextContent, ImageContent

class TextContentSerializer(ModelSerializer):

    class Meta:
        model = TextContent
        fields = ( 'product_title', 'description', 'keywords')
 
class ImageContentSerializer(ModelSerializer):
    # image = serializers.ImageField(required = True)
    class Meta:
        model = ImageContent
        fields = ['image']
        
 
