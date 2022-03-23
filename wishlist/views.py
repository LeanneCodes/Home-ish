from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.


def wishlist(request):
    """ A view that shows visitors items they have favourited """

    return render(request, 'wishlist/wishlist.html')


def add_to_wishlist(request, item_id):
    """ Add items to wishlist page """

    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    wishlist = request.session.get('wishlist', {})
    messages.success(request, f'Added {product.name} to your wishlist')

    request.session['wishlist'] = wishlist
    return redirect(redirect_url)
