# Generated by Django 2.0.3 on 2018-07-27 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0010_auto_20180523_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='subtitulo',
            field=models.TextField(blank=True, null=True),
        ),
    ]