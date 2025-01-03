from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('film', include('film.urls')),
    path('user', include('user.urls'))
]