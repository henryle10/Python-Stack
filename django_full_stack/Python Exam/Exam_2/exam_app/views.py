from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt


def index(request):
    return render(request, "index.html")


def reg(request):
    errors = User.objects.validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")

    # if already existing will return an objects of a user
    is_user_in_db = User.objects.filter(email=request.POST["email"]).first()

    if is_user_in_db:
        print("user is already exsiting")
        return redirect("/")

    hashed_pw = bcrypt.hashpw(
        request.POST["password"].encode(), bcrypt.gensalt()
    ).decode()

    user_created = User.objects.create(
        first_name=request.POST["fname"],
        last_name=request.POST["lname"],
        email=request.POST["email"],
        password=hashed_pw,
    )

    request.session["user_id"] = user_created.id
    return redirect("/wishes")


def wishes(request):
    user_id_is_session = request.session.get("user_id")
    all_wishes = Wish.objects.all()
    if user_id_is_session:
        user_from_db = User.objects.get(id=user_id_is_session)
        context = {
            "user": user_from_db,
            "all_wishes": all_wishes,
            "user_wishes": Wish.objects.filter(wished_by=user_from_db),
            "granted_wishes": Wish.objects.filter(grant_wish=True),
            "not_granted": Wish.objects.filter(grant_wish=False),
        }

    return render(request, "success.html", context)


def log(request):
    found_user = User.objects.filter(email=request.POST["email"]).first()

    if found_user:  # if email is found in db
        is_pw_correct = bcrypt.checkpw(
            request.POST["password"].encode(), found_user.password.encode()
        )

        if is_pw_correct:  # if password is correct
            request.session["user_id"] = found_user.id
            return redirect("/wishes")
        else:  # if pw is incorrect
            messages.error(request, "Incorrect password")
            return redirect("/")
    else:  # if email is not found
        messages.error(request, "User doesn't exist")
        return redirect("/")


def logout(request):
    request.session.clear()
    return redirect("/")


def wish_page(request):
    user_id_is_session = request.session.get("user_id")
    if user_id_is_session:
        user_from_db = User.objects.get(id=user_id_is_session)
        context = {"user": user_from_db}
    return render(request, "new_wish.html", context)


def make_wish(request):
    errors = Wish.objects.validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/wish_page")
    else:
        current_user = User.objects.get(id=request.session["user_id"])
        new_wish = Wish.objects.create(
            item=request.POST["wish"],
            description=request.POST["desc"],
            wished_by=current_user,
        )
        request.session["new_wishes"] = new_wish.id
        return redirect("/wishes")


def cancel(request):
    return redirect("/wishes")


def remove(request, id):
    wish_id = Wish.objects.get(id=id)
    wish_id.delete()
    return redirect("/wishes")


def edit_page(request, id):
    user_id_is_session = request.session.get("user_id")
    if user_id_is_session:
        user_from_db = User.objects.get(id=user_id_is_session)
        context = {
            "wish_id": Wish.objects.get(id=id),
            "user": user_from_db,
        }
    return render(request, "edit_page.html", context)


def edit_wish(request, id):
    update = Wish.objects.get(id=id)
    errors = Wish.objects.validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/wishes/{id}/edit")
    else:
        update.item = request.POST["wish"]
        update.description = request.POST["desc"]
        update.save()
    return redirect("/wishes")


def grant_wish(request, id):
    wish_from_db = Wish.objects.get(id=id)
    wish_from_db.grant_wish = not wish_from_db.grant_wish
    wish_from_db.save()
    wish_from_db.wish_count = +1
    return redirect("/wishes")


def likes(request, id):
    current_wish = Wish.objects.get(id=id)
    current_user = User.objects.get(id=request.session["user_id"])
    like_check = Wish.objects.filter(like=current_user)
    if current_wish not in like_check:
        current_wish.like.add(current_user)
        current_wish.total_likes += 1
        current_wish.save()
        return redirect("/wishes")
    else:
        pass
    return redirect("/wishes")


def view_stats(request):
    current_user = User.objects.get(id=request.session["user_id"])
    context = {
        "current_user": current_user,
        "pending_wishes": Wish.objects.filter(grant_wish=False, wished_by=current_user),
        "all_grants": Wish.objects.filter(grant_wish=True),
        "wish_granted": Wish.objects.filter(grant_wish=True, wished_by=current_user),
    }
    return render(request, "stats.html", context)
