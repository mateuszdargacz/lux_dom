# -*- coding: utf-8 -*-
__author__ = 'mateusz'
__date__ = '13.11.14 / 08:59'
__git__ = 'https://github.com/mateuszdargacz'
from django.shortcuts import render


def main(request):
    context = {}
    context.update(active='main')
    return render(request, 'core/main.html', context=context)


def houses(request):
    context = {}
    context.update(active='houses')
    return render(request, 'core/houses.html', context=context)


def hood(request):
    context = {}
    context.update(active='hood')
    return render(request, 'core/hood.html', context=context)


def gallery(request):
    context = {}
    context.update(active='gallery')
    return render(request, 'core/gallery.html', context=context)


def contact(request):
    context = {}
    context.update(active='contact')
    return render(request, 'core/contact.html', context=context)



