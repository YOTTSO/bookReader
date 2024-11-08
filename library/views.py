from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Book, UserBookStatus
from .serializers import BookSerializer

class BookCreateView(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, title):
        formatted_title = title.replace('_', ' ')
        book = get_object_or_404(Book, title=formatted_title)
        serializer = BookSerializer(book, context={'request': request})
        return Response(serializer.data)

class BookStatusUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, title):
        formatted_title = title.replace('_', ' ')
        book = get_object_or_404(Book, title=formatted_title)
        status = request.data.get('status')
        if status not in ['reading', 'read', 'planned', 'abandoned']:
            return Response({"detail": "Invalid status"})

        book_status, created = UserBookStatus.objects.update_or_create(
            user=request.user,
            book=book,
            defaults={'status': status}
        )
        return Response({"status": book_status.status})
