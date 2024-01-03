# Generated by Django 3.2.18 on 2023-12-28 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0010_alter_ticket_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('check', 'Check Out'), ('paid', 'Paid'), ('canceld', 'Canceled')], default='not', max_length=10),
        ),
    ]
