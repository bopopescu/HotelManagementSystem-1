# Generated by Django 2.1.3 on 2018-11-27 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20181127_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinginformation',
            name='no_of_rooms',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='bookinginformation',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]
