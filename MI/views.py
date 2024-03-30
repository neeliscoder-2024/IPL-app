from django.shortcuts import render
from django.http import HttpResponse
def rohit(request):
    return render(request,'rohit.html')
def hardik(requst):
    return HttpResponse('All-rounder')