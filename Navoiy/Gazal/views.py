from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect
import pandas as pd
# Create your views here.
from Gazal.forms import FormFile, FormWord, FormMeta
from Gazal.models import Gazal, Soz, Misra, File, File_Word, File_Meta
from Maqol_Ibora.models import Maqol
from Sheriy_sanat.models import Talmeh


def gazal(request):

    misra = Misra.objects.all()

    number_word = 0
    sozlar = []
    for i in misra:
        soz = i.misra.split(' ')
        number_word += len(soz)
        sozlar.extend(soz)
    print(sozlar)

    new_sozlar = []
    for i in sozlar:
        if i not in new_sozlar:
            new_sozlar.append(i)

    gazal = Gazal.objects.all()
    p = Paginator(gazal, 100)
    page_number = request.GET.get('page')
    page_gazal = p.get_page(page_number)

    context = {
        'gazal': page_gazal,
        'misra_soni': misra.count(),
        'gazal_soni': gazal.count(),
        'soz_soni': number_word,
        'yangi_sozlar_soni': len(new_sozlar),
    }
    return render(request, 'Gazal/gazal.html', context)


def in_gazal(request, pk):
    new_query = request.GET.get('search_word')
    query = request.GET.get('umumiy')
    print(query)
    if request.method == 'POST':
        gazal_id = request.POST.get('id')
        word1 = request.POST.get('word')
        word2 = word1[0].lower() + word1[1:]

        soz = Soz.objects.filter(soz_id=gazal_id).get(soz=word2)
        print(soz)

        if soz:
            sozIzlanayotgan = soz.soz
            sozmano = soz.mano
            res = {
                'error': True,
                'soz': sozIzlanayotgan,
                'mano': sozmano,
            }
        # elif soz2:
        #     sozIzlanayotgan2 = soz2.soz
        #     sozmano2 = soz2.mano
        #     res = {
        #         'error': True,
        #         'soz': sozIzlanayotgan2,
        #         'mano': sozmano2,
        #     }
        else:
            res = {
                'error': False,
                'soz': '',
                'mano': '',

            }
        return JsonResponse(res)
    in_gazal = Gazal.objects.get(id=pk)

    misra = Misra.objects.filter(gazal_id=pk)

    soz = Soz.objects.filter(soz_id=pk)

    context = {
        'in_gazal': in_gazal,
        'soz': soz,
        'misra': misra,
        'search_word': query,
        'new_search': new_query,
        'oldingi': pk-1,
        'keyingi': pk + 1,
    }
    return render(request, 'Gazal/in_gazal.html', context)

def gazal_meta(request, pk):

    gazal_meta = Gazal.objects.get(id=pk)
    misra = Misra.objects.filter(gazal_id=pk)

    number_word = 0
    for i in misra:
        soz = i.misra.split(' ')

        number_word += len(soz)

    context = {
        'gazal_meta': gazal_meta,
        'number_word': number_word,
    }

    return render(request, 'Gazal/Gazal_meta.html', context)


def file(request):
    files = FormFile
    context = {
        'files': files,
    }

    return render(request, 'Gazal/file.html', context)


def file_save(request):
    if request.POST:
        form = FormFile(request.POST, request.FILES)

        if form.is_valid():
            File.objects.all().delete()
            fileSW = form.save(commit=False)
            fileSW.name = '111'
            print(form)
            print(request.POST)
            fileSW.save()
            file_data = File.objects.get(name='111')
            print(file_data.files)

            df = pd.read_excel(file_data.files)
            list_of_columns = df.columns.values

            first_date = 0
            for row in range(0, len(df)):
                if type(df[list_of_columns[0]][row]) is int:
                    first_date = df[list_of_columns[0]][row]
                    print(df[list_of_columns[0]][row])
                    print(type(df[list_of_columns[0]][row]))

                else:
                    Misra.objects.create(gazal_id_id=first_date, misra=df[list_of_columns[0]][row])
                    print(df[list_of_columns[0]][row])


        else:
            form = FormFile()

        return render(request, 'Gazal/file.html', {'form': form})

    def file_save(request):
        if request.POST:
            form = FormFile(request.POST, request.FILES)

            if form.is_valid():
                File.objects.all().delete()
                fileSW = form.save(commit=False)
                fileSW.name = '111'
                print(form)
                print(request.POST)
                fileSW.save()
                file_data = File.objects.get(name='111')
                print(file_data.files)

                df = pd.read_excel(file_data.files)
                list_of_columns = df.columns.values

                first_date = 0
                for row in range(0, len(df)):
                    if type(df[list_of_columns[0]][row]) is int:
                        first_date = df[list_of_columns[0]][row]
                        print(df[list_of_columns[0]][row])
                        print(type(df[list_of_columns[0]][row]))

                    else:
                        Misra.objects.create(gazal_id_id=first_date, misra=df[list_of_columns[0]][row])
                        print(df[list_of_columns[0]][row])


            else:
                form = FormFile()

            return render(request, 'Gazal/file.html', {'form': form})


def soz_save(request):
    if request.POST:
        form = FormWord(request.POST, request.FILES)

        if form.is_valid():
            File_Word.objects.all().delete()
            fileSW = form.save(commit=False)
            fileSW.name = 'suz'
            print(form)
            print(request.POST)
            fileSW.save()
            word_file = File_Word.objects.get(name='suz')
            print(word_file.files)

            df = pd.read_excel(word_file.files)
            list_of_columns = df.columns.values

            first_date = df[list_of_columns[0]][0]

            for row in range(len(df[list_of_columns])):

                if df[list_of_columns[0]][row] == first_date:
                    Soz.objects.create(soz_id_id=first_date, soz=df[list_of_columns[1]][row],
                                       mano=df[list_of_columns[2]][row], janr=df[list_of_columns[3]][row],
                                       satr_id=df[list_of_columns[4]][row], tip_id=df[list_of_columns[5]][row],
                                       yosh_id=df[list_of_columns[6]][row])
                else:
                    first_date = df[list_of_columns[0]][row]

        else:
            form = FormWord()

        return render(request, 'Gazal/file.html', {'form': form})


def meta_save(request):
    if request.POST:
        form = FormMeta(request.POST, request.FILES)

        if form.is_valid():
            File_Meta.objects.all().delete()
            fileSW = form.save(commit=False)
            fileSW.name = 'meta'
            fileSW.save()

            meta_file = File_Meta.objects.get(name='meta')

            df = pd.read_excel(meta_file.files)
            list_of_columns = df.columns.values

            for row in range(len(df[list_of_columns])):
                Gazal.objects.create(number=df[list_of_columns[0]][row], name=df[list_of_columns[1]][row],
                                     matn_tipi_id=df[list_of_columns[2]][row],
                                     auditoriya_yoshi_id=df[list_of_columns[3]][row])

        else:
            form = FormWord()

        return render(request, 'Gazal/file.html', {'form': form})


