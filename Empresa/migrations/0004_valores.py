# Generated by Django 2.0.3 on 2018-05-16 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Empresa', '0003_auto_20180515_0800'),
    ]

    operations = [
        migrations.CreateModel(
            name='Valores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.CharField(blank=True, max_length=3, null=True)),
                ('concep_valor', models.TextField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]