# Generated by Django 3.2.18 on 2023-12-03 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Way',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origion', models.CharField(max_length=30)),
                ('destination', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('price', models.IntegerField()),
                ('seats', models.IntegerField()),
                ('cancel', models.SmallIntegerField()),
                ('airline', models.CharField(max_length=30)),
                ('way', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.way')),
            ],
        ),
    ]
