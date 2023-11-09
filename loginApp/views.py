from django.shortcuts import render
from django.http import HttpResponse

def loginPage(request):
    s="Welcome Mirvan"
    return HttpResponse(s)
# Create your views here.
