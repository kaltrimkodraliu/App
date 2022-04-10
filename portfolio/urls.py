from django.contrib import admin
from django.urls import path, include
from portfolio.views import *

urlpatterns = [
    path('', home_page, name="home"),
    path('about/', about_page, name="about"),
    path('portfolio/', portfolio_page, name="portfolio")
]
