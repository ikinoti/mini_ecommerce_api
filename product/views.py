from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from .models import Category, Brand, Product
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer


@extend_schema(responses=CategorySerializer)
class CategoryViewSet(viewsets.ViewSet):
    '''
    A simple Viewset for viewing all categories
    '''

    queryset = Category.objects.all()

    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


@extend_schema(responses=BrandSerializer)
class BrandViewSet(viewsets.ViewSet):
    '''
    A simple Viewset for viewing all brand
    '''

    queryset = Brand.objects.all()

    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)\
        
@extend_schema(responses=ProductSerializer)
class ProductViewSet(viewsets.ViewSet):
    '''
    A simple Viewset for viewing all Product
    '''

    queryset = Product.objects.all()

    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)