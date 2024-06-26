# Generated by Django 4.1.6 on 2024-06-01 10:21

from django.db import migrations, models
import proveedores.models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='rfc',
            field=models.CharField(
                max_length=13,
                validators=[proveedores.models.validate_rfc],
                verbose_name='R.F.C'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='telefono',
            field=models.PositiveBigIntegerField(),
        ),
    ]
