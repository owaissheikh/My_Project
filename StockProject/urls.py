from django.contrib import admin
from django.urls import include,path
urlpatterns = [
    path('MyStock/',include('MyStock.urls')),
    path('admin/',admin.site.urls),
]
