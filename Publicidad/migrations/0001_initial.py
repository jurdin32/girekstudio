# Generated by Django 2.0.3 on 2018-05-22 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publicidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publi_inicio', models.FileField(help_text='Imagen 1028 x 500', upload_to='publicidad/')),
                ('publi_servicio', models.FileField(help_text='Imagen  x ', upload_to='publicidad/')),
                ('publi_producto', models.FileField(help_text='Imagen  x ', upload_to='publicidad/')),
                ('publi_producto2', models.FileField(help_text='Imagen  x ', upload_to='publicidad/')),
                ('publi_blog', models.FileField(help_text='Imagen  x ', upload_to='publicidad/')),
                ('publi_blog2', models.FileField(help_text='Imagen  x ', upload_to='publicidad/')),
            ],
        ),
    ]
