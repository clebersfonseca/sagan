from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lista/', views.objectList, name='list'),
    path('sobre/', views.about, name='about'),
    path('contribue/', views.contribute, name='contribute'),
    path('lista/observacoes', views.returnModal, name='modal'),
    path('lista/observacoes2', views.modal, name='modal2'),
    path('objeto/<int:ticID>/<int:ind>', views.tessObject, name='object'),
    path('objetojson/<int:ticID>/<int:ind>', views.returnJson, name='retornoJ')
]