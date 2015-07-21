# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('caption', models.CharField(max_length=56, verbose_name='podpis zdjecia')),
                ('description', models.TextField(verbose_name='podpis zdjecia')),
                ('image', models.ImageField(upload_to=b'pics/', verbose_name='Plik zdj\u0119cia')),
                ('corder', models.IntegerField(verbose_name='kolejnosc')),
            ],
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('caption', models.CharField(max_length=56, verbose_name='podpis zdjecia')),
                ('description', models.TextField(verbose_name='podpis zdjecia')),
                ('image', models.ImageField(upload_to=b'pics/', verbose_name='Plik zdj\u0119cia')),
                ('order', models.IntegerField(verbose_name='kolejnosc')),
            ],
        ),
        migrations.CreateModel(
            name='HouseDraft',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name='Nazwa')),
                ('desc', models.TextField(verbose_name='Opis')),
            ],
        ),
        migrations.CreateModel(
            name='HouseType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=56, verbose_name='Nazwa')),
                ('description', models.TextField(verbose_name='Opis')),
                ('short_desc', models.TextField(verbose_name='Kr\xf3tki opis')),
                ('space', models.DecimalField(verbose_name='Metra\u017c', max_digits=6, decimal_places=2)),
                ('price', models.DecimalField(verbose_name='Cena', max_digits=10, decimal_places=2)),
            ],
        ),
        migrations.AddField(
            model_name='housedraft',
            name='house_type',
            field=models.ForeignKey(verbose_name='Dom', to='core.HouseType'),
        ),
        migrations.AddField(
            model_name='cimage',
            name='house_type',
            field=models.ForeignKey(related_name='images', verbose_name='Dom', to='core.HouseType'),
        ),
    ]
