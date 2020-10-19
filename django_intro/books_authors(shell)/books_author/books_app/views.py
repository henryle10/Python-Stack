from django.shortcuts import render, redirect
from .models import *


def index(request):
    context = {
        "all_b": Book.objects.all(),
    }
    return render(request, "index.html", context)


def add_b(request):
    Book.objects.create(
        title=request.POST["title"], desc=request.POST["desc"])
    return redirect('/')


def show_b(request, id):
    print(id)
    b = Book.objects.filter(id=id).first()
    context = {
        "book": b,
        "publisherz": author.objects.all()
    }
    return render(request, "book.html", context)


def add_author_book(request, id):
    b = Book.objects.get(id=id)
    c = author.objects.get(id=request.POST["authorz"])
    b.publishers.add(c)
    return redirect("/")


def authors(request):
    context = {
        'all_a': author.objects.all()
    }
    return render(request, "authors.html", context)


def add_a(request):
    author.objects.create(
        name=request.POST['name'], notes=request.POST['notes'])
    return redirect('/authors')


def author_view(request, id):
    af = author.objects.filter(id=id).first()
    context = {
        'all_a': author.objects.all(),
        'author_filt': af,
        'all_books': Book.objects.all()
    }
    return render(request, "author_view.html", context)


def add_book_author(request, id):
    a = author.objects.get(id=id)
    c = Book.objects.get(id=request.POST["bookz"])
    a.books.add(c)
    return redirect("/")
