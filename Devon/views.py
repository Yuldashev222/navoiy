from django.shortcuts import render


# Create your views here.
from Devon.models import Devon


def devon(request):
    devonlar = Devon.objects.all()
    context = {
        'devon': devonlar,
    }
    return render(request, 'Devon/devon.html', context)


def in_devon(request, pk):
    devon = Devon.objects.get(id=pk)

    context = {
        'devon': devon,
    }
    return render(request, 'Devon/in_devon.html', context)

