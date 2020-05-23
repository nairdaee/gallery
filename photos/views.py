from django.shortcuts import render,redirect
from .models import Photos
from django.http import HttpResponse

def photo_list(request):
    photos = Photos.objects.all().order_by('date')
    return render(request,'photos/photos_list.html', {'photos': photos})

def photo_detail(request,slug):
   photos = Photos.objects.get(slug=slug)
   return render(request,"photos/photos_detail.html",{'photo':photo})
