from django.contrib import admin
from django.urls import path
from aplikasi.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('mimil/', mimil, name='mimil'),
    path('coba/', coba, name='coba'),
    path('index1/', index1, name='index1'),
]