# Generated by Django 4.1.6 on 2023-05-24 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0003_alter_proyecto_proveedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='duracion',
            field=models.DecimalField(
                decimal_places=2, max_digits=78,
                verbose_name='Duracion (Meses)'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='nombre_proyecto',
            field=models.CharField(
                max_length=255, verbose_name='Nombre del proyecto'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='objetivo',
            field=models.TextField(max_length=255, verbose_name='Objetivo'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='presupuesto',
            field=models.CharField(
                max_length=15, verbose_name='Presupuesto ($)'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='responsables',
            field=models.CharField(max_length=200, verbose_name='Responsable'),
        ),
    ]
