from django.shortcuts import render, redirect
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


def search(request):
    apartments_list = Apartments.objects.order_by(
        '-list_date').filter(is_published=True)
    # print("list: ", apartments_list)
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            apartments_list = apartments_list.filter(city__iexact=city)
    print("list: ", apartments_list)
    context = {
        "apartments_list": apartments_list,
        "header_h1": "Пошук",
        "header_p": "Головна >> Пошук",
    }
    return render(request, "pages/search.html", context)


def to_favorites(request):
    if request.method == "POST":
        apartment_id = request.POST['apartment_id']
        if request.user != 'AnonymousUser':
            apartment = Apartments.objects.filter(id=apartment_id)
            filtered_apartment = apartment.filter(Favorites=request.user)
            if filtered_apartment.count() == 0:
                apartment[0].Favorites.add(request.user)
                apartment[0].save()
    return redirect("/apartments/"+apartment_id)
