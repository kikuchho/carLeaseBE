# Generated by Django 5.2.3 on 2025-07-25 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_bookmark_numberplate_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
