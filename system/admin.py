from django.contrib import admin
from .models import *


class BookAuthorAdmin(admin.ModelAdmin):
	list_display = ['id', 'name']

class BookAdmin(admin.ModelAdmin):
	list_display = ['bookid', 'name']


class BookPublishAdmin(admin.ModelAdmin):
	list_display = ['id', 'name']

admin.site.register(Book, BookAdmin)

class IssueAdmin(admin.ModelAdmin):
	list_display = ['id', 'member_id']

admin.site.register(Issue, IssueAdmin)

class MemberAdmin(admin.ModelAdmin):
	list_display = ['id', 'name']

admin.site.register(Member, MemberAdmin)

admin.site.register(State)

admin.site.register(City)

admin.site.register(BookAuthor, BookAuthorAdmin)
admin.site.register(BookPublish, BookPublishAdmin)
