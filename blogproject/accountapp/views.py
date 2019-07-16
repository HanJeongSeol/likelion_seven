from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect,'})
    else:
        return render(request, 'login.html')



def signup(request):
    if request.method == 'POST':                # POST방식으로 전송 된 경우에만 실행하게 된다.
        if request.POST['password1'] == request.POST['password2']:
            # username, password변수에 POST형식으로 받아온 데이터를 담는다., create_user함수로 계정이 생성된다.
            user = User.objects.create_user(
                username=request.POST['username'], password=request.POST['password1'])
            # 로그인을 하는 함수, 즉 회원가입이 끝나자 마자 로그인이 된다.
            auth.login(request, user)
            return redirect('home')
    return render(request, 'signup.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request,'login.html')

