from django.contrib import admin

# Register your models here.

from .models import Categoria, Produto

admin.site.register(Categoria)
admin.site.register(Produto)