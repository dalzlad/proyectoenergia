# Generated by Django 4.2.1 on 2023-07-17 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_profesor', models.CharField(max_length=50)),
                ('apellido_profesor', models.CharField(max_length=70)),
                ('telefono_profesor', models.CharField(max_length=15)),
                ('email_profesor', models.EmailField(max_length=254)),
                ('direccion_profesor', models.TextField()),
                ('numero_documento', models.BigIntegerField()),
                ('tipo_documento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profesor.tipo_documento')),
            ],
        ),
    ]
