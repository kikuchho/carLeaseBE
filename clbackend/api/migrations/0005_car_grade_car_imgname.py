# Generated by Django 5.2.3 on 2025-06-23 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_car_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='grade',
            field=models.CharField(default='スタンダード', max_length=100),
        ),
        migrations.AddField(
            model_name='car',
            name='imgname',
            field=models.CharField(default='default.png', max_length=100),
        ),
    ]
