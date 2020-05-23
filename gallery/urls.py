from django.conf.urls import url,include
from django.contrib import admin
from . import views
from photos import views as photo_views #differentiates the two
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^about/$',views.about),
    url(r'^photos/',include('photos.urls')),
    url(r'^$',photo_views.photo_list,name= "home" ),
]
