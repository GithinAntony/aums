# Generated by Django 3.0.4 on 2020-03-18 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0015_auctiondetails_final_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctiondetails',
            name='final_status',
        ),
        migrations.AddField(
            model_name='property',
            name='final_status',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=7),
        ),
    ]
