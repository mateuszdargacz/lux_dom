# -*- coding: utf-8 -*-
__author__ = 'mateusz'
__date__ = '13.11.14 / 09:00'
__git__ = 'https://github.com/mateuszdargacz'

from django.contrib import admin
from apps.core.models import CImage, HouseDraft, HouseType, GalleryImage

admin.site.register(HouseType)
admin.site.register(HouseDraft)
admin.site.register(CImage)
admin.site.register(GalleryImage)
