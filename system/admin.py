from django.contrib import admin
from .models import *

class IssueAdmin(admin.ModelAdmin):
	list_display = ['id', 'date']

class BookAuthorAdmin(admin.ModelAdmin):
	list_display = ['id', 'name']

class BookAdmin(admin.ModelAdmin):
	list_display = ['bookid', 'name']

class TestAdmin(admin.ModelAdmin):
	list_display = ['id', 'state']

admin.site.register(Test, TestAdmin)

class BookPublishAdmin(admin.ModelAdmin):
	list_display = ['id', 'name']

admin.site.register(Book, BookAdmin)
admin.site.register(BookAuthor, BookAuthorAdmin)
admin.site.register(BookPublish, BookPublishAdmin)
admin.site.register(Issue, IssueAdmin)