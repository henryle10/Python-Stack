from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string


def index(request):
    if "random_count" not in request.session:
        request.session['random_count'] = 0
    else:
        request.session['random_count'] += 1
    context = {
        "random_count": request.session['random_count'],
        "unique_random": get_random_string(length=14),
    }
    return render(request, 'index.html', context)


def reset(request):
    request.session['random_count'] = 0
    return redirect('/')
