from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.http import HttpResponse
from .models import Product

def index(request):
    price_list = Product.objects.all()
    template = loader.get_template('printona/index.html')
    context = {
        'price_list': price_list
    }
    return HttpResponse(template.render(context, request))

def quote(request):
    from IPython import embed
    # embed()
    print(request.POST)
    template = loader.get_template('printona/index.html##quotationModal')
    context = {
        'price_list': 1
    }
    return HttpResponse(template.render(context, request))

def order(request):
    return HttpResponse("You're building an order.")

def product(request):
    return HttpResponse("You're building an product.")

def user(request):
    return HttpResponse("You're building a user.")
