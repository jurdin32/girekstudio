# Generated by Django 2.0 on 2018-12-02 01:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Proyectos', '0009_auto_20181201_1718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proyecto',
            name='link',
        ),
    ]