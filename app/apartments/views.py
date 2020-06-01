from django.shortcuts import render
from .models import Apartments


def index(request):
    apartments = Apartments.objects.order_by(
        '-list_date').filter(is_published=True)
    # print(apartments)
    context = {
        "apartments": apartments
    }
    return render(request, "pages/apartment.html", context)
