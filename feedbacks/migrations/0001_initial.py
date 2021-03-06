# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-11 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.TextField()),
                ('from_email', models.EmailField(max_length=254)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
