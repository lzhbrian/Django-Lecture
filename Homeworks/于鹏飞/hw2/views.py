from django.shortcuts import render_to_response
from django.http import HttpResponse

def search(request):
    return render_to_response("search.html")

def profiles(request):

    if 'name' in request.GET:
        if request.GET['name'] == "Yu Pengfei":
            html = people(request.GET['name'],'18','male','yupf15@mails.tsinghua.edu.cn').make_html()
            return HttpResponse(html)
        if request.GET['name'] == "Pengfei Yu":
            html = people(request.GET['name'],'18','male','pfyu15@mails.tsinghua.edu.cn').make_html()
            return HttpResponse(html)
    else:
        return HttpResponse("wrong")

class people:
    def __init__(self, name, year, gender, email):
        self.name = name
        self.year = year
        self.gender = gender
        self.email = email
    def make_html(self):
        return '<p>name:%s</p><br/><p>age:%s<p><br/><p>gender:%s</p><br/><p>email:%s</p><br/>' % (self.name,self.year,self.gender,self.email)

