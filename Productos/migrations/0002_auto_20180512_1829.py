# Generated by Django 2.0.3 on 2018-05-12 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto_Imagen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('galeria_articulo', models.ImageField(blank=True, help_text='imagen producto 800x800', null=True, upload_to='media')),
            ],
            options={
                'verbose_name_plural': 'galeria de articulo',
            },
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='valor',
            new_name='precio',
        ),
        migrations.AddField(
            model_name='producto_imagen',
            name='producto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Productos.Producto'),
        ),
    ]