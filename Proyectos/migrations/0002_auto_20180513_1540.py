# Generated by Django 2.0.3 on 2018-05-13 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Proyectos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagenesproyecto',
            options={'verbose_name_plural': '3. Proyecto Imagenes'},
        ),
        migrations.AlterModelOptions(
            name='portafolio',
            options={'verbose_name_plural': '1. Tema Protafolio'},
        ),
        migrations.AlterModelOptions(
            name='proyecto',
            options={'verbose_name_plural': '2. Proyecto'},
        ),
    ]