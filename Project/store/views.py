from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView, FormView, View, TemplateView
from django.shortcuts import render, HttpResponse, redirect
from django.utils.decorators import method_decorator
from django.urls import reverse
from .models import item, category, Order
from .middlewares.auth import auth_middleware


class StoreListView(ListView):
    template_name="store/store.html"


    def post(self, request, category_id):
        product_id = request.POST.get('item_id')
        cart = request.session.get('cart')  
        if cart != None:
            quantity = cart.get(product_id)
            if quantity:
                plus_minus = request.POST.get('plus_minus')
                if plus_minus == '+':
                    cart[product_id] = quantity+1                
                elif plus_minus == '-':
                    cart[product_id] = quantity-1
                    if cart[product_id] == 0:
                       cart.pop(product_id)
                       if(not cart):
                           del request.session['cart']
                           return redirect('store', category_id=category_id)
                else:
                    cart[product_id] = quantity+1
            else:
                cart[product_id] = 1
        else:
            cart = {}
            cart[product_id] = 1

        request.session['cart'] = cart
        return redirect('store', category_id=category_id)

    def get(self, request, category_id):
        category_list = category.get_all_categories()
        if(category_id == "AllProducts"):
            object_list = item.get_all_items()
        else:
            object_list = item.get_items_by_categoryID(int(category_id))
        if 'query' in request.GET:
            query = request.GET['query']
            object_list = object_list.filter(name__icontains=query)
        context = {'category_list': category_list, 'object_list': object_list}
        return render(request, 'store/store.html', context)  


class ItemDetailView(DetailView):
    model=item
    template_name="store/detail.html"


class CartView(ListView):
    template_name = 'store/cart.html'

    @method_decorator(auth_middleware)
    def get(self, request):
        cart = []
        if request.session.get('cart') != None:
            cart = list(request.session.get('cart').keys())
        object_list = item.get_items_by_IDs(cart)
        if 'query' in request.GET:
            query = request.GET['query']
            object_list = object_list.filter(name__icontains=query)
        context = {'object_list': object_list}
        return render(request, 'store/cart.html', context)
    
    @method_decorator(auth_middleware)    
    def post(self, request):       
        cart = request.session.get('cart')
        product_id = request.POST.get('item_id')
        if cart == None:
            cart = {
                product_id: 1
            }
        else:
            cart[product_id] = 1
        request.session['cart'] = cart
        return redirect('cart')
    
class OrderListView(ListView):
    template_name = 'store/orders.html'
    
    @method_decorator(auth_middleware)
    def get(self, request):
        customer_id = request.user.id
        orders = Order.get_orders_by_userid(customer_id)
        context = {'orders': orders}
        return render(request, 'store/orders.html', context)
    
    
class CheckoutView(TemplateView):
    template_name='store/orders.html'

    def get(self, request):
        cart = request.session.get('cart')
        keys = list(cart.keys())
        items = item.get_items_by_IDs(keys)

        customer = request.user
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        for i in items:
            order = Order(customer=customer,
                          product=i,
                          contact=phone,
                          address=address,
                          quantity=cart.get(str(i.id)),
                          price=i.original_price
                          )    
            order.save()
        request.session['cart'] = {}        
        return redirect(reverse('orders'))   
