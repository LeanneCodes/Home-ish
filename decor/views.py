from django.shortcuts import render

# Create your views here.


def decor(request):
    """ A view that shows design inspirations """

    return render(request, 'decor/decor.html')
