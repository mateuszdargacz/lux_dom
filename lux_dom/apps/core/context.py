# -*- coding: utf-8 -*-
__author__ = 'mateuszdargacz@gmail.com'
__date__ = '7/9/15 / 11:16 PM'
__git__ = 'https://github.com/mateuszdargacz'

from apps.core.models import HouseType, GalleryImage


def models_context(request):
    return {
        'house_types': HouseType.objects.all(),
        'gallery_images': GalleryImage.objects.all().order_by('order')
    }