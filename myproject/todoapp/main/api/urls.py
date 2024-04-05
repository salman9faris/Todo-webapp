from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.getRoutes),
    path('gettasks/',views.gettasks),
    path('gettasks/<int:pk>/',views.gettask),
    path('deletetasks/<int:pk>/',views.deletetask)
]