from django.http import HttpResponse,Http404
from django.template.loader import get_template
from django.template import Context
import datetime
from django.shortcuts import render_to_response
class people:
	def __init__(self,dep,hobby):
		self.dep=dep
		self.hobby=hobby
tanghy=people('AUTOMATION',['basketball','pop music','go hiking'])
gaofeng=people('Electronic Engineering',['football','jazz music','date with girl'])
def search_form(request):
	return render_to_response('search_form.html')
def search(request):
	if request.GET['q']=='tanghy':
		t=get_template('people.html')
		html=t.render(Context({'name':'tanghy','DEP':tanghy.dep,'hobby':tanghy.hobby}))
		#MESS='666'
	elif request.GET['q']=='gaofeng':
		t=get_template('people.html')
		html=t.render(Context({'name':'gaofeng','DEP':gaofeng.dep,
		'hobby':gaofeng.hobby}))
	else:
		html='you should search \'tanghy\' or \'gaofeng\''
	return HttpResponse(html) 