from django.contrib import admin
from django.urls import path
import blogapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blogapp.views.home,name='home'),
    # url접속을 위해서는 주소 마지막에 'blog/객체번호'로 들어와야한다
    path('blog/<int:blog_id>',blogapp.views.detail, name='detail'),     # 사용자가 들어올 때 가장먼저 url을 통해 들어오기 때문에 url설정 먼저 설정.

]