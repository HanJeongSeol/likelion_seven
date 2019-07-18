from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import BlogModel

def home(request):
    blogs = BlogModel.objects           # 쿼리셋 가져오기
    # 블로그의 모든 글들을 대상으로
    blog_list = BlogModel.objects.all()
    # 블로그 객체 세 개를 한 페이지로 자르기, Paginator함수 사용
    paginator = Paginator(blog_list,4)
    # ruquest된 페이지가 뭔지를 알아내고(request페이지를 변수에 담아내고)
    # GET방식으로 얻어낸 request중에서 key값이 page인 딕셔너리형의 value값을 page에 담는다.
    page = request.GET.get('page')
    # request된 페이지를 얻어온 뒤 return해준다.
    # request된 페이지에 대한 post가 posts에 담겨진다.
    posts = paginator.get_page(page)
    return render(request,'home.html',{'blogs' : blogs, 'posts':posts})

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
