from django.urls import path
from . import views

urlpatterns = [
    path('', views.show, name='index'),
    path('shows', views.show),
    path('new', views.new),
    path('add_show', views.add_show),
    path('show_info/<int:id>', views.show_info),
    path('shows/<int:id>/edit', views.edit_shows),
    path('update_info/<int:id>', views.update_info),
    path('delete/<int:id>', views.delete),
]
