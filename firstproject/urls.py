"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from pages.views import home_views, about_views, content_views
from products.views import product_detail_view, product_create_view, product_search_view

urlpatterns = [
    path('', home_views, name='home'),
    path('home/', home_views, name='home'),
    path('about/', about_views),
    path('content/', content_views),
    path('product/', product_detail_view),
    path('create/', product_create_view),
    path('search/', product_search_view),
    path('admin/', admin.site.urls),
]
