from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('login/',views.loginpage,name="loginpage"),
path('register/',views.registeruser,name="registerpage"),
    path('logout/',views.logoutuser,name="logout"),
    path('completed/<int:pk>',views.completed,name='completed'),
    path('incomplete/<int:pk>',views.incomplete,name='incomplete'),
    path('delete/<int:pk>',views.deletetask,name='delete'),
    path('addtask',views.addtask,name="addtask"),
    path('update/<int:pk>',views.updatetask,name="updatetask"),
]
