from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
# Create your views here.

def index(request):
    # return HttpResponse('你好!')
    return render(request,"base.html")

def months(request, month):
   
    month_list = []
    try:
        month = int(month)
        for m in range (1,13):
            month_list.append(f'现在是今年的{m}月')
        return HttpResponse(month_list[month-1])
    except:
        return HttpResponse('你再写字')

def detail(request, name):
    users = [{'name': 'hooni', 'email': 'hooni@naver.com', 'hobby': 'running'}, 
            {'name': 'mina', 'email': 'mina@naver.com', 'hobby': 'dance'}, 
            {'name': 'yami', 'email': 'yami@naver.com', 'hobby': 'reading'}, 
            {'name': 'cool', 'email': 'cool@naver.com', 'hobby': 'surfing'}, 
            {'name': 'jack', 'email': 'jack@naver.com', 'hobby': 'golf'}]
    result=""
    for user in users:
        if user["name"] == name:
            # result += f"<h1>{user['name']}</h1><h2>{user['email']}</h2><h3>{user['hobby']}</h3>"
            a_user = user
        break    
    
    if a_user == None:
        return HttpResponseNotFound('유저를 찾을 수 없습니다.')
    return render(request,'landing/users.html', a_user)

def index(request):
    context = {
        "weather_data": {
        "weather":"아주 맑음",
        "temperature": "17도",
        }, "members":[]
    }

    return render(request,"index.html",context)