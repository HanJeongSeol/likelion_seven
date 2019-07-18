from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:blog_id>',views.detail, name='detail'),
    path('new/',views.new,name='new'),
    path('create/',views.create,name='create'),
    # 직접 만든 form의 url
    path('newblog/',views.blogpost,name='newblog'),
    
]

