# Generated by Django 4.2.7 on 2023-11-29 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=200)),
                ('edad', models.IntegerField()),
                ('correo_electronico', models.EmailField(max_length=254)),
                ('sexo', models.CharField(max_length=20)),
                ('numero_telefono', models.CharField(max_length=10)),
                ('destino', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=200)),
                ('edad', models.IntegerField()),
                ('correo_electronico', models.EmailField(max_length=254)),
                ('sexo', models.CharField(max_length=20)),
                ('destino', models.CharField(max_length=200)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('cupos', models.IntegerField()),
            ],
        ),
    ]