from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.http import HttpResponse
from .models import Product
import simplejson as json

def index(request):

    price_list = Product.objects.all()
    list_p = list(price_list.values())

    catalogue={}
    for price in list_p:
        catalogue[ price['id']] = str(price['cost'])


    template = loader.get_template('printona/index.html')
    context = {
        'price_list': price_list,
        'catalogue': catalogue,
    }

    return HttpResponse(template.render(context, request))

def quote(request):

    print(request.POST)
    template = loader.get_template('printona/index.html')
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
