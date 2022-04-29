from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lista/', views.objectList, name='list'),
    path('sobre/', views.about, name='about'),
    path('lista/observacoes', views.modal, name='modal'),
    path('objeto/<int:ticID>/<int:ind>', views.tessObject, name='object'),
    path('objeto/to_periodogram/<int:ticID>/<str:ind>', views.foldLightCurve, name='folded'),
]

urlpatterns += staticfiles_urlpatterns()