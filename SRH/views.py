from django.shortcuts import render
from django.http import HttpResponse
def cummins(request):
    return render(request,'cummins.html')
def travis(request):
    return HttpResponse('batter')
