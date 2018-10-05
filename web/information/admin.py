from django.contrib import admin
from information.models import Maintainance

# Register your models here.
class MaintainanceAdmin(admin.ModelAdmin):
    fields = ['set_maintainance_page']

admin.site.register(Maintainance, MaintainanceAdmin)
