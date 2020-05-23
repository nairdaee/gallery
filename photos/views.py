from django.shortcuts import render,redirect
from .models import Photos
from django.http import HttpResponse
from . import forms
from django.contrib.auth.decorators import login_required

def photo_list(request):
    photos = Photos.objects.all().order_by('date')
    return render(request,'photos/photos_list.html', {'photos': photos})

def photo_detail(request,slug):
   photos = Photos.objects.get(slug=slug)
   return render(request,"photos/photos_detail.html",{'photo':photo})

@login_required (login_url="/accounts/login/") #protects the view till user logs in
def photo_create(request):
    if request.method =='POST':
        form = forms.CreatePhoto(request.POST, request.FILES)  #get's data and validates it
        if form.is_valid():
            #save article to db
            instance = form.save(commit=False)
            instance.owner = request.user  #attaches the aut
            instance.save()  #commits to saving
            return redirect('photos:list')
    else:
        form = forms.CreatePhoto()
    return render(request,"photos/photos_create.html",{'form':form})