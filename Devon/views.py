from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from Devon.models import Devon, Janrlar, JanrMisra, JanrMisraSoz


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


def janr(request):
    janrlar = Janrlar.objects.all()

    context = {
        'janrlar': janrlar,
    }
    return render(request, 'Devon/janrlar.html', context)


def in_janr(request, pk):
    Janr = Janrlar.objects.get(id=pk)
    janr_misra = JanrMisra.objects.filter(janr_id=pk).values('janr_id', 'janr_number')

    seen = set()
    number = []
    for i in janr_misra:
        t = tuple(i.items())
        if t not in seen:
            seen.add(t)
            number.append(i)

    context = {
        'janr_number': number,
        'Janr': Janr,
    }
    return render(request, 'Devon/in_janr.html', context)


def janr_misra(request, pk):
    query = request.GET.get('Janr_name')
    janr_name = Janrlar.objects.get(id=query)
    janr_misra = JanrMisra.objects.filter(janr_id=query, janr_number=pk).values('janr_id', 'janr_number', 'misra')
    janr_new = janr_misra[0]
    print(janr_new)

    if request.method == 'POST':
        janr_id = request.POST.get('janr_id')
        janr_word1 = request.POST.get('janr_word')
        janr_word2 = janr_word1[0].lower() + janr_word1[1:]
        janr_soz = JanrMisraSoz.objects.filter(janr_id=query, janr_number=pk).filter(soz=janr_word2)

        if janr_soz.exists():
            janr_soz = janr_soz.first()
            janr_sozIzlanayotgan = janr_soz.soz
            janr_sozmano = janr_soz.mano
            res = {
                'error': True,
                'soz': janr_sozIzlanayotgan,
                'mano': janr_sozmano,
            }

        else:
            mano = 'kiritilmagan'
            res = {
                'error': False,
                'soz': '',
                'mano': mano,

            }
        return JsonResponse(res)

    context = {
        'janr_misra': janr_misra,
        'janr': query,
        'janr_new': janr_new,
        'janr_name': janr_name,
    }

    return render(request, 'Devon/janr_misra.html', context)

