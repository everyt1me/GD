from django.shortcuts import render
from .models import Apartments
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404


def index(request):
    apartments = Apartments.objects.order_by(
        '-list_date').filter(is_published=True)

    paginator = Paginator(apartments, 2)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    context = {
        "apartments": page,
        "header_h1": "Квартири <span>для вас</span>",
        "header_p": "Головна >> Квартири для вас",
    }
    return render(request, "pages/apartments.html", context)


def apartment(request, apartment_id):
    apartment = get_object_or_404(Apartments, pk=apartment_id)
    context = {
        "apartment": apartment,
        "header_h1": "Квартири <span>для вас</span>",
        "header_p": "Головна >> Квартири для вас",
    }
    return render(request, "pages/apartment.html", context)
