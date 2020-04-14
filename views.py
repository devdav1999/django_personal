import requests
from django.shortcuts import render


def homepage(request):
    home_html = open('content/index.html').read()
    context = {
    'content': home_html
    }
    return render(request, 'base.html', context)

def contact(request):
    contact_html = open('content/contact.html').read()
    context = {
    'content': contact_html
    }
    return render(request, 'base.html', context)

def projects(request):
    projects_html = open('content/projects.html').read()
    context = {
    'content': projects_html
    }
    return render(request, 'base.html', context)


