from django.contrib import admin
from django.urls import path, include
from myapp.views import index, new, final, verynew

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('new/', new, name='new'),
    path('final/', final, name='final'),
    path('verynew/', verynew, name='verynew'),
]
