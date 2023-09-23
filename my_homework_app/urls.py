from django.urls import path
from . import views

urlpatterns = [
    path('1/', views.first_app, name='first_app'),
    path('about/', views.about_me, name='about_me'),
]
