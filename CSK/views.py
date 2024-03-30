from django.shortcuts import render
from django.http import HttpResponse
def msd(request):
    return render(request,'msd.html')
def ruturaj(request):
    return HttpResponse('New captain of CSK')
def sameer(request):
    return HttpResponse('Batter')
def rachin(request):
    return HttpResponse('All-rounder')
def daryl(request):
    return HttpResponse('All-rounder')
def mustafizur(request):
    return HttpResponse('bowler')
def jadeja(request):
    return HttpResponse('All-rounder')
def shivam(request):
    return HttpResponse('All-rounder')
def pathirana(request):
    return HttpResponse('bowler')
def deepak(request):
    return HttpResponse('bowler')
def rahane(request):
    return HttpResponse('batter')
