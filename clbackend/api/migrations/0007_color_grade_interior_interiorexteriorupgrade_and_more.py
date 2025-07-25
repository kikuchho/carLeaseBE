# Generated by Django 5.2.3 on 2025-07-17 08:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_bookmark_plan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('color', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('car_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='colors', to='api.car')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('grade', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('car_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grades', to='api.car')),
            ],
        ),
        migrations.CreateModel(
            name='Interior',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('interior', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('car_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interiors', to='api.car')),
            ],
        ),
        migrations.CreateModel(
            name='InteriorExteriorUpgrade',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('interior_exterior_upgrade', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('car_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interior_exterior_upgrades', to='api.car')),
            ],
        ),
        migrations.CreateModel(
            name='OptionPackage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('optionpackage', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('car_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='option_packages', to='api.car')),
            ],
        ),
    ]
