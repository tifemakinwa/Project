from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def greet(request):
#     return HttpResponse('Goodbye my friend',)

# def greet(request):
#     return render(request,'index.html',{'name':'Tife'})

def greet(request):
    return render(request,'index.html',{'age':20})


# def about(request):
#     return render(request, 'index.html')    
