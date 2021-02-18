from django.urls import path
from django.urls import re_path
from django.views.static import serve
from . import views

urlpatterns = [
    path('', views.index),
    path('object', views.object),
    path('reset', views.reset),
    re_path(r'^(?P<path>.*)$', serve, {
            'document_root': 'coverage_app/coverage_data/htmlcov',
            }),
]
