# Generated by Django 2.0.3 on 2018-08-11 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proyectos', '0005_proyecto_orden'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='orden',
            field=models.IntegerField(default=0),
        ),
    ]
