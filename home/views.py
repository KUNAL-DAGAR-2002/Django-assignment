from django.shortcuts import render, HttpResponse
from home.models import Customer, Orders
from django.db.models import Sum, Count
from datetime import datetime
# Create your views here.

def index(request):
    orders = Orders.objects.all()
    cust = []
    for order in orders:
        cust.append(order.customer.name)


    total_order = int(orders.count())
    total_customer = len(set(cust))

    values = orders.values_list('order_value',flat=True)
    total_val = 0
    for value in values:
        total_val = total_val + int(value)
    
    average_val = total_val / total_order

    context = {
        'total_order': total_order,
        'total_customer': total_customer,
        'average_val':average_val,
        'total_val':total_val
    }
    
    return render(request,'index.html',context)

def submit(request):
    date = request.GET.get('date')
    date = str(date)
    
    orders = Orders.objects.filter(order_date = date)
    if orders.count()==0:
        context = {
            "message":"No orders found on selected date"
        }
        return render(request,"index.html",context)
    customer_list = []
    for order in orders:
        customer_list.append(order.customer.name)
    customer_list = set(customer_list)

    total_order = int(orders.count())
    total_customer = len(customer_list)
    values = orders.values_list('order_value',flat=True)
    total_val = 0
    for value in values:
        total_val = total_val + int(value)
    
    average_val = total_val / total_order
    context = {
        'total_order': total_order,
        'total_customer': total_customer,
        'average_val':average_val,
        'total_val':total_val
    }
    return render(request,'index.html',context)