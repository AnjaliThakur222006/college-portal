from django.urls import path
from . import View

urlpatterns = [
    path('', View.home, name='home'),
    path('about', View.about, name='about'),
    path('contact', View.contact, name='contact')
]