from django.contrib import admin
from .models import (
	Book,
	Issue,
	BookAuthor,
	BookPublish,
	Member,
)


admin.site.register(Book)
admin.site.register(Issue)
admin.site.register(Member)
admin.site.register(BookAuthor)
admin.site.register(BookPublish)
