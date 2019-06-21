from django.contrib import admin
from django.urls import path
from . import views

#app_name = 'ezmanagement'

urlpatterns = [
    path('', views.index, name='index'),
    path('menu_inicial/', views.menu_inicial, name='menu_inicial'),
    path('cadastro_funcionario/', views.cadastro_funcionario, name='cadastro_funcionario'),
    path('cadastro_engenheiro/', views.cadastro_engenheiro, name='cadastro_engenheiro'),
    path('cadastro_representante/', views.cadastro_representante, name='cadastro_representante'),
    path('remocao_funcionario/', views.remocao_funcionario, name='remocao_funcionario'),
    path('alteracao_funcionario/', views.alteracao_funcionario, name='alteracao_funcionario'),
    path('consulta_funcionario/', views.consulta_funcionario, name='consulta_funcionario'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('remocao/', views.remocao, name='remocao'),
    path('alteracao/', views.alteracao, name='alteracao'),
    path('consulta/', views.consulta, name='consulta'),
    path('relatorio/', views.relatorio, name='relatorio')

]
