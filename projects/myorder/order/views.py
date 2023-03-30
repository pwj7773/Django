from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Order
# Create your views here.

def home(request):
    return HttpResponseRedirect('/order/')

def index(request):
    return render(request,'order/index.html/')

def regist(request) :
    if request.method == 'GET' :
        return render(request,'order/regist.html/')
    else :
        Order.objects.create(
            order_text = request.POST['order_text'],
            price = request.POST['price'],
            address = request.POST['address']
        )
        return HttpResponseRedirect('/order/')

def read(request):
    order_list = Order.objects.all().order_by('-id')
    context = {
        'order_list' : order_list
    }
    return render(request,'order/read.html/',context)

def read_order(request,id):
    order = Order.objects.get(id = id)
    context = {
        'order' : order,
        'order_list' : order.order_text.split(',')
    }
    return render(request,'order/read_order.html/',context)

def delete(request,id) :
    Order.objects.get(id = id).delete()
    return HttpResponseRedirect("/order/")

def update(request,id) :
    order = Order.objects.get(id = id)
    if request.method == "GET" :
        context = {'order': order}
        return render(request,'order/update.html/',context)
    else :
        order.order_text = request.POST['order_text']
        order.price = request.POST['price']
        order.address = request.POST['address']
        order.save()
        return HttpResponseRedirect("../../")
    
def search(request) : 
    search_address = request.POST['search_address']
    condition = request.POST['condition']

    order_list = []
    if condition == 'all' :
         order_list = Order.objects.filter(address__contains = search_address)
    else :
         order_list = Order.objects.filter(address__startswith = search_address)

    context = {'order_list' : order_list}
    return render(request,'order/read.html/',context)