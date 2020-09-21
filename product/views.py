from django.http import HttpResponse
from django.shortcuts import render
from .models import Category, Image


def base(request):
    cats = Category.objects.all()
    image = Image.objects.all()
    return render(request, 'base.html', {'image': image, 'cats': cats})


def category(request, cid):

    cats = Category.objects.all()
    categor = Category.objects.get(pk=cid)
    image = Image.objects.filter(cat=categor)
    return render(request, 'base.html', {'image': image, 'cats': cats})


def new(request):
    return HttpResponse('hi i am aditto')
