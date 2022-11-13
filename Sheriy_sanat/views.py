from django.core.paginator import Paginator
from django.shortcuts import render

import pandas as pd
# Create your views here.
from Gazal.forms import FormMeta
from Sheriy_sanat.forms import FormTalmeh, FormTazod, FormTanosib, FormTashbih
from Sheriy_sanat.models import Talmeh, Tazod, Tanosib, Tashbeh, File_Talmeh, File_Tazod, File_Tanosib, File_Tashbih


def talmeh(request):
    talmeh = Talmeh.objects.all()
    p = Paginator(talmeh, 6)
    page_number = request.GET.get('page')
    page_talmeh = p.get_page(page_number)

    context = {
        'talmeh': page_talmeh,
    }
    return render(request, 'Sheriy_sanat/talmeh.html', context)


def tazod(request):
    tazod = Tazod.objects.all()
    p = Paginator(tazod, 6)
    page_number = request.GET.get('page')
    page_tazod = p.get_page(page_number)

    context = {
        'tazod': page_tazod,
    }
    return render(request, 'Sheriy_sanat/tazod.html', context)


def tanosib(request):
    tanosib = Tanosib.objects.all()
    p = Paginator(tanosib, 200)
    page_number = request.GET.get('page')
    page_tanosib = p.get_page(page_number)

    context = {
        'tanosib': page_tanosib,
    }
    return render(request, 'Sheriy_sanat/tanosib.html', context)


def tashbeh(request):
    tashbeh = Tashbeh.objects.all()
    p = Paginator(tashbeh, 6)
    page_number = request.GET.get('page')
    page_tashbeh = p.get_page(page_number)

    context = {
        'tashbeh': page_tashbeh,
    }
    return render(request, 'Sheriy_sanat/tashbeh.html', context)


def talmeh_save(request):
    if request.POST:
        form = FormTalmeh(request.POST, request.FILES)
        if form.is_valid():
            File_Talmeh.objects.all().delete()
            fileSW = form.save(commit=False)
            fileSW.name = 'talmeh'
            fileSW.save()

            talmeh_file = File_Talmeh.objects.get(name='talmeh')
            df = pd.read_excel(talmeh_file.files)
            list_of_columns = df.columns.values

            for row in range(len(df[list_of_columns])):
                Talmeh.objects.create(bayt=df[list_of_columns[0]][row], mano=df[list_of_columns[1]][row])

        else:
            form = FormTalmeh()

        return render(request, 'Gazal/file.html', {'form': form})


def tazod_save(request):
    if request.POST:
        form = FormTazod(request.POST, request.FILES)

        if form.is_valid():
            File_Tazod.objects.all().delete()
            fileSW = form.save(commit=False)
            fileSW.name = 'tazod'
            fileSW.save()

            tazod_file = File_Tazod.objects.get(name='tazod')

            df = pd.read_excel(tazod_file.files)
            list_of_columns = df.columns.values

            for row in range(len(df[list_of_columns])):
                Tazod.objects.create(bayt=df[list_of_columns[0]][row], mano=df[list_of_columns[1]][row])

        else:
            form = FormTazod()

        return render(request, 'Gazal/file.html', {'form': form})


def tanosib_save(request):
    if request.POST:
        form = FormTanosib(request.POST, request.FILES)

        if form.is_valid():
            File_Tanosib.objects.all().delete()
            fileSW = form.save(commit=False)
            fileSW.name = 'tanosib'
            fileSW.save()

            tanosib_file = File_Tanosib.objects.get(name='tanosib')

            df = pd.read_excel(tanosib_file.files)
            list_of_columns = df.columns.values

            for row in range(len(df[list_of_columns])):
                Tanosib.objects.create(bayt=df[list_of_columns[0]][row], mano=df[list_of_columns[1]][row])

        else:
            form = FormTanosib()

        return render(request, 'Gazal/file.html', {'form': form})


def tashbih_save(request):
    if request.POST:
        form = FormTashbih(request.POST, request.FILES)

        if form.is_valid():
            File_Tashbih.objects.all().delete()
            fileSW = form.save(commit=False)
            fileSW.name = 'tashbih'
            fileSW.save()

            tashbih_file = File_Tashbih.objects.get(name='tashbih')

            df = pd.read_excel(tashbih_file.files)
            list_of_columns = df.columns.values

            for row in range(len(df[list_of_columns])):
                Tashbeh.objects.create(bayt=df[list_of_columns[0]][row], oxshamish=df[list_of_columns[1]][row], oxshatilmish=df[list_of_columns[2]][row], sabab=df[list_of_columns[3]][row], vosita=df[list_of_columns[4]][row])

        else:
            form = FormTashbih()

        return render(request, 'Gazal/file.html', {'form': form})
