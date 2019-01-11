from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def count(request):
    fulltext = request.GET['fulltext']
    w_number = fulltext.count(' ') + 1
    return render(request, 'count.html', {'fulltext': fulltext, 'w_number': w_number})
