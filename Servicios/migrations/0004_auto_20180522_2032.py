# Generated by Django 2.0.3 on 2018-05-23 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Servicios', '0003_auto_20180522_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='contenido_plan_branding',
            name='servicio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Servicios.Servicio'),
        ),
        migrations.AlterField(
            model_name='contenido_plan_branding',
            name='tipo_plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Servicios.Tipo_plan'),
        ),
    ]
