# Generated by Django 2.1.3 on 2018-11-28 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_auto_20181128_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinginformation',
            name='booking_id',
            field=models.IntegerField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
