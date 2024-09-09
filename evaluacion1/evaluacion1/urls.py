from django.contrib import admin
from django.urls import path
from mis_notas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('notas/', views.notas, name='notas'),
    path('confirmacion_eliminacion/', views.eliminar, name='eliminar'),
    path('confirmacion_creacion/', views.crear, name='crear'),
]
