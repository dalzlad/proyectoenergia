# Generated by Django 4.2.1 on 2023-09-04 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicios',
            name='estado',
            field=models.BooleanField(default=True),
        ),
    ]
