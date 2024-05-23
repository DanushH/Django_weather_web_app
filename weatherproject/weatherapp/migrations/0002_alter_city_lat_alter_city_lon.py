# Generated by Django 5.0.6 on 2024-05-23 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='lat',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
        migrations.AlterField(
            model_name='city',
            name='lon',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
    ]