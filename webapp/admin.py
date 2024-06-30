from django.contrib import admin
from .models import Orphan, Guardian

admin.site.register(Orphan)
admin.site.register(Guardian)

