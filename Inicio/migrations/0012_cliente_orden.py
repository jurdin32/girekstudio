# Generated by Django 2.0.3 on 2018-07-29 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0011_slider_subtitulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='orden',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
