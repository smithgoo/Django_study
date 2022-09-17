import json
from django.http import  HttpResponse,JsonResponse
from django.core import  serializers

def resultT(code,msg,data=''):
    data = {}
    if len(data)>0:
        data = {
            'code':code,
            'msg':msg,
            'data':data,
        }
    else:
        data = {
            'code': code,
            'msg': msg,
        }
    return JsonResponse(data)