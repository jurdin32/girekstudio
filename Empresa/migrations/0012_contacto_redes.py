# Generated by Django 2.0 on 2018-11-24 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Empresa', '0011_auto_20180531_2142'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto_redes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.CharField(blank=True, max_length=100, null=True)),
                ('instagram', models.CharField(blank=True, max_length=100, null=True)),
                ('twitter', models.CharField(blank=True, max_length=100, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=100, null=True)),
                ('youtube', models.CharField(blank=True, max_length=100, null=True)),
                ('behance', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': '8. Contácto Redes Sociales',
            },
        ),
    ]
