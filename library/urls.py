from django.urls import path
from .views import BookCreateView, BookDetailView, BookStatusUpdateView, BooksList, BookSearch, BookContentView, \
    UserBooksByStatusView, UpdateBookRatingView

urlpatterns = [
    path('upload/', BookCreateView.as_view(), name='BookCreate'),
    path('books/book_page/<str:title>/', BookDetailView.as_view(), name='book-detail'),
    path('books/list/', BooksList.as_view(), name='books-list'),
    path('books/search/', BookSearch.as_view(), name='books-search'),
    path('books/<str:title>/update_status/', BookStatusUpdateView.as_view(), name='book-detail'),
    path('books/<str:book_name>/content/', BookContentView.as_view(), name='book-content'),
    path('books/<str:book_name>/content/<int:chapter>/', BookContentView.as_view(), name='book-chapter'),
    path('books/status/<str:status>/', UserBooksByStatusView.as_view(), name='books-by-status'),
    path('books/<int:book_id>/rate/', UpdateBookRatingView.as_view(), name='update-book-rating'),


]
