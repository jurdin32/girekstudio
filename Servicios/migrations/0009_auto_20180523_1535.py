# Generated by Django 2.0.3 on 2018-05-23 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Servicios', '0008_auto_20180523_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='servicio/'),
        ),
    ]