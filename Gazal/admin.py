from django.contrib import admin

# Register your models here.
from Gazal.models import Gazal, Auditoriya_yoshi, Matn_tipi, Soz, Misra, File, File_Word, File_Meta

admin.site.register(Gazal)
admin.site.register(Matn_tipi)
admin.site.register(File)
admin.site.register(File_Word)
admin.site.register(File_Meta)


@admin.register(Auditoriya_yoshi)
class Auditoriya_yoshiAdmin(admin.ModelAdmin):
    list_display = ['id', 'yosh']



@admin.register(Soz)
class WordAdmin(admin.ModelAdmin):
    list_display = (
        'soz',
        'mano',
        'soz_id',
        'janr',
        'satr',
        'tip',
        'yosh',
    )
    search_fields = ('soz',)
    list_filter = ('janr', 'tip', 'yosh', 'soz_id')
    list_display_links = ('soz_id',)
    list_editable = ('soz', 'mano')


@admin.register(Misra)
class MisraAdmin(admin.ModelAdmin):
    list_display = (
        'gazal_id',
        'misra',
    )
    search_fields = ('misra',)
    list_filter = ('gazal_id', )
    list_editable = ('misra', )
