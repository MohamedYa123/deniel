from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect,reverse
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .forms import *
from decimal import Decimal
# Create your views here.


def homepage(request):
    return render(request,template_name="home.html")
def homepage2(request,l):
    return render(request,template_name="home.html")
