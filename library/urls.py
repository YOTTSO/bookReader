from django.urls import path
from .views import BookCreateView

urlpatterns = [
    path('upload/', BookCreateView.as_view(), name='BookCreate'),
]
