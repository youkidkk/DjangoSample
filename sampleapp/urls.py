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
    path('template', views.template, name='template'),
    # ～/link
    path('link', views.link, name='link'),
    # ～/static
    path('static', views.static, name='static'),
    # ～/basicform
    path('basicform', views.basicform, name='basicform'),
    path('basicformsubmit', views.basicformsubmit, name='basicformsubmit'),
    # ～/form
    path('form', views.form, name='form'),
    # ～/list
    path('list', views.list, name='list'),
    # ～/create
    path('create', views.create, name='create'),
    # ～/update/<id>
    path('update/<int:id>', views.update, name='update'),
    # ～/delete/<id>
    path('delete/<int:id>', views.delete, name='delete'),
    # ～/listpaging
    path('listpaging', views.listpaging, name='listpaging'),
    path('listpaging/<int:page>', views.listpaging, name='listpaging'),
]
