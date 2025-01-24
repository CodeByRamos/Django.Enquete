from django.contrib import admin

# Register your models here.

from .models import Perguntas, Escolha

admin.site.register(Perguntas)
admin.site.register(Escolha)