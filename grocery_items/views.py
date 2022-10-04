from django.shortcuts import render, redirect
from .forms import ItemForm
from .models import GroceryItem
from decimal import Decimal

# Create your views here.
def index(request):
    template = 'home.html'
    form = ItemForm()
    items = GroceryItem.objects.all()
    context = {'form': form, 'items': items}
    return render(request, template, context)

def add_item(request):
    item = request.POST['item']
    brand = request.POST['brand']
    location = request.POST['location']
    price = request.POST['price']
    price_type = request.POST['price_type']
    servings = request.POST['servings']
    grocery_item = GroceryItem(
        item=item, 
        brand=brand, 
        location=location, 
        price=price, 
        price_type=price_type, 
        servings=servings
        )
    grocery_item.save()
    return redirect('/')
    
