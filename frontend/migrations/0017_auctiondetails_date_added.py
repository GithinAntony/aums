# Generated by Django 3.0.4 on 2020-06-14 22:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0016_auto_20200318_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctiondetails',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
