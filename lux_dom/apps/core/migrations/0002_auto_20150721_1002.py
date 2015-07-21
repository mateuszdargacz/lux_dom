# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryimage',
            name='etap',
            field=models.CharField(blank=True, max_length=20, null=True, choices=[(b'etap1', b'Prace ziemne i fundamenty.'), (b'etap2', b'Wykonanie \xc5\x9bcian oraz gabaryt\xc3\xb3w domu'), (b'etap3', b'Wyko\xc5\x84czenia')]),
        ),
        migrations.AlterField(
            model_name='cimage',
            name='corder',
            field=models.IntegerField(null=True, verbose_name='kolejnosc', blank=True),
        ),
        migrations.AlterField(
            model_name='cimage',
            name='image',
            field=models.ImageField(upload_to=b'pics/', verbose_name='Plik zdj\u0119cia'),
        ),
        migrations.AlterField(
            model_name='galleryimage',
            name='image',
            field=models.ImageField(upload_to=b'pics/', verbose_name='Plik zdj\u0119cia'),
        ),
        migrations.AlterField(
            model_name='galleryimage',
            name='order',
            field=models.IntegerField(null=True, verbose_name='kolejnosc', blank=True),
        ),
        migrations.AlterField(
            model_name='housetype',
            name='short_desc',
            field=models.TextField(verbose_name='Kr\xf3tki opis'),
        ),
        migrations.AlterField(
            model_name='housetype',
            name='space',
            field=models.DecimalField(verbose_name='Metra\u017c', max_digits=6, decimal_places=2),
        ),
    ]
