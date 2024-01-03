# Generated by Django 3.2.18 on 2023-12-28 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_alter_order_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('check', 'Check Out'), ('paid', 'Paid'), ('canceld', 'Canceled')], default='check', max_length=10),
        ),
    ]
