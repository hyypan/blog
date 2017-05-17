# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-17 07:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yafish', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plate',
            name='name',
            field=models.CharField(choices=[('python', 'python'), ('vue', 'vue'), ('linux', 'linux'), ('docker', 'docker'), ('ansible', 'ansible'), ('nginx', 'nginx'), ('others', 'others')], max_length=50, verbose_name='板块名称'),
        ),
    ]
