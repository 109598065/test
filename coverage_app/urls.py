from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('object', views.object),
    path('reset', views.reset),
]
