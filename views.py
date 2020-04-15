import requests
from django.shortcuts import render


def homepage(request):
    context = {}
    return render(request, 'index.html', context)

def contact(request):
    context = {}
    return render(request, 'contact.html', context)

def projects(request):
    context = {}
    return render(request, 'projects.html', context)


def github_api(request):
    response = requests.get('https://api.github.com/users/devdav1999/repos')
    repos = response.json()
    context = {'github_repos':repos}
    return render(request, 'github.html', context)