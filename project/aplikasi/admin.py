from django.contrib import admin
from.models import Biodata, identitas
# Register your models here.


class BiodataAdmin(admin.ModelAdmin):
    list_display = ("npm", "jurusan",)


admin.site.register(Biodata, BiodataAdmin)
admin.site.register(identitas)