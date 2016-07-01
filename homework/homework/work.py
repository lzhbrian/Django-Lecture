from django.http import HttpResponse
from django.shortcuts import render_to_response
class me:
    name='chenjiayu'
    sex='male'
    height='175cm'
    
class girl:
    name='girl'
    sex='female'
    height='170cm'
    
a=me()
b=girl()

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    if request.GET['q']=='chenjiayu':
        message=a.name+' '+a.sex+' '+a.height
    elif request.GET['q']=='girl':
        message=b.name+' '+b.sex+' '+b.height
    else:
        message='You should input chenjiayu or girl to get a correct response'
    return HttpResponse(message)
    
