from django.shortcuts import render
from Shoppe.models import ShopItem

# Create your views here.
def index(request):
    return render(request, 'index.html')
