from django.shortcuts import render, get_object_or_404
from .models import Menu


# Create your views here.
def index(request, path):
    get_object_or_404(Menu.objects, url=f'/{path}/')
    return render(request, 'index.html')
