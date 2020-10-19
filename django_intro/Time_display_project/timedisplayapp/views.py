from django.shortcuts import render, HttpResponse
from time import localtime, strftime


def index(request):
    return HttpResponse("Henry's website")


def hello(request):
    return HttpResponse("wasssssuuupppppppppp")


def hello_name(request, name):
    return HttpResponse(f"hello {name}")


def time(request):
    age = 21
    hobbies = ["getting twisted", "coding"]
    context = {
        "time": strftime("%Y-%m-%d %I:%M:%S %p", localtime()),
        "fn": "Henry",
        "age": age,
        "hobbies": hobbies
    }
    return render(request, 'index.html', context)


def returnHTML(request):
    age = 21
    hobbies = ["getting twisted", "coding"]
    context = {
        "fn": "Henry",
        "age": age,
        "hobbies": hobbies
    }
    return render(request, "index.html", context)


def getPost(request):
    if request.method == "GET":
        print("a GET request is being made to this route")
        return render(request, "index.html")
    if request.method == "POST"
    print("a POST request is being made to this route")
    return redirect("/")


def submitting_form_data(request):
    if request.method == "GET":
        print(request.GET)
    if request.method == "POST":
        val_from_field_one = request.POST["one"]
