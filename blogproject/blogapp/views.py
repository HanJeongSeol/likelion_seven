from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import BlogModel

def home(request):
    blogs = BlogModel.objects           # 쿼리셋 가져오기
    return render(request,'home.html',{'blogs' : blogs})

def detail(request, blog_id):
    details =get_object_or_404(BlogModel,pk=blog_id)
    return render(request,'detail.html',{'details':details})

def new(request):
    return render(request,'new.html')

def create(request):                    # 입력받은 데이터를 db에 넣어주는 함수
    blog = BlogModel()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()     # 글을 작성한 시점을 가져온다
    blog.save()                                 # 데이터를 저장한 blog객체를 저장시킨다.
    return redirect('/blog/'+str(blog.id))      # blog.id는 int형이지만 URL에서 작성될때는 문자형이기 떄문에 str함수로 형변환 한다.
    # redirect : 인자값으로 url을 받는다. 따라서 다른 url도 입력이 가능하다.
    # ex> return redirect("https://www.naver.com") -> 모든 함수가 실행되고 네이버로 이동된다.
    # render : views에서 정의한 함수를 사용하여 데이터를 처리하고, 처리한 데이터를 이용하고 싶을 때 사용한다. 
    # 세번째 인자값으로 dictionary형