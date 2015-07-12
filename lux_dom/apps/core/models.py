# -*- coding: utf-8 -*-
__author__ = 'mateusz'
__date__ = '13.11.14 / 08:59'
__git__ = 'https://github.com/mateuszdargacz'

from django.db import models
from django.utils.translation import gettext_lazy as _

# TOOD INSTALL PILLOW
class HouseType(models.Model):
    name = models.CharField(_('Nazwa'), max_length=56)
    description = models.TextField(_('Opis'))
    short_desc = models.TextField(_('Krótki opis'))
    space = models.DecimalField(_('Metraż'), max_digits=6, decimal_places=2)
    price = models.DecimalField(_('Cena'), max_digits=10, decimal_places=2)

    @property
    def get_price(self):
        return self.price

    def __unicode__(self):
        return self.name


class HouseDraft(models.Model):
    name = models.CharField(_('Nazwa'), max_length=128)
    desc = models.TextField(_('Opis'))
    house_type = models.ForeignKey('HouseType', verbose_name=_('Dom'))

    def __unicode__(self):
        return self.name


class CImage(models.Model):
    caption = models.CharField(_('podpis zdjecia'), max_length=56)
    description = models.TextField(_('podpis zdjecia'))
    image = models.ImageField(_('Plik zdjęcia'), upload_to='pics/')
    house_type = models.ForeignKey('HouseType', verbose_name=_('Dom'), related_name='images')
    order = models.IntegerField(_('kolejnosc'), max_length=3)

    def __unicode__(self):
        return self.caption


class GalleryImage(models.Model):
    caption = models.CharField(_('podpis zdjecia'), max_length=56)
    description = models.TextField(_('podpis zdjecia'))
    image = models.ImageField(_('Plik zdjęcia'), upload_to='pics/')
    order = models.IntegerField(_('kolejnosc'), max_length=3)

    def __unicode__(self):
        return self.caption
