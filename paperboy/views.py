from django.http import HttpResponse
from django.shortcuts import render

def root(request):
    # return redirect(reverse('show_all'))
    return HttpResponse('hi!')

def home_page(request):
    # return HttpResponse('hi!')
    response = render(request, 'index.html')
    return HttpResponse(response)