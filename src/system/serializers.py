from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'edition', 'cost', 'page', 'description', 'stock', 'today_stock', 'rating', 'profile',
                  'publish_date', 'language', ]
