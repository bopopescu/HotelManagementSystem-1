# Generated by Django 2.0.4 on 2018-11-15 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='password',
            field=models.CharField(default='NULL', max_length=140),
        ),
    ]