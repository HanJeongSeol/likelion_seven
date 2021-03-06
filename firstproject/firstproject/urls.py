"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import wordcount.views          # 생성한 app의 views.py를 import하여 url설정을 할 수 있도록 한다.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', wordcount.views.home,name='home'),             # url의 마지막이 공백인 경우 home.html로 이동한다. 이 때 이름을 home으로 명시하여 다른 곳에서도 home으로 사용할 수 있다.
    path('about/', wordcount.views.about,name='about'),     # url이 about로 끝나는 경우 about.html로 이동한다.
    path('result/', wordcount.views.result,name='result'),
]
