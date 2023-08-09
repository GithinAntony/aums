# Generated by Django 3.0.4 on 2020-03-17 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0004_auto_20200318_0148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, null=True)),
                ('Description', models.TextField(null=True)),
                ('Image', models.CharField(max_length=100, null=True)),
                ('Location', models.CharField(max_length=255, null=True)),
                ('Type', models.CharField(max_length=25, null=True)),
                ('Reserve_price', models.CharField(max_length=255, null=True)),
                ('Intial_quote_amount', models.CharField(max_length=255, null=True)),
                ('Mobile', models.CharField(max_length=15, null=True)),
                ('Date', models.CharField(max_length=100, null=True)),
                ('Stime', models.CharField(max_length=100, null=True)),
                ('Etime', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Prop1',
        ),
    ]