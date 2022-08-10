from django.shortcuts import render, redirect
from django.contrib import auth, messages
from Shoppe.models import ShopItem
from django.shortcuts import HttpResponse

# Create your views here.
def rdrct(request):
    return redirect('index')

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
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')
