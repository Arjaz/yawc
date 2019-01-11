from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def count(request):
    fulltext = request.GET['fulltext']
    words = fulltext.split()
    w_number = len(words)

    word_usage = dict()
    
    for word in words:
        if word in word_usage:
            word_usage[word] += 1
        else:
            word_usage[word] = 1
    
    sorted_words = sorted(word_usage.items(), key=lambda x: x[1], reverse=True)
    return render(request, 'count.html', {'fulltext': fulltext, 'w_number': w_number, 'word_usage': sorted_words})

def about(request):
    return render(request, 'about.html')
