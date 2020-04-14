import requests
from django.shortcuts import render


def homepage(request):
	content_html = open('content/index.html')
    context = {
    'content': content_html
    }
    return render(request, 'base.html', context)

def contact(request):
	content_html = open('content/contact.html')
    context = {
    'content': content_html
    }
    return render(request, 'base.html', context)

def projects(request):
	content_html = open('content/projects.html')
    context = {
    'content': content_html
    }
    return render(request, 'base.html', context)


