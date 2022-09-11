from django.http import HttpResponse
from TestModel.models import Test

def add(request):
    name = request.GET.get('name')
    age = request.GET.get('age')
    test = Test(name=name,age=age)
    test.save()
    return HttpResponse('<p>save success</p>')

def getAll(request):
    list = Test.objects.all()
    response = ''
    for l in list:
        response = l.name+' '+response
    return HttpResponse('<p>'+response+'</p>')

def getInfoById(request):
    id = request.GET.get('id');
    list = Test.objects.get(id = id)

    try:
        return HttpResponse('<p>' + list.name + '</p>')
    except:
        return HttpResponse('<p>' + 'no found' + '</p>')

def updateInfo(request):
    id = request.GET.get('id');
    name = request.GET.get('name');
    list = Test.objects.get(id = id)
    try:
        list.name = name
        list.save()
    except:
        return HttpResponse('<p>' + 'no found' + '</p>')


def deleteInfo(request):
    id = request.GET.get('id')
    list = Test.objects.get(id=id)
    list.delete()
    return HttpResponse('<p>delete success</p>')