from django.contrib import admin
from django.urls import path, include
from portfolio.views import home_page

urlpatterns = [
    path('', home_page, name="home"),
]
