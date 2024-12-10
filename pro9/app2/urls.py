from django.urls import path
from app2 import views

urlpatterns = [
    path("",views.home,name='home_'),
    path("about",views.about,name='about_'),
    path("contact",views.contact,name='us')
]
