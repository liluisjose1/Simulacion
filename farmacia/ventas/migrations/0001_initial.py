# Generated by Django 2.0 on 2018-06-24 04:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detalle_Facturas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10, unique=True)),
                ('cliente', models.CharField(max_length=10)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('medicamento', models.ManyToManyField(through='ventas.Detalle_Facturas', to='inventario.Medicamento')),
            ],
        ),
        migrations.AddField(
            model_name='detalle_facturas',
            name='Factura',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ventas.Factura'),
        ),
        migrations.AddField(
            model_name='detalle_facturas',
            name='medicamento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventario.Medicamento'),
        ),
    ]