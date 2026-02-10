from django.shortcuts import render

def login_view(request):
    return render(request, 'a_propos.html')

def inscription(request):
    return render(request, 'contact.html')
