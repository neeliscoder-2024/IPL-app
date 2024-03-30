from django.shortcuts import render
from django.http import HttpResponse
def shubman(request):
    return render(request,'shubman.html')
def shankar(request):
    return HttpResponse('All-rounder')
