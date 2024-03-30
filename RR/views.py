from django.shortcuts import render
from django.http import HttpResponse
def samson(request):
    return render(request,'samson.html')
def krishna(request):
    return HttpResponse('bowler')