from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('hello', views.hello),
    path('hello/<str:name>', views.hello_name),
    path('html', views.returnHTML),
    path('time_display', views.time),
]
