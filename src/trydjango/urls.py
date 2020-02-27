"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin

from pages.views import home_view, contact_view, about_view
from products.views import product_detail_view, product_create_view, render_initial_data, dynamic_lookup_view

urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name='about'),
    path('product/', product_detail_view, name='product'),
    path('products/<int:id>/', dynamic_lookup_view, name='product'),
    path('create/', product_create_view, name='create'),
    path('initial/', render_initial_data, name='initial'),
    path('admin/', admin.site.urls),
]
