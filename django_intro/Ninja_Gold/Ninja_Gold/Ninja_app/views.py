from django.shortcuts import render, HttpResponse, redirect
from random import randint
from datetime import datetime


def index(request):
    if "gold_count" not in request.session:
        request.session["gold_count"] = 0
        request.session["activities"] = []
    context = {
        "gold_count": request.session["gold_count"],
        "activites": request.session["activities"],
    }
    return render(request, "index.html", context)


def process_money(request):
    location = request.POST["location"]

    if location == "reset":
        request.session.clear()

    elif location == "Farm":
        gold = randint(10, 20)
        request.session["gold_count"] += gold
        request.session["activities"].append(
            "you earned "
            + str(gold)
            + " golds from the "
            + request.POST["location"]
            + " "
            + str(datetime.now().strftime("%Y-%m-%d %H:%M"))
        )
    elif location == "Cave":
        gold = randint(5, 10)
        request.session["gold_count"] += gold
        request.session["activities"].append(
            "you earned "
            + str(gold)
            + " golds from the "
            + request.POST["location"]
            + " "
            + str(datetime.now().strftime("%Y-%m-%d %H:%M"))
        )
    elif location == "House":
        gold = randint(2, 5)
        request.session["gold_count"] += gold
        request.session["activities"].append(
            "you earned "
            + str(gold)
            + " golds from the "
            + request.POST["location"]
            + " "
            + str(datetime.now().strftime("%Y-%m-%d %H:%M"))
        )
    elif location == "Casino":
        gold = randint(-50, 50)
        request.session["gold_count"] += gold
        if gold > 0:
            request.session["activities"].append(
                "you earned "
                + str(gold)
                + " golds from the "
                + request.POST["location"]
                + " "
                + str(datetime.now().strftime("%Y-%m-%d %H:%M"))
            )
        else:
            request.session["activities"].append(
                "OOPS you lost "
                + str(gold)
                + " golds from the "
                + request.POST["location"]
                + " "
                + str(datetime.now().strftime("%Y-%m-%d %H:%M"))
            )
    return redirect("/")


# def reset(request):
#     if request.method == "POST":
#         request.session["gold_count"] = 0
#     return redirect("/")
