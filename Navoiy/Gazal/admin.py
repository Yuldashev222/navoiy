from django.contrib import admin

# Register your models here.
from Gazal.models import Gazal, Auditoriya_yoshi, Matn_tipi, Soz, Misra, File, File_Word, File_Meta

admin.site.register(Gazal)
admin.site.register(Auditoriya_yoshi)
admin.site.register(Matn_tipi)
admin.site.register(Soz)
admin.site.register(Misra)
admin.site.register(File)
admin.site.register(File_Word)
admin.site.register(File_Meta)
