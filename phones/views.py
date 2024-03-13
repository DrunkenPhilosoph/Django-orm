from django.http import HttpResponse
from django.shortcuts import render, redirect
from phones.models import Phone
def index(request):
    phones = Phone.objects.all()
    print(phones)
    return redirect('catalog', phones=phones)


def show_catalog(request):
    template = 'catalog.html'
    param = request.GET.get('sort')
    phones_obj = Phone.objects.all()
    if param == 'min_price':
        phones_obj = Phone.objects.order_by('price')
    elif param == 'max_price':
        phones_obj = Phone.objects.order_by('-price')
    elif param == 'name':
        phones_obj = Phone.objects.order_by('name')
    context = { 'phones': phones_obj }
    return render(request, template, context)


def test_list(request):
    phones_obj = Phone.objects.filter(slug='nokia-8')
    phones = [f'<p>{p.name}, {p.price}, {p.image}, {p.release_date}, {p.lte_exists}, {p.slug}</p>' for p in phones_obj]
    return HttpResponse(phones)

def show_product(request, slug):
    template = 'product.html'
    phones_obj = Phone.objects.filter(slug=slug)
    context = {'phone': phones_obj}
    return render(request, template, context)
