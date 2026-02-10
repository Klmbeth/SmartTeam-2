from django.urls import path
from . import views

app_name = 'comptes'

urlpatterns = [
    path('connexion/', views.login_view, name='login'),
    path('inscription/', views.inscription, name='inscription'),
]
