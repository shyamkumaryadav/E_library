from django.contrib import admin
from django.utils.translation import ngettext, gettext as _
from django.contrib import messages
from django.db.models import F
from import_export.admin import ImportExportModelAdmin
from .models import Book, Issue, BookAuthor, BookPublish, Genre
import decimal


# ['id', 'name', 'genre', 'author', 'publish', 'publish_date', 'date', 'language', 'edition', 'cost', 'page', 'discription', 'stock',
# 'today_stock', 'rating', 'profile']
@admin.register(Book)
class BookAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('__str__', 'author', 'date', 'stock', 'today_stock')
    fieldsets = (
        (None, {'fields': ('pk', 'name', 'author')}),
        ('Information', {
            'classes': ('collapse',),
            'fields': ('genre', 'publish', 'publish_date', 'language', 'edition', 'cost', 'page', 'description', 'stock', 'today_stock', 'rating', 'profile')}),
    )
    search_fields = ('name',)
    readonly_fields = ('today_stock', 'pk', 'date')
    ordering = ('name',)
    actions = ['apply_discount', ]
    list_filter = ('edition', 'language', 'date')

    def apply_discount(self, request, queryset):
        updated = queryset.update(cost=F('cost') * decimal.Decimal('0.9'))
        self.message_user(request, ngettext(
            '%d book was successfully apply 10%% discount.',
            '%d books were successfully apply 10%% discount.',
            updated,
        ) % updated, messages.SUCCESS)
    apply_discount.short_description = _('Apply 10%% discount')


@admin.register(BookAuthor)
class BookAuthorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('first_name', 'last_name', )
    search_fields = ('first_name',)
    readonly_fields = ('pk',)
    list_filter = ('date_of_death',)


@admin.register(BookPublish)
class BookPublishAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('__str__', 'address')
    readonly_fields = ('pk',)


@admin.register(Issue)
class IssueAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('__str__', 'date', 'due_date',)
    list_filter = ('date',)
    readonly_fields = ('date',)

    # def defaulter(self, obj):
    # defaulter.boolean = True


@admin.register(Genre)
class GenreAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('name',)
