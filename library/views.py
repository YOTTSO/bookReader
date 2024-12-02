from django.http import Http404
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .epub_reader import extract_epub_content
from .models import Book, UserBookStatus
from .serializers import BookSerializer, BooksListSerializer


class BookCreateView(APIView):
    def post(self, request):
        serializer = BooksListSerializer(data=request.data)
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

class BooksList(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer = BooksListSerializer(instance=books, many=True)
        return Response(serializer.data)

class BookSearch(APIView):
    def get(self, request):
        title = request.query_params.get('title')
        genre = request.query_params.get('genre')
        tags = request.query_params.get('tags')
        books = Book.objects.all()

        if title:
            formatted_title = title.replace('_', ' ')
            books = books.filter(title__icontains=formatted_title)
        if genre:
            formatted_genre = genre.replace('_', ' ')
            books = books.filter(genre__icontains=formatted_genre)
        if tags:
            books = books.filter(tags__name=tags)
        if not books.exists():
            return Response({"message": "No books found matching the criteria."}, status=status.HTTP_404_NOT_FOUND)

        serializer = BooksListSerializer(instance=books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

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


class BookContentView(APIView):
    def get(self, request, book_name, chapter=None):
        try:
            book = Book.objects.get(title=book_name)
            file_path = book.file.path
            chapters = extract_epub_content(file_path)

            if chapter is not None:
                chapter = int(chapter)
                if chapter < 1 or chapter > len(chapters):
                    return Response({"error": "Chapter not found."}, status=404)
                return Response({"chapter": chapters[chapter - 1]})

            return Response({"chapters": len(chapters), "titles": [f"Chapter {i + 1}" for i in range(len(chapters))]})
        except Book.DoesNotExist:
            raise Http404("Book not found.")