# - coding:utf-8 - #
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.http import HttpResponse

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    if 'st' in request.GET:
        if request.GET['st']=='TsinghuaUniversity':
            t = get_template('template.html')
            html = t.render(Context({'school_name':'Tsinhua University','school_chinese_name':'清华大学','birth':'1909','headmaster':'邱勇'}))
            return HttpResponse(html)
        elif request.GET['st']=='PekingUniversity':
            t = get_template('template.html')
            html = t.render(Context({'school_name':'Peking University','school_chinese_name':'北京大学','birth':'1898','headmaster':'林建华'}))
            return HttpResponse(html)
        else:
            return render_to_response('error.html')
    else:
        return render_to_response('error.html')
