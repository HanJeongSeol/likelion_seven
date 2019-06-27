from django.shortcuts import render
from .models import modelapp            # 같은 폴더 안의 models에 있는 modelapp 클래스 import

def home(request) :
    blogs = modelapp.objects            # blogs변수에 modelapp클래스의 객체를 담아준다
    # db에 저장된 데이터를 사용하기 위해 모델로부터 객체를 전달받아야 한다.
    # 이 때 전달받은 객체를 쿼리셋이라고 한다.
    # 쿼리셋을 우리가 원하는대로 하기 위해서 메소드를 활용한다.
    return render(request, 'home.html', {'blogs' : blogs})


    # 쿼리셋과 메소드 형식
    # 모델.쿼리셋(objects).메소드
