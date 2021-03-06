# Generated by Django 2.1.3 on 2019-06-02 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookingHistory',
            fields=[
                ('bookingid', models.BigIntegerField(default=0, primary_key=True, serialize=False)),
                ('checkin', models.CharField(default='NULL', max_length=140)),
                ('checkout', models.CharField(default='NULL', max_length=140)),
                ('email', models.EmailField(max_length=50)),
                ('userid', models.BigIntegerField(default=0)),
            ],
            options={
                'db_table': 'bookinghistory',
            },
        ),
        migrations.CreateModel(
            name='RoomBooking',
            fields=[
                ('bookingid', models.BigIntegerField(default=0, primary_key=True, serialize=False)),
                ('checkin', models.CharField(default='NULL', max_length=140)),
                ('checkout', models.CharField(default='NULL', max_length=140)),
                ('firstname', models.CharField(max_length=140)),
                ('middlename', models.CharField(max_length=140)),
                ('lastname', models.CharField(max_length=140)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.TextField(max_length=400)),
                ('city', models.CharField(max_length=140)),
                ('state', models.CharField(max_length=140)),
                ('zipcode', models.IntegerField()),
                ('idproof', models.CharField(max_length=140)),
                ('rooms', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'roombooking',
            },
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomtype', models.CharField(default='NULL', max_length=140)),
                ('total', models.BigIntegerField(default=0)),
                ('available', models.BigIntegerField(default=0)),
            ],
            options={
                'db_table': 'rooms',
            },
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('email', models.EmailField(max_length=100, primary_key=True, serialize=False)),
                ('address', models.TextField(max_length=400)),
                ('password', models.CharField(default='NULL', max_length=140)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
