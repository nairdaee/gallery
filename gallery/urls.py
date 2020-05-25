from django.conf.urls import url,include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from photos import views as photo_views #differentiates the two
from django.conf.urls import handler404,handler500

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^about/$',views.about),
    url(r'^accounts/',include('accounts.urls')),
    url(r'^photos/',include('photos.urls')),
    url(r'^$',photo_views.photo_list,name= "home" ),
]
handler500 = photo_views.error_500
handler404 = photo_views.error_404

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)