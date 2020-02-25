from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about.html', views.about, name = 'about'),
    path('contact.html', views.contact, name = 'contact')

]
