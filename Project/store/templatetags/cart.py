from django import template


register = template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    keys = cart.keys()
    for id in keys:

        if int(id) == product.id:
            return True
    return False

@register.filter(name='cart_quantity')
def cart_quantity(product, cart):
    keys = cart.keys()

    for id in keys:
        if int(id) == product.id:
            return cart[id]

@register.filter(name='item_total')
def item_total(product, cart):
    keys = cart.keys()

    for id in keys:
        if int(id) == product.id:
            return cart[id] * product.original_price

@register.filter(name='cart_total')
def cart_total(products, cart):
    sum = 0

    for p in products:
        sum += item_total(p, cart)
    return sum

@register.filter(name='multiply')
def multiply(n1, n2):
    return n1*n2