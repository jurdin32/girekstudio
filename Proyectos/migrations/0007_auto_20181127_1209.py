# Generated by Django 2.0 on 2018-11-27 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proyectos', '0006_auto_20180811_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='tipo_archivo',
            field=models.CharField(choices=[('imagen', 'imagen'), ('video_horizontal', 'video_horizontal'), ('video', 'video')], default='imagen', max_length=20),
        ),
    ]
