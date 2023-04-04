from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item,Order

def index(request):
    return render(request,"item/index.html")

def item_add(request):
    if request.method == 'GET':
        return render(request,"item/item_add.html")
    else :
        Item.objects.create(
            item_name = request.POST['item_name'],
            item_count = request.POST['item_count'],
        )
        return redirect('/item/')
    
def item_show(request):
        item = Item.objects.all()
        if request.GET['item_name'] :  
            item = Item.objects.filter(item_name__contains = request.GET['item_name'])
        return render(request,"item/item_show.html",{'item' : item })

def order_add(request):
        if request.method == "GET" :
            return render(request,"item/order_add.html")
        else :     
            id = request.POST['id']
            order_count = request.POST['order_count']
            item = Item.objects.get(id = id)
            item.order_set.create(
                    item_code = item,
                    quantity = order_count
            )
            return redirect('/item/')
def order_show(request):
     order = Order.objects.all()
     return render(request,"item/order_show.html",{'item' : order })

def sale_show(request):
     item = Item.objects.all()
     return render(request,"item/sale_show.html",{'item' : item })

     