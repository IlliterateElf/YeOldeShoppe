from django.shortcuts import render, redirect
from Shoppe.models import ShopItem
from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def searching(request):
    query = request.POST['textField']
    return redirect('search', query)

def search(request, pk):
    query = pk
    shop_objects = ShopItem.objects.filter(name__contains=query)[:20]
    context = {
        'shop_objects': shop_objects,
        'query': query
    }
    return render(request, 'search.html', context)

def view_item(request, pk):
    shop_item = ShopItem.objects.get(serial_number__exact=pk)
    context = {
        'shop_item': shop_item,
        'serial_number': pk
    }
    return render(request, 'shop_item.html', context)

def login(request):
    return render(request, 'login.html')