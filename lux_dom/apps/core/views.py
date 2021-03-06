# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.mail import send_mail

__author__ = 'mateusz'
__date__ = '13.11.14 / 08:59'
__git__ = 'https://github.com/mateuszdargacz'
from django.shortcuts import render, get_object_or_404
from apps.core.models import HouseType, GalleryImage, ETAP_CHOICES, Message


def main(request):
    context = {}
    context.update(active='main')
    return render(request, 'core/main.html', context=context)


def houses(request, pk):
    context = {}
    house = get_object_or_404(HouseType, pk=pk)
    context.update(active='houses', house=house)
    # for x in xrange(1, 4):
    #     images = HouseType.objects.get(pk=x).images.all()
    #     images_pks = images.values_list('pk', flat=True)[:3]
    #     images.exclude(pk__in=images_pks).delete()
    #
    return render(request, 'core/houses.html', context=context)


def hood(request):
    context = {}
    context.update(active='hood')
    return render(request, 'core/hood.html', context=context)


def gallery(request, etap):
    if not etap:
        etap = ETAP_CHOICES[0][0]
    context = {}
    images = GalleryImage.objects.filter(etap=etap).order_by('order')
    if not images:
        images = GalleryImage.objects.filter(etap='etap1').order_by('order') or GalleryImage.objects.all().order_by(
            'order')[:16]
    else:
        context.update(etap=True)
    context.update(active='gallery', images=images, etaps=ETAP_CHOICES, active_etap=etap)
    return render(request, 'core/gallery.html', context=context)


def contact(request):
    context = {}
    context.update(active='contact')
    if request.method == "POST":
        email = request.POST.get('email')
        message = request.POST.get('message')
        Message.objects.create(email=email, message=message)
        if message and email:
            subject = '[L D L] Pytanie'
            message = message + "\n\n EMAIL: %s" % email
            send_mail(subject, message, settings.FROM_EMAIL, settings.EMAIL_RECIPIENTS)
            context.update(email_sent=True)
    return render(request, 'core/contact.html', context=context)




