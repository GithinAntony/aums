# Generated by Django 3.0.4 on 2020-06-15 00:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0020_auctiondetails_advance_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctiondetails',
            name='card_type',
        ),
    ]
