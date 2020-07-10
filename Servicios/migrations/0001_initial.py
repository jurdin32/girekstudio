# Generated by Django 2.0.3 on 2018-05-13 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImagenesServicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.FileField(upload_to='servicio/')),
                ('estado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Infoicono',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Infoserv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.TextField(default='')),
                ('descripcion', models.TextField(default='')),
                ('infoicono', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Servicios.Infoicono')),
            ],
        ),
        migrations.CreateModel(
            name='Planserv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagenplan', models.FileField(upload_to='planserv/')),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orden', models.IntegerField()),
                ('titulo', models.TextField()),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='planserv',
            name='servicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Servicios.Servicio'),
        ),
        migrations.AddField(
            model_name='infoserv',
            name='servicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Servicios.Servicio'),
        ),
        migrations.AddField(
            model_name='imagenesservicio',
            name='servicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Servicios.Servicio'),
        ),
    ]
