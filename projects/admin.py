from django.contrib import admin
from .models import *


class ProjetAdmin(admin.ModelAdmin):
    list_display = ('title', 'orderNum')
    list_editable =('orderNum',)
    ordering = ('-orderNum',)

admin.site.register(Project,ProjetAdmin)
