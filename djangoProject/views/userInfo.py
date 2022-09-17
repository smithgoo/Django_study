import json
from django.http import  HttpResponse,JsonResponse
from django.core import  serializers
from django.shortcuts import render
from django.template.context_processors import csrf

from djangoProject.views.TJsonResponse import resultT
from userInfo.models import user

# phone = models.CharField(max_length=10)
# pwd = models.CharField(max_length=20)
# email = models.CharField(max_length=100)
# age = models.IntegerField(default=18)
# sex = models.IntegerField(default=0)  # 0未知 1男 2女
# tips = models.CharField(max_length=120)
# coins = models.IntegerField(default=0)
# avator = models.CharField(max_length=300)
def  register(request):
    phone = request.GET.get('phone','')
    pwd = request.GET.get('pwd','')
    email = request.GET.get('email','')
    age = request.GET.get('age','')
    tips = request.GET.get('tips','')
    avator = request.GET.get('avator','')
    print(phone,pwd,email,age,tips,avator)
    tmpUser = user(phone=phone, pwd=pwd, email=email, age=age, tips=tips, avator=avator)
    tmpUser.save()
    return resultT('200', '注册成功，请重新登录')
    # list = user.objects.all()
    # for x in list:
    #     if x.phone == phone:
    #         return resultT('6001','你注册的手机号已存在,请重新输入')
    #         break
    #     else:
    #        tmpUser = user(phone=phone,pwd =pwd,email=email,age=age,tips=tips,avator=avator)
    #        tmpUser.save()
    #        return resultT('200','注册成功，请重新登录')
    #        break
    #
    # pass

def login(request):
    return render(request,'login.html')
