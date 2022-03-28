from django.shortcuts import render

# Create your views here.


def wishlist(request):
    """ A view that shows visitors items they have favourited """

    return render(request, 'wishlist/wishlist.html')

