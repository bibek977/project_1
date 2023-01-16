from django.shortcuts import render

from django.http import HttpResponse

owner = [
    {
        'name' : 'Bibek',
        'phone' : 9810258171,
        'gmail' : 'bhattaraibibek91@gmail.com',
        'address' : 'balkumari, Lalitpur'
    },
    {
        'name' : 'Bhattarai',
        'phone' : 9819213927,
        'gmail' : 'leomessi161743@gmail.com',
        'address' : 'piluwa, Bara'
    }
]

def index(request):
    data = {
        'owner' : owner,
        'title' : 'django'
    }
    return render(request, 'blog/home.html', data)

def about(request):
    return render(request, 'blog/about.html')