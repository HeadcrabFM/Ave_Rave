from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'main/index.html')

def aboutaverave(request):
    return render(request,'main/info.html')

def contacts(request):
    return render(request,'main/contacts.html')
