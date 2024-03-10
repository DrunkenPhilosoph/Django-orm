from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    phones = Phone.objects.all()
    print(phones)
    return redirect('catalog', phones=phones)


def show_catalog(request):
    template = 'catalog.html'

    context = {}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)
