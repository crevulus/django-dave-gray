# from django.http import HttpResponse

# def homepage(req):
#     return HttpResponse('homepage')

# def aboutpage(req):
#     return HttpResponse('aboutpage')

from django.shortcuts import render

def homepage(req):
    return render(req,'home.html')

def aboutpage(req):
    return render(req,'about.html')