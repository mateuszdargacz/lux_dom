# -*- coding: utf-8 -*-
__author__ = 'mateusz'
__date__ = '13.11.14 / 08:59'
__git__ = 'https://github.com/mateuszdargacz'
from django.shortcuts import render


def main(request):
    context = {}
    return render(request, 'core/main.html', context=context)


def houses(request):
    context = {}
    return render(request, 'core/houses.html', context=context)


def hood(request):
    context = {}
    return render(request, 'core/hood.html', context=context)


def gallery(request):
    context = {}
    return render(request, 'core/gallery.html', context=context)


def contact(request):
    context = {}
    return render(request, 'core/contact.html', context=context)
