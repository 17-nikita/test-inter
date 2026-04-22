from django.shortcuts import render
from testing.models import get_filtered_product
from testing.serializer import ProductSerializer, ProductResponseSerializer
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
# Create your views here.
CACHE_TM = 60*5
class Product(APIView):

    def get(self,request):
        query_serializer = ProductSerializer(data=request.query_params)
        query_serializer.is_valid(raise_exception=True)
        validated_data = query_serializer.validated_data 

        cache_key = f"analytics:{validated_data}"
        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data,HTTP_200_OK)
        data = get_filtered_product(validated_data)
        response_data = ProductResponseSerializer(data= data)
        response_data.is_valid(raise_exception=True)
        cache.set(cache_key,response_data.data,CACHE_TM)
        return Response(response_data.data,HTTP_200_OK)
