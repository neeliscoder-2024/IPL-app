from django.shortcuts import render
from django.http import HttpResponse
def kl(request):
    return render(request,'kl.html')
def mayers(request):
    return HttpResponse('All-rounder')
