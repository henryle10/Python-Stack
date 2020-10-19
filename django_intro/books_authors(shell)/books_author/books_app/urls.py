from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book/<int:id>', views.show_b),
    path('add_book', views.add_b),
    path('add_author_book/<int:id>', views.add_author_book),
    path("authors", views.authors),
    path('author_view/<int:id>', views.author_view),
    path('add_a', views.add_a),
    path('add_book_author/<int:id>', views.add_book_author),
]
