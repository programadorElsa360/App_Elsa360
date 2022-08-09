from django.views import View
from .models import UsuarioElsa,perfilUsuario,Membresia
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
class UsuarioView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request,  *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id=0):
        if(id>0):
            usuarios=list(UsuarioElsa.objects.filter(id=id).values())
            if len(usuarios)>0:
                usuario=usuarios[0]
                datos={'mensaje':'Exito','usuarios':usuario}
            else:
                datos={'mensaje':'Usuario no encontrado'}
            
            return JsonResponse(datos)


        else:
            usuarios=list(UsuarioElsa.objects.values())
            if len(usuarios)>0:
                datos={'mensaje':'Exito','usuarios':usuarios}
            else:
                datos={'mensaje':'Usuarios no encontrados'}
        return JsonResponse(datos)

    def post(self,request):
        jsonDatos=json.loads(request.body)
        UsuarioElsa.objects.create(
            nombreCompleto=jsonDatos['nombreCompleto'],
            email=jsonDatos['email'],
            password=jsonDatos['password'],
            fechaLogin=jsonDatos['fechaLogin'],
            fechaRegistro=jsonDatos['fechaRegistro'],
            ipPc=jsonDatos['ipPc'],
            estado=jsonDatos['estado']
            )
        datos={'mensaje':'Registro exitoso'}
        return JsonResponse(datos)

    def put(self,request,id):
        jsonDatos=json.loads(request.body)
        usuario=list(UsuarioElsa.objects.filter(id=id).values())
        if len(usuario)>0:
            usuario=UsuarioElsa.objects.get(id=id)
            usuario.nombreCompleto=jsonDatos['nombreCompleto']
            usuario.email=jsonDatos['email']
            usuario.password=jsonDatos['password']
            usuario.fechaLogin=jsonDatos['fechaLogin']
            usuario.fechaRegistro=jsonDatos['fechaRegistro']
            usuario.ipPc=jsonDatos['ipPc']
            usuario.estado=jsonDatos['estado']
            usuario.save()
            datos={'mensaje':'Registro exitoso'}
        else:
            datos={'mensaje':'Usuarios no encontrados'}
        return JsonResponse(datos)


    def delete(self,request,id):
        usuarios=list(UsuarioElsa.objects.filter(id=id).values())
        if len(usuarios)>0:
            UsuarioElsa.objects.filter(id=id).delete()
            datos={'mensaje':'Registro eliminado con exitoso'}
        else:
            datos={'mensaje':'Usuario no encontrado'}
        
        return JsonResponse(datos)


class PerfilUsuariosView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request,  *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id=0):
        if(id>0):
            perfiles=list(perfilUsuario.objects.filter(id=id).values())
            if len(perfiles)>0:
                perfil=perfiles[0]
                datos={'mensaje':'Exito','perfil':perfil}
            else:
                datos={'mensaje':'Perfil no encontrado'}
            
            return JsonResponse(datos)


        else:
            perfiles=list(perfilUsuario.objects.values())
            if len(perfiles)>0:
                datos={'mensaje':'Exito','perfiles':perfiles}
            else:
                datos={'mensaje':'Perfiles no encontrados'}
        return JsonResponse(datos)

    def post(self,request):
        jsonDatos=json.loads(request.body)
        perfilUsuario.objects.create(
            genero=jsonDatos['genero'],
            fechaNacimiento=jsonDatos['fechaNacimiento'],
            estatura=jsonDatos['estatura'],
            peso=jsonDatos['peso'],
            nivelDeportivo=jsonDatos['nivelDeportivo'],
            porque=jsonDatos['porque'],
            dieta=jsonDatos['dieta'],
            tipoCuerpo=jsonDatos['tipoCuerpo'],
            potenciometro=jsonDatos['potenciometro'],
            pulsometro=jsonDatos['pulsometro'],
            velocimetro=jsonDatos['velocimetro'],
            cadenciometro=jsonDatos['cadenciometro'],
            fechaRegistro=jsonDatos['fechaRegistro'],
            ipPc=jsonDatos['ipPc'],
            estado=jsonDatos['estado'],
            idUsuario=jsonDatos['idUsuario']
            )
        datos={'mensaje':'Perfil registrado con exito'}
        return JsonResponse(datos)

    def put(self,request,id):
        jsonDatos=json.loads(request.body)
        perfil=list(perfilUsuario.objects.filter(id=id).values())
        if len(perfil)>0:
            perfil=perfilUsuario.objects.get(id=id)
            perfil.genero=jsonDatos['genero'],
            perfil.fechaNacimiento=jsonDatos['fechaNacimiento'],
            perfil.estatura=jsonDatos['estatura'],
            perfil.peso=jsonDatos['peso'],
            perfil.nivelDeportivo=jsonDatos['nivelDeportivo'],
            perfil.porque=jsonDatos['porque'],
            perfil.dieta=jsonDatos['dieta'],
            perfil.tipoCuerpo=jsonDatos['tipoCuerpo'],
            perfil.potenciometro=jsonDatos['potenciometro'],
            perfil.pulsometro=jsonDatos['pulsometro'],
            perfil.velocimetro=jsonDatos['velocimetro'],
            perfil.cadenciometro=jsonDatos['cadenciometro'],
            perfil.fechaRegistro=jsonDatos['fechaRegistro'],
            perfil.ipPc=jsonDatos['ipPc'],
            perfil.estado=jsonDatos['estado'],
            perfil.idUsuario=jsonDatos['idUsuario']
            perfil.save()
            datos={'mensaje':'Perfil actualizado con exitoso'}
        else:
            datos={'mensaje':'Perfil no encontrado'}
        return JsonResponse(datos)


    def delete(self,request,id):
        perfiles=list(perfilUsuario.objects.filter(id=id).values())
        if len(perfiles)>0:
            UsuarioElsa.objects.filter(id=id).delete()
            datos={'mensaje':'Perfil eliminado con exitoso'}
        else:
            datos={'mensaje':'Perfil no encontrado'}
        
        return JsonResponse(datos)

