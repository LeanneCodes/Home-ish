from django.shortcuts import render

# Create your views here.


def contact(request):
    # A view that renders contact methods
    # visitors can reach Home(ish) with

    return render(request, 'contact/contact.html')
