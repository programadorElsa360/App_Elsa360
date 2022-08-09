from django.urls import path
from .views import UsuarioView,PerfilUsuariosView
urlpatterns=[
    path('usuarios/',UsuarioView.as_view(),name='listarUsuarios'),
    path('usuarios/<int:id>',UsuarioView.as_view(),name='procesosDeUsuarios'),
     path('perfiles/',PerfilUsuariosView.as_view(),name='listarPerfiles'),
    path('perfiles/<int:id>',PerfilUsuariosView.as_view(),name='procesosDePerfiles'),
]