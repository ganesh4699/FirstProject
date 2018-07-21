from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#def index(request):
#    return HttpResponse("Hi  I am comming from HttpResponse")

def index(request):
    dict1={'use_me':"Innovator of the PYTHON:"}
    return render (request,'first_template/index.html',context=dict1)