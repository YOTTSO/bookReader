from django.urls import path
from .views import BookCreateView, BookDetailView, BookStatusUpdateView

urlpatterns = [
    path('upload/', BookCreateView.as_view(), name='BookCreate'),
    path('books/<str:title>/', BookDetailView.as_view(), name='book-detail'),
    path('books/<str:title>/update_status/', BookStatusUpdateView.as_view(), name='book-detail'),
]
