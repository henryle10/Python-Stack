from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt


def index(request):
    request.session.clear()
    return render(request, "index.html")


def reg(request):
    errors = User.objects.validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")

    # if already existing will return an objects of a user
    is_user_in_db = User.objects.filter(email=request.POST['email']).first()

    if is_user_in_db:
        print("user is already exsiting")
        return redirect("/")

    hashed_pw = bcrypt.hashpw(
        request.POST['password'].encode(), bcrypt.gensalt()).decode()

    user_created = User.objects.create(
        first_name=request.POST['fname'],
        last_name=request.POST['lname'],
        email=request.POST['email'],
        password=hashed_pw
    )

    request.session['user_id'] = user_created.id

    return redirect('/success')


def success(request):
    user_id_is_session = request.session.get('user_id')
    if user_id_is_session:
        user_from_db = User.objects.get(id=user_id_is_session)
        context = {
            "user": user_from_db
        }
        return render(request, "success.html", context)
    return redirect("/")


def log(request):
    found_user = User.objects.filter(email=request.POST['email']).first()

    if found_user:  # if email is found in db
        is_pw_correct = bcrypt.checkpw(
            request.POST['password'].encode(),
            found_user.password.encode()
        )

        if is_pw_correct:  # if password is correct
            request.session['user_id'] = found_user.id
            return redirect('/success')
        else:  # if pw is incorrect
            print("something is not working")
            return redirect("/")
    else:  # if email is not found
        print("something is not working")
        return redirect("/")


def logout(request):
    request.session.clear()
    return redirect("/")
