# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-26 22:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('westros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anime_id', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('tag', models.CharField(max_length=1000)),
                ('epidodes', models.IntegerField()),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('members', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('n', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='author',
        ),
        migrations.DeleteModel(
            name='FeedBack',
        ),
        migrations.AddField(
            model_name='anime',
            name='genres',
            field=models.ManyToManyField(to='westros.Genre'),
        ),
    ]
