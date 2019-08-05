from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from paperboy.models import Paperboy

def root(request):
    return redirect(reverse("show_all"))

def show_all(request):
    paperboys = Paperboy.objects.all()
    context = {"paperboys": paperboys}
    return render(request, "show_all.html", context)