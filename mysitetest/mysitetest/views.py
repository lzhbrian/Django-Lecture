from django.http import HttpResponse, Http404
import datetime

def hello(request): 
	return HttpResponse("Hello world") 

def time_ahead(request, offset):
	try:  
		offset = int(offset)
	except ValueError: 
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	# assert False
	html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
	return HttpResponse(html)
