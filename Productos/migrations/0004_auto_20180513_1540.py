# Generated by Django 2.0.3 on 2018-05-13 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0003_auto_20180512_2301'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ciudad',
            options={'verbose_name_plural': '1. Ciudad'},
        ),
        migrations.AlterModelOptions(
            name='clasif_producto',
            options={'verbose_name_plural': '3. Clasificaciòn de Producto'},
        ),
        migrations.AlterModelOptions(
            name='producto',
            options={'verbose_name_plural': '4. Producto'},
        ),
        migrations.AlterModelOptions(
            name='producto_imagen',
            options={'verbose_name_plural': '5. Producto Imagenes'},
        ),
        migrations.AlterModelOptions(
            name='proveedor',
            options={'verbose_name_plural': '2. Proveedor'},
        ),
    ]