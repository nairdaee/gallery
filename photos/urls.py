from . import views
from django.conf.urls import url


app_name = 'photos'

urlpatterns = [
    url(r'^$',views.photo_list,name="list"),
    url(r"^create/$",views.photo_create,name="create"),
    url(r'^(?P<slug>[\w-]+)',views.photo_detail, name="detail"),     ##(?P<slug>[\w-]+)
    url(r'^search/',views.search_photos,name='search_photos'),
    url(r'^location/(\d+)',views.filter_location,name='located_images'),
]