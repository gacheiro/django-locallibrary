from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('borrowed/', views.LoanedBooksView.as_view(), name='all-borrowed'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]

# Book views
urlpatterns += [
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/create/', views.BookCreateView.as_view(), name='book-create'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('book/<int:pk>/update', views.BookUpdateView.as_view(), name='book-update'),
    path('book/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book-delete'),
    path('book/<uuid:pk>/renew/', views.RenewBookView.as_view(), name='renew-book-librarian'),
]

# Author views
urlpatterns += [
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/create/', views.AuthorCreateView.as_view(), name='author-create'),
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),
    path('author/<int:pk>/update/', views.AuthorUpdateView.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', views.AuthorDeleteView.as_view(), name='author-delete'),
]
