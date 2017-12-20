from django.shortcuts import render

from minerals.models import Mineral
import random


def index(request):
    '''Home page displaying all minerals'''
    minerals = Mineral.objects.all()
    random_mineral = random.choice(minerals)
    return render(request, 'index.html', {'minerals': minerals,'random_mineral': random_mineral})
