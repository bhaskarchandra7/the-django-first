from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('', views.index, name='signup'),
    path("home", views.home, name='index'),
    path("signup", views.signup, name='signup'),
    path("login", views.login, name='login'),
    path('table',views.table, name='table'),
    path('quary',views.quary, name='quary'),
]