from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('index.html', views.index, name="index"),
    path('about.html', views.about, name="about"),
    path('guarantee.html', views.guarantee, name="guarantee"),
    path('apartment.html', views.apartment, name="apartment"),
    path('discounts.html', views.discounts, name="discounts"),
]
