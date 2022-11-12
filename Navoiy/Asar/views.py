from django.core.paginator import Paginator
from django.shortcuts import render


# Create your views here.
from Asar.models import Asar


def asar(request):
    asarlar = Asar.objects.all()
    p = Paginator(asarlar, 6)
    page_number = request.GET.get('page')
    page_asar = p.get_page(page_number)

    context = {
        'asar': page_asar,
    }
    return render(request, 'Asar/asar.html', context)


