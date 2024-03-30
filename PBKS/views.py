from django.shortcuts import render
from django.http import HttpResponse
def dhawan(request):
    return render(request,'dhawan.html')
def bairstow(request):
    return HttpResponse('Wicket-keeper')
