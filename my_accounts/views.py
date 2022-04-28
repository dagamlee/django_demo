from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def sign_up(request):
    # 요청이 포스트인지 확인
    context = {}
    if request.method == 'POST':
    #요청받은 request에서 username이 존재하는 지
        username = request.POST.get('username')
    #요청받은 request에서 password가 존재하는 지
        password = request.POST.get('password')
    #요청받은 request에서 username와 password_check가 같은지
        password_check = request.POST.get('password_check')
            #회원가입 ok
        if (username and password and password == password_check):
            try:
                new_user = User.objects.create_user(username=username, password=password)
                #새로운 유저 아이디로 로그인
                auth.login(request, new_user)
                #블로그 홈으로 리다이렉트 시켜주기
    # 에러메세지 context에 담기   
                return redirect ('blog_samples:home')
            except:
                context['error'] = '이미 존재하는 아이디 입니다.'  
        else:
            context['error'] = '아이디와 비밀번호를 잘 못 입력하셨습니다..'      
    return render(request, 'my_accounts/sign_up.html', context) 

def login(request):
    if request.user.is_authenticated:
        return redirect('blog_samples:home')
    context={}
    if request.method == 'POST':
        username = request.POST.get('username')
    if request.method == 'POST':
        password = request.POST.get('password')    
        if (username and password):
            user = auth.authenticate(request, 
                                 username=username, 
                                 password=password)    
            if user:
                auth.login(request,user)
                return redirect('blog_samples:home')    
            
            else:
                context['error'] = '아이디랑 비밀번호가 틀렸습니다.'
        else:
            context['error'] = '아이디랑 비밀번호를 입력해 주세요.'           
    return render (request,'my_accounts/login.html')

def logout(request):
    # if request.method == 'POST':
    auth.logout(request)
    return redirect('blog_samples:home')

def naver_test(request):
    return render(request,'my_accounts/naver_test.html')

     