from os import name
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from . import views as admin_views


urlpatterns = [
    path('admin_dashboard',admin_views.admin_dashboard,name='admin_dashboard'),
    path('add_post',admin_views.add_post,name='add_post')
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)