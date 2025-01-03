from rest_framework import serializers
from .models import Book, UserBookStatus, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']

class BookSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    tags = TagSerializer(many=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'genre', 'publication_date', 'tags', 'file', 'status', 'rating']

    def get_status(self, obj):
        user = self.context['request'].user
        book_status = UserBookStatus.objects.filter(user=user, book=obj).first()
        if book_status:
            return book_status.status
        return None

class UserBookStatusSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = UserBookStatus
        fields = ['book', 'status']

class BooksListSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'publication_date', 'tags', 'file']

'''
    from library.models import Book
    from library.serializers import BooksListSerializer
    books = Book.objects.all()
    print((BooksListSerializer(books, many=True)).data)

'''