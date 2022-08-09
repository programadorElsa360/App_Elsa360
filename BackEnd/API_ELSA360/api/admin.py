from django.contrib import admin
from .models import Membresia, UsuarioElsa, perfilUsuario

# Register your models here.
admin.site.register(UsuarioElsa)
admin.site.register(perfilUsuario)
admin.site.register(Membresia)