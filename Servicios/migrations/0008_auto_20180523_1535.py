# Generated by Django 2.0.3 on 2018-05-23 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Servicios', '0007_auto_20180522_2111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planserv',
            name='servicio',
        ),
        migrations.AddField(
            model_name='servicio',
            name='video',
            field=models.FileField(blank=True, default=False, null=True, upload_to='servicio/'),
        ),
        migrations.DeleteModel(
            name='Planserv',
        ),
    ]
