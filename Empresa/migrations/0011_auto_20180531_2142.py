# Generated by Django 2.0.3 on 2018-06-01 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Empresa', '0010_auto_20180522_0828'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto_empresa',
            name='calle',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contacto_empresa',
            name='correo_personal',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contacto_empresa',
            name='representante',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
