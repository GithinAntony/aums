# Generated by Django 3.0.4 on 2020-03-18 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0014_auto_20200318_0938'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctiondetails',
            name='final_status',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=7),
        ),
    ]