# Generated by Django 3.2.18 on 2023-12-28 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0012_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('check', 'Check Out'), ('paid', 'Paid'), ('canceld', 'Canceled')], default='check', max_length=10),
        ),
    ]
