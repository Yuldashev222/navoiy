from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
# Create your views here.
from django.views.decorators.http import require_GET

from Devon.models import Devon, Janrlar
from Gazal.models import Gazal, Misra, Soz
# from colorama import Fore, Back, Style, init
import json


def search(request):
    devonlar = Devon.objects.all()
    janrlar = Janrlar.objects.all()
    gazal = Gazal.objects.all()

    context = {
        'devon': devonlar,
        'janr': janrlar,
        'gazal': gazal,
    }

    return render(request, 'Search/Search.html', context)


def search_result(request):
    query = request.GET.get('umumiy')
    misra = Misra.objects.filter(Q(misra__icontains=query))
    print(misra)
    misra_soni = misra.count()



    gazal = Gazal.objects.filter(misra__misra__icontains=query)
    new_gazal = []
    for x in gazal:
        if x not in new_gazal:
            new_gazal.append(x)

    gazal_soni = len(new_gazal)

    context = {
        'misra': misra,
        'misra_soni': misra_soni,
        'gazal_soni': gazal_soni,
        'search_word': query,
    }
    return render(request, 'Search/Search_result.html', context)


def search_special(request):
    global context
    if request.method == "POST":
        devon = request.POST.get('devon')
        gazal = request.POST.get('gazal')
        janr = request.POST.get('janr')
        key_word = request.POST.get('key_word')
        key_word2 = request.POST.get('key_word2')
        print(request.POST)

        if key_word and devon:
            # if not key_word2:
            misra = Misra.objects.filter(misra__icontains=key_word)
            misra_soni = misra.count()
            gazal = Gazal.objects.filter(misra__misra__icontains=key_word)
            new_gazal = []
            for x in gazal:
                if x not in new_gazal:
                    new_gazal.append(x)

            gazal_soni = len(new_gazal)

            context = {
                'misra': misra,
                'misra_soni': misra_soni,
                'gazal_soni': gazal_soni,
                'search_word': key_word,
            }

    return render(request, 'Search/Search_special.html', context)
