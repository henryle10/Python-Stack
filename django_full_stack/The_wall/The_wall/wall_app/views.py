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

    return redirect("/success")


def success(request):
    user_id_is_session = request.session.get("user_id")
    if user_id_is_session:
        user_from_db = User.objects.get(id=user_id_is_session)
        context = {"user": user_from_db}
        return render(request, "success.html", context)
    return redirect("/")


def log(request):
    found_user = User.objects.filter(email=request.POST["email"]).first()

    if found_user:  # if email is found in db
        is_pw_correct = bcrypt.checkpw(
            request.POST["password"].encode(), found_user.password.encode()
        )

        if is_pw_correct:  # if password is correct
            request.session["user_id"] = found_user.id
            return redirect("/dash")
        else:  # if pw is incorrect
            messages.error(request, "Incorrect password")
            return redirect("/")
    else:  # if email is not found
        messages.error(request, "User doesn't exist")
        return redirect("/")


def logout(request):
    request.session.clear()
    return redirect("/")


def dash(request):
    user_id_is_session = request.session.get("user_id")
    all_msg = Message.objects.all()
    all_com = Comment.objects.all()
    if user_id_is_session:
        user_from_db = User.objects.get(id=user_id_is_session)
        context = {
            "user": user_from_db,
            "all_messages": all_msg,
            "all_comm": all_com,
        }
    return render(request, "dash.html", context)


def create_msg(request):
    errors = Message.objects.validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/dash")

    user_message = User.objects.get(id=request.session["user_id"])
    new_msg = Message.objects.create(message=request.POST["message"], user=user_message)
    request.session["msg_id"] = new_msg.id
    return redirect("/dash")


def create_comments(request):
    msg_id = Message.objects.get(id=request.POST["mssg_id"])
    user_id = User.objects.get(id=request.session["user_id"])
    new_comment = Comment.objects.create(
        comment=request.POST["comments"], message=msg_id, user=user_id
    )
    request.session["com_id"] = new_comment.id
    return redirect("/dash")


def delete_com(request, id):
    comm_id = Comment.objects.get(id=id)
    comm_id.delete()
    return redirect("/dash")


def delete_post(request, id):
    post_id = Message.objects.get(id=id)
    post_id.delete()
    return redirect("/dash")


def update_page(request, id):
    context = {
        "msg": Message.objects.get(id=id),
    }
    return render(request, "edit_message.html", context)


def update_post(request, id):
    update = Message.objects.get(id=id)
    update.message = request.POST["messagez"]
    update.save()
    return redirect("/dash")


def liking_msg(request, id):
    current_msg = Message.objects.get(id=id)
    current_user = User.objects.get(id=request.session["user_id"])
    like_check = Message.objects.filter(like=current_user)
    if current_msg not in like_check:
        current_msg.like.add(current_user)
        current_msg.total_likes += 1
        current_msg.save()
    else:
        pass
    return redirect("/dash")
