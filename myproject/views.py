# from django.http import HttpResponse

# def homepage(req):
#     return HttpResponse('homepage')

# def aboutpage(req):
#     return HttpResponse('aboutpage')

from django.shortcuts import render

def homepage(request):
    return render(request,'home.html')

def aboutpage(request):
    return render(request,'about.html')