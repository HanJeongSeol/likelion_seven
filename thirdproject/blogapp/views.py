from django.shortcuts import render, get_object_or_404
from .models import blogapp
# Create your views here.

def home(request) :             # home은 request만 들어오면 실행되는 함수이다. 즉 home.html을 사용자에게 보여주기 위해 가져오라는 요청만 있으면 되기 때문에 하나의 인자로 구성된다.
    blogs = blogapp.objects
    return render(request, 'home.html',{'blog' : blogs})

def detail(request, blog_id):                                    # rquest만으로는 몇 번 객체를 다룰 것인지에 대한 정보가 부족하기 때문에 blog_id라는 인자를 추가로 받는다.
    blog_detail = get_object_or_404(blogapp,pk=blog_id)          # 이용자가 원한 몇 번 블로그 객체, Model의 blogapp클래스를 가져오며, 이 때 pk값은 url에서 넘어온 blog_id값이다. blogapp의 blog_id번째 객체를 불러온다.
    return render(request,'detail.html',{'blog' : blog_detail})