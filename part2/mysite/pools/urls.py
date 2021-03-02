from django.urls import path

from . import views

urlpatterns = [
    # ex: pools/
    path ('', views.index, name = 'index'),
]