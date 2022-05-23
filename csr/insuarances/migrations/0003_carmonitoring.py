# Generated by Django 4.0.4 on 2022-05-23 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insuarances', '0002_carinsuarance'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarMonitoring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.IntegerField()),
                ('speed', models.IntegerField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insuarances.car')),
            ],
        ),
    ]
