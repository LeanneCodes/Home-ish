from django.http.response import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from products.models import Wishlist, Product

# Create your views here.


def wishlist(request):
    """ A view that shows visitors items they have favourited """

    return render(request, 'wishlist/wishlist.html')


def add_to_wishlist(request):
    """ Add items to wishlist page """

    wishlist_items = Wishlist.objects.filter(product=request.product)

    context = {
        'wishlist_items': wishlist_items,
    }

    return render(request, 'wishlist/wishlist.html', context)
