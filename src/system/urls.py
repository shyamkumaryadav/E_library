from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('Books', views.BookView)

app_name = 'system'

urlpatterns = [
    path('bookapi/', include(router.urls)),
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.aboutView.as_view(), name='about'),
    path('terms/', views.TermsView.as_view(), name='terms'),
    path('view-books/', views.ViewBookView.as_view(),
         name='viewbooks'),
    path('author-management/', views.AuthorManagementView.as_view(),
         name='authormanagement'),
    path('author-management/<uuid:pk>/', views.AuthorManagementUpdateView.as_view(),
         name='authormanagementupdate'),
    path('publisher_management/<uuid:pk>/', views.PublisherManagementUpdateView.as_view(),
         name='publishermanagementupdate'),
    path('member-management/', views.MemberManagementView.as_view(),
         name='membermanagement'),
    path('book-issuing/', views.BookIssuingView.as_view(),
         name='bookissuing'),
    path('book-inventory/', views.BookInventoryView.as_view(),
         name='bookinventory'),
    path('book-inventory/<uuid:pk>/', views.BookInventoryUpdateView.as_view(),
         name='bookinventoryupdate'),
    path('publisher-management/', views.PublisherManagementView.as_view(),
         name='publishermanagement'),
    path('shyamkumaryadav/', views.ShyamkumaryadavView.as_view(),
         name='shyamkumaryadav'),
]
