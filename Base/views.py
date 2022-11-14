from django.http import FileResponse, Http404
from django.shortcuts import render

# Create your views here.
from Base.models import Maqola, Tarjimayi_hol, View_number


def index(request):
    # views = View_number.objects.all()
    # views.number += 1
    # views.save()
    # context = {
    #     'view': views,
    # }
    return render(request, 'Base/index.html')

def korpus_haqida(request):
    return render(request, 'Base/korpus haqida.html')


def mualliflar(request):
    return render(request, 'Base/mualliflar.html')

def maqola(request):
    maqolalar = Maqola.objects.all()

    context = {
        'maqola': maqolalar,
    }

    return render(request, 'Base/maqola.html', context)


def maqola_pdf(request, id):
    maqola = Maqola.objects.get(id=id)
    maqola_pdf2 = Maqola.objects.filter(name='pdf')
    context = {
        'maqola_pdf': maqola,
    }
    return render(request, 'Base/maqola_pdf.html', context)


def tarjimayi_hol(request):
    dates = Tarjimayi_hol.objects.all()
    context = {
        'dates': dates,
    }
    return render(request, 'Base/tarjimayi hol.html', context)
