# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 22:30
from __future__ import unicode_literals

from django.db import migrations, models
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Title')),
                ('short_text', redactor.fields.RedactorField(verbose_name='Text')),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='descriptions',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
