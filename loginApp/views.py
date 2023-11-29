from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def loginPage(request):
    # s="<h1>Welcome Mirvan</h1>"
    template=loader.get_template('login.html')
    response=template.render()
    return HttpResponse(response)

def aeLoginPage(request):
    template=loader.get_template('aelogin.html')
    response=template.render()
    return HttpResponse(response)
    
