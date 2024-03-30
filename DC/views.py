from django.shortcuts import render
from django.http import HttpResponse
def rishab(request):
    return render(request,'rishab.html')
def kuldeep(request):
    return HttpResponse('bowler')