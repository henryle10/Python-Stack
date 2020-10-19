from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


def show(request):
    context = {
        "all_s": Shows.objects.all()
    }
    return render(request, 'index.html', context)


def new(request):
    return render(request, 'new.html')


def add_show(request):
    errors = Shows.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/new")
    else:
        shows = Shows.objects.create(
            title=request.POST['title'],
            network=request.POST['network'],
            release_date=request.POST['release_date'],
            desc=request.POST['desc']
        )
        # request.session['shows_id'] = shows.id
        shows_id = Shows.objects.last().id
        return redirect(f"/show_info/{shows_id}")


def show_info(request, id):
    show_id = Shows.objects.filter(id=id).first()
    context = {
        "show_id": show_id,
        "all_s": Shows.objects.all()
    }
    return render(request, "show_info.html", context)


def edit_shows(request, id):
    context = {
        "show_id": Shows.objects.get(id=id),
    }
    return render(request, "edit_info.html", context)


def update_info(request, id):
    update = Shows.objects.get(id=id)
    errors = Shows.objects.validator(request.POST)
    print(errors)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/shows/{update.id}/edit")
    else:
        update.title = request.POST['title']
        update.network = request.POST['network']
        # update.release_date = request.POST['release_date']
        update.desc = request.POST['desc']
        update.save()
    return redirect(f"/show_info/{update.id}")


def delete(request, id):
    print(id)
    shows_id = Shows.objects.get(id=id)
    shows_id.delete()
    return redirect("/shows")
