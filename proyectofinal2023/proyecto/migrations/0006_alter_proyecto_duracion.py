# Generated by Django 4.1.6 on 2023-05-25 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0005_alter_proyecto_duracion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='duracion',
            field=models.DecimalField(decimal_places=2, max_digits=78, verbose_name='Duracion (Meses)'),
        ),
    ]
