# Generated by Django 5.0.6 on 2024-07-21 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas_backend', '0003_empleado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterModelTable(
            name='cliente',
            table='clientes',
        ),
        migrations.DeleteModel(
            name='Oferta',
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
    ]
