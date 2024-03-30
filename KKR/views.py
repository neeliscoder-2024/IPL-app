from django.shortcuts import render
from django.http import HttpResponse
def shreyas(request):
    return render(request,'shreyas.html')
def russell(request):
    return HttpResponse('All-rounder')
