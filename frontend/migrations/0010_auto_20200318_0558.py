# Generated by Django 3.0.4 on 2020-03-18 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0009_auto_20200318_0556'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='iIntial_quote_amount',
            new_name='intial_quote_amount',
        ),
    ]