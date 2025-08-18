from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.contrib import messages

def product_list(request):
    products = Product.objects.all()
    return render(request, 'catalogue/products.html', {'products': products})

def product_details(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'catalogue/product_details.html', {'product': product})

def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)
    cart = request.session.get('cart', {})
    if str(id) in cart:
        cart[str(id)] += 1
    else:
        cart[str(id)] = 1
    request.session['cart'] = cart
    messages.success(request, f"Added {product.name} to cart.")
    return redirect('cart_detail')

def cart_detail(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        item_total = product.price * quantity
        total_price += item_total
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'item_total': item_total,
        })
    return render(request, 'catalogue/cart.html', {'cart_items': cart_items, 'total_price': total_price})

def remove_from_cart(request, id):
    cart = request.session.get('cart', {})
    if str(id) in cart:
        del cart[str(id)]
    request.session['cart'] = cart
    messages.success(request, "Removed item from cart.")
    return redirect('cart_detail')
