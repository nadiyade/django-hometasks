"""ishop URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from myapp.views import RegisterFormView, home, LoginFormView, LogoutFormView, CreateTovar\
    , TovarListView, TovarUpdateView, CreatePurchase


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('register/', RegisterFormView.as_view(), name='register'),
    path('login/', LoginFormView.as_view(), name='login'),
    path('logout/', LogoutFormView.as_view(), name='logout'),
    path('create/', CreateTovar.as_view(), name='create'),
    path('see/', TovarListView.as_view(), name='see'),
    path('update/<int:pk>/', TovarUpdateView.as_view(), name='update'),
    path('buy/', CreatePurchase.as_view(), name='buy'),
]
