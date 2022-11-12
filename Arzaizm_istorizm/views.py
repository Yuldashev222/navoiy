import pandas as pd
from django.core.paginator import Paginator
from django.shortcuts import render

from Arzaizm_istorizm.forms import FormArxaizm
from Arzaizm_istorizm.models import arxaizm, istorizm, File_Arxaizm


def Arxaizm(request):
    soz = arxaizm.objects.all()
    p = Paginator(soz, 30)
    page_number = request.GET.get('page')
    page_soz = p.get_page(page_number)
    context = {
        'soz': soz,
        'soz_soni': soz.count(),
    }
    return render(request, 'Arzaizm_istorizm/arxaizm.html', context)


def Istorizm(request):
    soz = istorizm.objects.all()
    context = {
        'soz': soz,
        'soz_soni': soz.count(),
    }
    return render(request, 'Arzaizm_istorizm/istorizm.html', context)


def arxaizm_save(request):
    if request.POST:
        form = FormArxaizm(request.POST, request.FILES)

        if form.is_valid():
            File_Arxaizm.objects.all().delete()
            fileSW = form.save(commit=False)
            fileSW.name = 'arxaizm'
            fileSW.save()

            meta_file = File_Arxaizm.objects.get(name='arxaizm')

            df = pd.read_excel(meta_file.files)
            list_of_columns = df.columns.values

            for row in range(len(df[list_of_columns])):
                arxaizm.objects.create(soz=df[list_of_columns[0]][row], mano=df[list_of_columns[1]][row])

        else:
            form = FormArxaizm()

        return render(request, 'Gazal/file.html', {'form': form})
