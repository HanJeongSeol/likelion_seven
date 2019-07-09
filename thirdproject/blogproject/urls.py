"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import blogapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blogapp.views.home,name='home'),
    # url접속을 위해서는 주소 마지막에 'blog/객체번호'로 들어와야한다
    path('blog/<int:blog_id>',blogapp.views.detail, name='detail'),     # 사용자가 들어올 때 가장먼저 url을 통해 들어오기 때문에 url설정 먼저 설정.

]