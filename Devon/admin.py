from django.contrib import admin

# Register your models here.
from Devon.models import Devon, Janrlar, JanrMisra, JanrMisraSoz, ChistonJavob

admin.site.register([Devon, Janrlar, ChistonJavob])


@admin.register(JanrMisraSoz)
class JanrMisraSozAdmin(admin.ModelAdmin):
    list_display = ['id', 'janr', 'janr_number', 'soz', 'mano', 'auditoriya_yoshi']


@admin.register(JanrMisra)
class JanrMisraAdmin(admin.ModelAdmin):
    list_display = ['id', 'janr_number', 'janr', 'misra', 'chiston_javobi']
