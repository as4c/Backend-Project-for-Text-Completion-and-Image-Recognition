
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
from .models import TextContent, ImageContent
from .serializers import TextContentSerializer, ImageContentSerializer
import openai
import cv2
from collections import Counter
import numpy as np
import keras_ocr
from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework.parsers import MultiPartParser, FormParser



class ProductDescriptionAPIView(APIView):
   
    api_key = settings.API_KEY

    def post(self, request):
        product_title = request.data.get('product_title', '')

        if not product_title:
            return Response({
                'error': 'Missing product title in request body.'
            }, status=status.HTTP_400_BAD_REQUEST)

        description = self.generate_product_description(product_title)
        # print("description: ", description)
        keywords = self.extract_keywords(description)
        # print("keywords: ", keywords)
        description_obj = TextContent.objects.create(
            product_title=product_title,
            description=description,
            keywords=keywords,
        )

        serializer = TextContentSerializer(description_obj)
        return Response(serializer.data)

    def generate_product_description(self, product_title):
        openai.api_key = self.api_key

        prompt = f"Generate a detailed description for a product with the title: {product_title}"
        response = openai.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=256,
            temperature=0.7,
            n=1,
            stop=None,
        )
        # print("description response: ", response)
        return response.choices[0].text.strip()

    def extract_keywords(self, description):
        openai.api_key = self.api_key

        prompt = f"Extract keywords from the following description: {description}"
        response = openai.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=64,
            temperature=0.7,
            n=1,
            stop=None,
        )
        # print("keywords response: ", response)
        keywords = response.choices[0].text.strip().split()
        return keywords


class ImageContentView(APIView):
    """
    API endpoint for uploading images and extracting keywords.
    """
   
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        print(request.data)
        if 'image' not in request.data:
            return Response({"error": "No image file submitted."}, status=status.HTTP_400_BAD_REQUEST)

        image = request.data['image']
        keywords = self.extract_keywords(image)
        # print("Keywords extracted...")
        # print(keywords)
        # serializer = ImageContentSerializer(data={'image': request.data['image']})
        # serializer.is_valid(raise_exception=True)
        # serializer.save()

        return Response({"keywords": keywords})

    def extract_keywords(self, image):
        # Read the image using OpenCV
        if isinstance(image, InMemoryUploadedFile):
            content = image.read()
        else:
            with open(image.image.path, 'rb') as image_file:
                content = image_file.read()

        img = cv2.imdecode(np.frombuffer(content, np.uint8), cv2.IMREAD_COLOR)

        # Extract text using Keras-OCR
        pipeline = keras_ocr.pipeline.Pipeline()
        prediction = pipeline.recognize([img])[0]
        # print(prediction)
        # extracted_text = prediction.get_text()
        extracted_text = [text for text, _ in prediction]

        # Combine extracted text and skip object detection (as it uses YOLOv3)
        combined_text = " ".join(extracted_text)

        # Tokenize and filter
        filtered_tokens = [token.lower() for token in combined_text.split() if token.isalnum()]

        # Count and return the top keywords
        keywords = Counter(filtered_tokens).most_common(10)
        return [keyword for keyword, _ in keywords]

    