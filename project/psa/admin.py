from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Patient)
admin.site.register(Provsvar)
admin.site.register(Kallelse)
admin.site.register(Hantera)