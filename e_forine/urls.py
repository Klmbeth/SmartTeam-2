from django.urls import path
from . import views

app_name = 'e_forine'

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('a-propos/', views.a_propos, name='a_propos'),
    path('contact/', views.contact, name='contact'),
    path('prestations/', views.prestations, name='prestations'),
]
