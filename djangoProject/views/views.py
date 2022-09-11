from django.http import HttpResponse

from django.shortcuts import render

def Hello(request):

    return HttpResponse('Hello world')

def index(request):
    context = {}
    context['name']= 'kpeng'
    return render(request, 'index.html', context)