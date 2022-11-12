from django.contrib import admin

# Register your models here.
from Sheriy_sanat.models import Talmeh, Tazod, Tanosib, Tashbeh, File_Talmeh, File_Tazod, File_Tanosib, File_Tashbih

admin.site.register(Talmeh)
admin.site.register(Tazod)
admin.site.register(Tanosib)
admin.site.register(Tashbeh)
admin.site.register(File_Talmeh)
admin.site.register(File_Tazod)
admin.site.register(File_Tanosib)
admin.site.register(File_Tashbih)
