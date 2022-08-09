from django.db import models

class UsuarioElsa(models.Model):
    nombreCompleto=models.CharField(max_length=200,verbose_name='nombre')
    email=models.EmailField(max_length=100,verbose_name='email')
    password=models.CharField(max_length=20,verbose_name='password')
    fechaLogin=models.DateField(verbose_name='fechaLogin')
    fechaRegistro=models.DateField(verbose_name='fechaRegistro',null=False)
    ipPc=models.CharField(max_length=20,verbose_name='IP',null=True)
    estado=models.BooleanField(verbose_name='estado',default=True)

    class Meta:
        verbose_name='usuario'
        verbose_name_plural='usuarios'
        db_table='usuarios'

class perfilUsuario(models.Model):
    genero=models.CharField(max_length=20,verbose_name='genero')
    fechaNacimiento=models.DateField(verbose_name='fechaNacimiento')
    estatura=models.FloatField(verbose_name='estatura')
    peso=models.FloatField(verbose_name='peso')
    nivelDeportivo=models.CharField(max_length=100,verbose_name='nivelDeportivo')
    porque=models.CharField(max_length=100,verbose_name='porque')
    dieta=models.CharField(max_length=100,verbose_name='dieta')
    tipoCuerpo=models.CharField(max_length=100,verbose_name='tipoCuerpo')
    potenciometro=models.BooleanField(verbose_name='potenciometro',default=False)
    pulsometro=models.BooleanField(verbose_name='pulsometro',default=False)
    velocimetro=models.BooleanField(verbose_name='velocimetro',default=False)
    cadenciometro=models.BooleanField(verbose_name='cadenciometro',default=False)
    fechaRegistro=models.DateField(verbose_name='fechaRegistro',null=False)
    ipPc=models.CharField(max_length=20,verbose_name='IP',null=True)
    estado=models.BooleanField(verbose_name='estado',default=True)
    idUsuario=models.ForeignKey(UsuarioElsa,on_delete=models.CASCADE)

    class Meta:
        verbose_name='perfilDeUsuario'
        verbose_name_plural='perfilesDeUsuarios'
        db_table='perfilesDeUsuarios'

class Membresia(models.Model):
    tiempo=models.PositiveIntegerField(verbose_name='Duracion',null=False)
    fechaInicial=models.DateField(verbose_name='fechaInicial',null=True)
    fechaTerminacion=models.DateField(verbose_name='fechaTerminacion',null=True)
    precio=models.FloatField(verbose_name='precioMembresia')
    refPayu=models.CharField(max_length=1000,verbose_name='referenciaPagoPayu')
    fechaRegistro=models.DateField(verbose_name='fechaRegistro',null=False)
    ipPc=models.CharField(max_length=20,verbose_name='IP',null=True)
    estado=models.BooleanField(verbose_name='estado',default=True)
    idPerfilUsuario=models.ForeignKey(perfilUsuario, on_delete=models.CASCADE)

    class Meta:
        verbose_name='membresia'
        verbose_name_plural='membresias'
        db_table='membresias'




