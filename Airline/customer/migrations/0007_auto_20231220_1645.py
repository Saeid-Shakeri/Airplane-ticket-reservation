# Generated by Django 3.2.18 on 2023-12-20 13:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_rename_fly_order_flight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='flight',
        ),
        migrations.AddField(
            model_name='order',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='order',
            name='number',
            field=models.SmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='order',
            name='ticket',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='customer.ticket'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='password',
            field=models.CharField(max_length=30),
        ),
    ]