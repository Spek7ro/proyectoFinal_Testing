# Generated by Django 4.1.6 on 2024-06-02 22:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costos', '0005_alter_costo_proyecto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costo',
            name='costo',
            field=models.DecimalField(
                decimal_places=2, max_digits=10,
                validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='costo',
            name='descripcion',
            field=models.CharField(
                max_length=255,
                validators=[django.core.validators.MaxLengthValidator(255)]),
        ),
    ]
