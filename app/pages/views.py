from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'pages/index.html')


def about(request):
    data = {"header_h1": "КВАРТИРИ <span>ДЛЯ ВАС</span>",
            "header_p": "Головна >> Квартири для Вас"}
    return render(request, 'pages/about.html', context=data)
