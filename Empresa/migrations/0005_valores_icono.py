# Generated by Django 2.0.3 on 2018-05-16 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Empresa', '0004_valores'),
    ]

    operations = [
        migrations.AddField(
            model_name='valores',
            name='icono',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
    ]