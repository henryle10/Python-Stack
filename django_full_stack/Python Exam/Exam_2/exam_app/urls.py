from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wishes", views.wishes),
    path("register", views.reg),
    path("login", views.log),
    path("logout", views.logout),
    path("wish_page", views.wish_page),
    path("make_wish", views.make_wish),
    path("cancel", views.cancel),
    path("remove/<int:id>", views.remove),
    path("wishes/<int:id>/edit", views.edit_page),
    path("edit_wish/<int:id>", views.edit_wish),
    path("grant_wish/<int:id>", views.grant_wish),
    path("likes/<int:id>", views.likes),
    path("view_stats", views.view_stats),
]
