from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("success", views.success),
    path("register", views.reg),
    path("login", views.log),
    path("logout", views.logout),
    path("dash", views.dash),
    path("create_msg", views.create_msg),
    path("create_comments", views.create_comments),
    path("delete_com/<int:id>", views.delete_com),
    path("delete_post/<int:id>", views.delete_post),
    path("update_page/<int:id>", views.update_page),
    path("update_post/<int:id>", views.update_post),
    path("liking_msg/<int:id>", views.liking_msg),
]
