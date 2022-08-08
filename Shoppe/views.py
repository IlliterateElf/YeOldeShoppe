from django.shortcuts import render
from Shoppe.models import ShopItem

# Create your views here.
def index(request):
    i = 0
    shop_objects = ShopItem.objects.all()[:20]
    length = len(shop_objects)
    context = {
        'shop_objects': shop_objects
    }
    return render(request, 'index.html', context)
