from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.http import HttpResponse

def index(request):
    template = loader.get_template('printona/index.html')
    context = {} 
    return HttpResponse(template.render(context, request))

def order(request):
    return HttpResponse("You're building an order.")

def product(request):
    return HttpResponse("You're building an product.")

def user(request):
    return HttpResponse("You're building a user.")
