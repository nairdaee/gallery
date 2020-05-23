from . import views
from django.conf.urls import url


app_name = 'photos'

urlpatterns = [
    url(r'^$',views.photo_list,name="list"),
    url(r'^(?P<slug>[\w-]+)/$',views.photo_detail, name="detail"),
]