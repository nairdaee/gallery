from django.shortcuts import render,redirect,get_object_or_404
from .models import Photos,Location, Category
from django.http import HttpResponse
from . import forms
from django.contrib.auth.decorators import login_required

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


def search_photos(request):

    if 'photo' in request.GET and request.GET["photo"]:
        search_term = request.GET.get("photo")
        search_photos = Photos.search_by_category(search_term)
        message = f"{search_term}"

        return render(request,'photos/search.html',{"message":message,"photos_searched":search_photos})

    else:
        message = "that...You haven't searched yet"
        return render(request,"photos/search.html",{"message":message})


def filter_location(request,photo_id):
    try:
        location = Location.get_location()
        located_photos = Photos.objects.filter(location=photo_id)
    except DoesNotExist:
        raise Http404()
        return render(request,'photos/photos_detail.html',{"located_photos":located_photos,"locations":location})

def photo_list(request):
    photos = Photos.objects.all().order_by('date')
    return render(request,'photos/photos_list.html', {'photos': photos})

def photo_detail(request,slug):
    photo = Photos.objects.get(slug=slug)  
    photo1 = Photos.objects.filter(slug=slug)
              ##photo = get_object_or_404(Photos, slug=slug)
    return render(request,"photos/photos_detail.html",{'photo':photo},{'photo1':photo1})

def error_404(request):
    return render(request, "photos/error_404.html")

def error_500(request):
    return render(request,"photos/error_500.html")