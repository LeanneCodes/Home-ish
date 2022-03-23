from django.shortcuts import render

# Create your views here.


def decor(request):
    """ A view that renders images of decor images on the page """

    return render(request, 'decor/decor.html')
