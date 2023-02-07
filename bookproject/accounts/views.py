from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    #POST : 로그인 시키기
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
        else:
            return render(request, 'bad_login.html')
    #GET : login.html 띄우기
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def signup(request):
    if request.method=="POST":
        if request.POST['password'] == request.POST['repeat']:
            #회원가입
            new_user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            #로그인
            auth.login(request, new_user, backend='django.contrib.auth.backends.ModelBackend')
            #홈 리다이렉션
            return redirect('home')
    return render(request, 'register.html')