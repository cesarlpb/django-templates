from django.contrib import admin
from proyecto.models import MiUser

class MiUserAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(MiUser, MiUserAdmin)
