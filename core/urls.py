from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('noticias/', views.noticias, name='noticias'),
    path('contacto/', views.contacto, name='contacto'),
]
