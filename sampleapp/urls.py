from django.urls import path

from . import views

urlpatterns = [
    # ～/httpresponse
    path('httpresponse', views.httpresponse, name='httpresponse'),
    # ～/queryparam?msg=・・・
    path('queryparam', views.queryparam, name='queryparam'),
    # ～/urlpattern/<number>/<text>/
    path('urlpattern/<int:number>/<text>/',
         views.urlpattern, name='urlpattern'),
    # ～/template
    path('template', views.template, name='template')
]
