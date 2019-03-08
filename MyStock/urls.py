"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(r'^getcategory/$' , views.getcategory, name='getcategory'),
    path(r'^getsubcategory/$' , views.getsubcategory, name='getsubcategory'),
    path(r'^getmanufacturer/$' , views.getmanufacturer, name='getmanufacturer'),
    path(r'^getinvoice/$' , views.getinvoice, name='getinvoice'),
    path(r'^category2/$' , views.category2, name='category2'),
    path(r'^subcategory2/$' , views.subcategory2, name='subcategory2'),
    path(r'^Product2/$' , views.Product2, name='Product2'), 
    path(r'^Manufacturer2/$' , views. Manufacturer2, name='Manufacturer2'),
    path(r'^customer2/$' , views.customer2, name='customer2'),
    path(r'^invoice2/$' , views.invoice2, name='invoice2'),
    path(r'^Category1/$' , views.Category1, name='Category1'),
    path(r'^Subcategory1/$' , views.Subcategory1, name='Subcategory1'),
    path(r'^Product1/$' , views.Product1, name='Product1'), 
    path(r'^Manufacturer1/$' , views. Manufacturer1, name='Manufacturer1'),
    path(r'^Customer1/$' , views.Customer1, name='Customer1'),
    path(r'^invoice1/$' , views.invoice1, name='invoice1'),
]
