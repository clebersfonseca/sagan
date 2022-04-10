from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('painel/', views.dashboardPanel, name='panel'),
    path('lista/', views.objectList, name='list'),
    path('sobre/', views.about, name='about'),
    path('contribue/', views.contribute, name='contribute'),
    path('lista/', views.returnModal, name='modal'),
    path('objeto/<int:ticID>/', views.tessObject, name='object')
]