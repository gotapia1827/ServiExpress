from django.contrib import admin
from django.urls import path
from django import views
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('index_master', views.index_master, name="index_master"),
    path('agregar', views.agregar, name="agregar"),    
    path('eliminar/<int:idUsuario>', views.eliminar, name="eliminar"),
    path('listar', views.listar, name="listar"),
    path('actualizar/<int:idUsuario>', views.actualizar, name="actualizar"),
    path('signup', views.signup, name="signup"),
    path('signout', views.signout, name="signout"),
    path('signin', views.signin, name="signin"),
    path('agenda', views.agenda, name="agenda"),
    path('ingreso', views.ingreso, name="ingreso"),
    path('solicitud', views.solicitud, name="solicitud"),
    path('asignar/<int:idSolicitud>', views.asignar, name="asignar"),
    path('eliminaragenda/<int:idSolicitud>', views.eliminaragenda, name="eliminaragenda"),
]