from django.contrib import admin
from .models import Book, Issue, BookAuthor, BookPublish, Genre


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'language',
                    'display_genre', 'stock', 'today_stock')
    search_fields = ('name',)
    readonly_fields = ('today_stock',)
    ordering = ('name',)
    list_filter = ('genre', 'language',)


class BookPublishAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    readonly_fields = ('pk',)

admin.site.register(Book, BookAdmin)
admin.site.register(Issue)
admin.site.register(BookAuthor)
admin.site.register(BookPublish, BookPublishAdmin)
admin.site.register(Genre)
