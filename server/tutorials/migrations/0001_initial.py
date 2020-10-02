# Generated by Django 3.1.2 on 2020-10-01 23:09

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=70)),
                ('description', models.CharField(default='', max_length=200)),
                ('published', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=20)),
                ('last_name', models.CharField(default='', max_length=20)),
                ('email', models.CharField(default='', max_length=30)),
                ('password', models.CharField(default='', max_length=20)),
                ('balance', models.IntegerField()),
                ('transactions', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True,
                                                                           max_length=100), blank=True, null=True,
                                                                           size=None)),
            ],
        ),
    ]