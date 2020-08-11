from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('success')

def rfailed(reqeust):
    a = 202/0
    return HttpResponse('request failed')