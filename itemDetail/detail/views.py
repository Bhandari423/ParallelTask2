from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_200_OK,
    HTTP_404_NOT_FOUND,
    HTTP_400_BAD_REQUEST,
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_401_UNAUTHORIZED,
)
from .models import Item
import time

# Create your views here.
class CreateDetail(APIView):
    def post(self, request):
        itemName = request.POST.get('itemName')
        itemCost = request.POST.get('itemCost')
        itemId = request.POST.get('itemId')
        
        if Item.objects.filter(itemId=itemId).exists():
            return Response({"error": "item already exists"}, status=HTTP_400_BAD_REQUEST)
        else:
            obj = Item.objects.create(
                itemName = itemName,
                itemCost = itemCost,
                itemId = itemId,
            )
            return Response({"message": "Object created"}, status=HTTP_201_CREATED)


    def get(self,request):
        time.sleep(60)
        obj = Item.objects.values()
        if obj:  
            return Response({"obj": obj}, status=HTTP_200_OK)
        else:
            return Response({"error": "Not Found"}, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        obj = Item.objects.filter(itemId=pk)
        if obj:
            obj.delete()
            return Response({"message": "Item Deleted"}, status=HTTP_200_OK)
        else:
            return Response({"error": "Invalid Item ID"}, status=HTTP_400_BAD_REQUEST)
