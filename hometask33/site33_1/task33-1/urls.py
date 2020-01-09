"""task33-1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from pagelinks.views import index, main_article, unique_article, article, article_sub, article_users\
    , article_archive, article_number, user_number


urlpatterns = [
    path('admin/', admin.site.urls),
    path('1st-url/', include('pagelinks.urls')),
    path('', index, name='index'),
    path('article/', main_article, name='main_article'),
    path('article/33/', unique_article, name='unique_article'),
    path('article/<int:article_id>/', article, name='article'),
    path('article/<int:article_id>/<slug:name>/', article, name='article_name'),
    path('article/archive/', article_archive, name='archive'),
    path('article/archive/<int:artnum>/', article_number, name='article_number'),
    path('article/users/', article_users, name='users'),
    path('article/users/<int:usernum>/', user_number, name='user_number'),
    path('article/<str:subarticle>/', article_sub, name='subarticle'),
]
