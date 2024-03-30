from django.shortcuts import render
from django.http import HttpResponse
def virat(request):
    return render(request,'virat.html')
def duplessis(request):
    return HttpResponse('batter')
