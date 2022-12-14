# Generated by Django 4.0 on 2022-08-09 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UsuarioElsa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCompleto', models.TextField(max_length=200, verbose_name='nombre')),
                ('email', models.EmailField(max_length=100, verbose_name='email')),
                ('password', models.TextField(max_length=20, verbose_name='password')),
                ('fechaLogin', models.DateField(verbose_name='fechaLogin')),
                ('fechaRegistro', models.DateField(verbose_name='fechaRegistro')),
                ('ipPc', models.TextField(max_length=20, null=True, verbose_name='IP')),
                ('estado', models.BooleanField(default=True, verbose_name='estado')),
            ],
            options={
                'verbose_name': 'usuario',
                'verbose_name_plural': 'usuarios',
                'db_table': 'usuarios',
            },
        ),
        migrations.CreateModel(
            name='perfilUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.TextField(max_length=20, verbose_name='genero')),
                ('fechaNacimiento', models.DateField(verbose_name='fechaNacimiento')),
                ('estatura', models.FloatField(verbose_name='estatura')),
                ('peso', models.FloatField(verbose_name='peso')),
                ('nivelDeportivo', models.TextField(max_length=100, verbose_name='nivelDeportivo')),
                ('porque', models.TextField(max_length=100, verbose_name='porque')),
                ('dieta', models.TextField(max_length=100, verbose_name='dieta')),
                ('tipoCuerpo', models.TextField(max_length=100, verbose_name='tipoCuerpo')),
                ('potenciometro', models.BooleanField(default=False, verbose_name='potenciometro')),
                ('pulsometro', models.BooleanField(default=False, verbose_name='pulsometro')),
                ('velocimetro', models.BooleanField(default=False, verbose_name='velocimetro')),
                ('cadenciometro', models.BooleanField(default=False, verbose_name='cadenciometro')),
                ('fechaRegistro', models.DateField(verbose_name='fechaRegistro')),
                ('ipPc', models.TextField(max_length=20, null=True, verbose_name='IP')),
                ('estado', models.BooleanField(default=True, verbose_name='estado')),
                ('idUsuario', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.usuarioelsa')),
            ],
            options={
                'verbose_name': 'perfilDeUsuario',
                'verbose_name_plural': 'perfilesDeUsuarios',
                'db_table': 'perfilesDeUsuarios',
            },
        ),
        migrations.CreateModel(
            name='Membresia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiempo', models.PositiveIntegerField(verbose_name='Duracion')),
                ('fechaInicial', models.DateField(null=True, verbose_name='fechaInicial')),
                ('fechaTerminacion', models.DateField(null=True, verbose_name='fechaTerminacion')),
                ('precio', models.FloatField(verbose_name='precioMembresia')),
                ('refPayu', models.TextField(verbose_name='referenciaPagoPayu')),
                ('fechaRegistro', models.DateField(verbose_name='fechaRegistro')),
                ('ipPc', models.TextField(max_length=20, null=True, verbose_name='IP')),
                ('estado', models.BooleanField(default=True, verbose_name='estado')),
                ('idPerfilUsuario', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.perfilusuario')),
            ],
            options={
                'verbose_name': 'membresia',
                'verbose_name_plural': 'membresias',
                'db_table': 'membresias',
            },
        ),
    ]
