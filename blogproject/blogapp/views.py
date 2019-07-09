from django.shortcuts import render, get_object_or_404
from .models import BlogModel

def home(request):
    blogs = BlogModel.objects           # 쿼리셋 가져오기
    return render(request,'home.html',{'blogs' : blogs})

def detail(request, blog_id):
    details =get_object_or_404(BlogModel,pk=blog_id)
    return render(request,'detail.html',{'details':details})
