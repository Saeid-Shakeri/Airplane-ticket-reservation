# Generated by Django 3.2.18 on 2023-12-05 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_ticket'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='custome',
            new_name='customer',
        ),
        migrations.AlterField(
            model_name='customer',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]