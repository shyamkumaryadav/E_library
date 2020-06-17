from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'system'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.aboutView.as_view(), name='about'),
    path('terms/', views.TermsView.as_view(), name='terms'),
    path('view_books/', views.ViewBookView.as_view(),
         name='viewbooks'),
    path('author_management/', views.AuthorManagementView.as_view(),
         name='authormanagement'),
    path('author_management/<uuid:pk>/', views.AuthorManagementUpdateView.as_view(),
         name='authormanagementupdate'),
    path('publisher_management/<uuid:pk>/', views.PublisherManagementUpdateView.as_view(),
         name='publishermanagementupdate'),
    path('member_management/', views.MemberManagementView.as_view(),
         name='membermanagement'),
    path('book_issuing/', views.BookIssuingView.as_view(),
         name='bookissuing'),
    path('book_inventory/', views.BookInventoryView.as_view(),
         name='bookinventory'),
    path('publisher_management/', views.PublisherManagementView.as_view(),
         name='publishermanagement'),
    path('shyamkumaryadav/', views.ShyamkumaryadavView.as_view(),
         name='shyamkumaryadav'),
]
