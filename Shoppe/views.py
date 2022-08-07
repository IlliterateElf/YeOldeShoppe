from django.shortcuts import render
from Shoppe.models import ShopItem

# Create your views here.
def index(request):
    return render(request, 'index.html')

def get_shopp_item(request, pk):
    shoppe_objects = ShopItem.objects.get(pk=pk)
    return render(request, "index.html")
