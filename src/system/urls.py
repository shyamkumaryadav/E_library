from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'system'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('terms/', views.terms, name='terms'),
    path('view_books/', views.ViewBookView.as_view(), name='viewbooks'),
    path('admin_author_management/', views.adminauthormanagement,
         name='adminauthormanagement'),
    path('admin_member_management/', views.adminmembermanagement,
         name='adminmembermanagement'),
    path('admin_book_issuing/', views.adminbookissuing, name='adminbookissuing'),
    path('admin_book_inventory/', views.adminbookinventory,
         name='adminbookinventory'),
    path('admin_publisher_management/', views.adminpublishermanagement,
         name='adminpublishermanagement'),
    path('shyamkumaryadav/', views.shyamkumaryadav, name='shyamkumaryadav'),
]
