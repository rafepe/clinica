from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView
from django.contrib.auth import views as auth_views

from . import views


favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    path('', views.index, name='index'),
    path('favicon.ico', favicon_view),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path("paciente_create/", views.paciente_create.as_view(), name='paciente_create'),
    path('paciente_menu/', views.paciente_menu.as_view(), name='paciente_menu'),
    path("paciente_update/<int:pk>/", views.paciente_update.as_view(), name='paciente_update'),
    path('paciente_delete/<int:pk>/', views.paciente_delete.as_view(), name='paciente_delete'),

    path('funcionario_menu/', views.funcionario_menu.as_view(), name='funcionario_menu'),
    path("funcionario_create/", views.funcionario_create.as_view(), name='funcionario_create'),
    path("funcionario_list/", views.funcionario_list.as_view(), name='funcionario_list'),
    path("funcionario_update/<int:pk>/", views.funcionario_update.as_view(), name='funcionario_update'),
    path('funcionario_delete/<int:pk>/', views.funcionario_delete.as_view(), name='funcionario_delete'),

    path("medico_create/", views.medico_create.as_view(), name='medico_create'),
    path('medico_menu/', views.medico_menu.as_view(), name='medico_menu'),
    path("medico_update/<int:pk>/", views.medico_update.as_view(), name='medico_update'),
    path('medico_delete/<int:pk>/', views.medico_delete.as_view(), name='medico_delete'),

    path("procedimento_create/", views.procedimento_create.as_view(), name='procedimento_create'),
    path('procedimento_menu/', views.procedimento_menu.as_view(), name='procedimento_menu'),
    path("procedimento_update/<int:pk>/", views.procedimento_update.as_view(), name='procedimento_update'),
    path('procedimento_delete/<int:pk>/', views.procedimento_delete.as_view(), name='procedimento_delete'),
     
    path("procedimento_executado_create/", views.procedimento_executado_create.as_view(), name='procedimento_executado_create'),
    path('procedimento_executado_menu/', views.procedimento_executado_menu.as_view(), name='procedimento_executado_menu'),
    path("procedimento_executado_update/<int:pk>/", views.procedimento_executado_update.as_view(), name='procedimento_executado_update'),
    path('procedimento_executado_delete/<int:pk>/', views.procedimento_executado_delete.as_view(), name='procedimento_executado_delete'),
     
    path('orm_sql/', views.orm_sql, name='orm_sql'),

    path('exportar', views.exportar, name='exportar'),

]