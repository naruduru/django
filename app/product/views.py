from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from .models import Product
from rest_framework.views import APIView
from .serializers import ProductSerializer

# Create your views here.
class ProductListAPI(APIView):
    def get(self, request):
        queryset = Product.objects.all()
        print(queryset)

        serializers = ProductSerializer(queryset, many=True)

        return Response(serializers.data)
