from django.contrib import admin
from django.db.models import F
from import_export.admin import ImportExportModelAdmin
from .models import Book, Issue, BookAuthor, BookPublish, Genre
import decimal


def apply_discount(modeladmin, request, queryset):
    queryset.update(cost=F('cost') * decimal.Decimal('0.9'))
apply_discount.short_description = 'Apply 10%% discount'


@admin.register(Book)
class BookAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'author', 'date', 'stock', 'today_stock')
    search_fields = ('name',)
    readonly_fields = ('today_stock', 'pk','date')
    ordering = ('name',)
    actions = [apply_discount, ]
    list_filter = ('edition', 'language',)

@admin.register(BookAuthor)
class BookAuthorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('first_name', 'last_name', )
    search_fields = ('first_name',)
    readonly_fields = ('pk',)
    list_filter = ('date_of_death',)

@admin.register(BookPublish)
class BookPublishAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'address')
    readonly_fields = ('pk',)


@admin.register(Issue)
class IssueAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('user', 'book', 'date')
    list_filter = ('date',)


@admin.register(Genre)
class GenreAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
