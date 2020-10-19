from django.shortcuts import render, HttpResponse, redirect


def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")


def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")


def show(request, num):
    return HttpResponse(f"placeholder to display a new form to create a new blog:{num}")


def create(request):
    return redirect("/")


def edit(request, num):
    return HttpResponse(f"placeholder to display a new form to create a new blog:{num}")


def destroy(request, num):
    return redirect("/")
