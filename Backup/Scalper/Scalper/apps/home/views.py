from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def Home(request, id):
    return render(request, './templates/base/sample_blank.html')


def helloWorld(request):
    return HttpResponse('Hello World!')
