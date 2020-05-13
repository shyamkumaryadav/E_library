from django.contrib import admin
from .models import Book,Issue,BookAuthor,BookPublish,Genre

class BookAdmin(admin.ModelAdmin):
	list_display = ('bookid', 'name','author', 'language', 'display_genre','stock','today_stock')
	search_fields = ('name',)
	ordering = ('bookid',)
	list_filter = ('genre', 'language',)


admin.site.register(Book, BookAdmin)
admin.site.register(Issue)
admin.site.register(BookAuthor)
admin.site.register(BookPublish)
admin.site.register(Genre)
