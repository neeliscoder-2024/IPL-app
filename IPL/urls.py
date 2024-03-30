"""
URL configuration for IPL project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from CSK.views import *
from DC.views import *
from GT.views import *
from KKR.views import *
from LSG.views import *
from MI.views import *
from PBKS.views import *
from RCB.views import *
from RR.views import *
from SRH.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('msd/',msd,name='msd'),
    path('ruturaj/',ruturaj,name='ruturaj'),
    path('sameer/',sameer,name='sameer'),
    path('rachin/',rachin,name='rachin'),
    path('daryl/',daryl,name='daryl'),
    path('mustafizur/',mustafizur,name='mustafizur'),
    path('jadeja/',jadeja,name='jadeja'),
    path('shivam/',shivam,name='shivam'),
    path('pathirana/',pathirana,name='pathirana'),
    path('deepak/',deepak,name='deepak'),
    path('rahane/',rahane,name='rahane'),
    path('rishab/',rishab,name='rishab'),
    path('kuldeep/',kuldeep,name='kuldeep'),
    path('shubman/',shubman,name='shubman'),
    path('shankar/',shankar,name='shankar'),
    path('shreyas/',shreyas,name='shreyas'),
    path('russell/',russell,name='russell'),
    path('kl/',kl,name='kl'),
    path('mayers/',mayers,name='mayers'),
    path('rohit/',rohit,name='rohit'),
    path('hardik/',hardik,name='hardik'),
    path('dhawan/',dhawan,name='dhawan'),
    path('bairstow/',bairstow,name='bairstow'),
    path('virat/',virat,name='virat'),
    path('duplessis/',duplessis,name='duplessis'),
    path('cummins/',cummins,name='cummins'),
    path('travis/',travis,name='travis'),
]
