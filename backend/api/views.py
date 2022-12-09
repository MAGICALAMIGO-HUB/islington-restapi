# from django.shortcuts import render

# # Create your views here.
from django.http import JsonResponse
from rest_framework import viewsets
from .models import Artical
from .serializers import AritcalSerializer
class ArticalViewSet(viewsets.ModelViewSet):
    queryset =Artical.objects.all()
    serializer_class =AritcalSerializer
# def api_home(request, *args, **kwargs):
def api_home(request):
    return JsonResponse({"message":"Hi there, this is your Django API response!!"})
def api_home2(request):
    return JsonResponse({"message":"this is the base url hahahah"}) 