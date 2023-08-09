# Generated by Django 3.0.2 on 2020-02-23 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amount',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, null=True)),
                ('amount', models.CharField(max_length=255, null=True)),
                ('tamo', models.CharField(max_length=25, null=True)),
                ('result', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Image', models.CharField(max_length=100, null=True)),
                ('Name', models.CharField(max_length=255, null=True)),
                ('Dob', models.CharField(max_length=25, null=True)),
                ('Gender', models.CharField(max_length=255, null=True)),
                ('Address', models.CharField(max_length=15, null=True)),
                ('Mobileno', models.TextField(null=True)),
                ('Qualification', models.CharField(max_length=255, null=True)),
                ('Emailid', models.IntegerField(null=True)),
                ('Username', models.CharField(max_length=255, null=True)),
                ('Password', models.CharField(max_length=15, null=True)),
                ('Status', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fback',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100, null=True)),
                ('feedback', models.CharField(max_length=255, null=True)),
                ('response', models.CharField(max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prop1',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Image', models.CharField(max_length=100, null=True)),
                ('Location', models.CharField(max_length=255, null=True)),
                ('Type', models.CharField(max_length=25, null=True)),
                ('Amount', models.CharField(max_length=255, null=True)),
                ('Description', models.TextField(null=True)),
                ('Mobileno', models.CharField(max_length=15, null=True)),
                ('Username', models.CharField(max_length=255, null=True)),
                ('Status', models.CharField(max_length=100, null=True)),
                ('Usertype', models.CharField(max_length=100, null=True)),
                ('Adate', models.CharField(max_length=100, null=True)),
                ('Stime', models.CharField(max_length=100, null=True)),
                ('Etime', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reg',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Image', models.CharField(max_length=100, null=True)),
                ('Name', models.CharField(max_length=255, null=True)),
                ('Dob', models.CharField(max_length=25, null=True)),
                ('Gender', models.CharField(max_length=255, null=True)),
                ('Address', models.CharField(max_length=15, null=True)),
                ('Mobileno', models.CharField(max_length=15, null=True)),
                ('Nationality', models.CharField(max_length=255, null=True)),
                ('Emailid', models.TextField(null=True)),
                ('Username', models.CharField(max_length=255, null=True)),
                ('Password', models.CharField(max_length=50, null=True)),
                ('Status', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, null=True)),
                ('amount', models.CharField(max_length=255, null=True)),
                ('sdate', models.CharField(max_length=25, null=True)),
                ('username', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=255, null=True)),
                ('username', models.CharField(max_length=25, null=True)),
                ('password', models.CharField(max_length=255, null=True)),
                ('phone', models.CharField(max_length=15, null=True)),
                ('address', models.TextField(null=True)),
                ('place', models.CharField(max_length=255, null=True)),
                ('status', models.IntegerField(null=True)),
            ],
        ),
    ]