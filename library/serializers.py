from rest_framework import serializers
from .models import Book, UserBookStatus


class BookSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'publication_date', 'tags', 'file', 'status']

    def get_status(self, obj):
        user = self.context['request'].user
        book_status = UserBookStatus.objects.filter(user=user, book=obj).first()
        if book_status:
            return book_status.status
        return None

class BooksListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'publication_date', 'tags', 'file']

'''
    from library.models import Book
    from library.serializers import BooksListSerializer
    books = Book.objects.all()
    print((BooksListSerializer(books, many=True)).data)

'''