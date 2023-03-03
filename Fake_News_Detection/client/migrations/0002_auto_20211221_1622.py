# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2021-12-21 10:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccuracyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accuracy', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AccuracyModel1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accuracy1', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AccuracyModel2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accuracy2', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AccuracyModel3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accuracy3', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='clientinformation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=300)),
                ('lastname', models.CharField(max_length=200)),
                ('userid', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('phoneno', models.BigIntegerField()),
                ('email', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='FakeRealModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fakenews', models.CharField(max_length=100)),
                ('realnews', models.CharField(max_length=100)),
                ('alpha', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='RegisterModel',
        ),
    ]
