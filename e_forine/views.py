from django.shortcuts import render
from prestations.models import Prestation

def accueil(request):
    prestations = Prestation.objects.filter(active=True).prefetch_related('formules')
    return render(request, 'accueil.html', {
        'prestations': prestations
    })

def a_propos(request):
    return render(request, 'a_propos.html')

def contact(request):
    return render(request, 'contact.html')

def prestations(request):
    prestations = Prestation.objects.filter(active=True).prefetch_related('formules')
    return render(request, 'prestations.html', {
        'prestations': prestations
    })
