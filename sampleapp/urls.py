from django.urls import path

from . import views

urlpatterns = [
    path('httpresponse', views.httpresponse, name='httpresponse'),
]
