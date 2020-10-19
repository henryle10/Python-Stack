from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('success', views.success),
    path('register', views.reg),
    path('login', views.log),
    path('logout', views.logout),
]
