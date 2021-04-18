from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'system'

urlpatterns = [
     path('', views.HomeView.as_view(), name='home'),
     path('privacy/', views.privacyView.as_view(), name='privacy'),
     path('terms/', views.TermsView.as_view(), name='terms'),
     
     # Author LIST UPDATE DELETE
     path('author-management/', views.AuthorManagementView.as_view(),
          name='authormanagement'),
     path('author-management/<uuid:pk>/', views.AuthorManagementUpdateView.as_view(),
          name='authormanagementupdate'),
     path('author-management/<uuid:pk>/delete/', views.AuthorManagementDeleteView.as_view(),
          name='authormanagementdelete'),
     # Publisher LIST UPDATE DELETE
     path('publisher-management/', views.PublisherManagementView.as_view(),
          name='publishermanagement'),
     path('publisher-management/<uuid:pk>/', views.PublisherManagementUpdateView.as_view(),
          name='publishermanagementupdate'),
     path('publisher-management/<uuid:pk>/delete/', views.PublisherManagementDeleteView.as_view(),
         name='publishermanagementdelete'),
     # Member  LIST UPDATE DELETE
     path('member-management/', views.MemberManagementView.as_view(),
          name='membermanagement'),
     path('member-management/<uuid:pk>/delete/', views.MemberManagementDeleteView.as_view(),
          name='membermanagementdelete'),
     # Book Issue LIST UPDATE DELETE
     path('book-issuing/', views.BookIssuingView.as_view(),
          name='bookissuing'),
     path('book-issuing/<pk>/', views.BookIssuingUpdateView.as_view(),
          name='bookissuingupdate'),
     path('book-issuing/<pk>/delete/', views.BookIssuingDeleteView.as_view(),
          name='bookissuingdelete'),
     # Book LIST UPDATE DELETE
     path('view-books/', views.ViewBookView.as_view(),
          name='viewbooks'),
     path('book-inventory/', views.BookInventoryView.as_view(),
          name='bookinventory'),
     path('view-books/<pk>/', views.BookInventoryDetailView.as_view(),
          name='bookinventorydetail'),
     path('book-inventory/<uuid:pk>/', views.BookInventoryUpdateView.as_view(),
          name='bookinventoryupdate'),
     path('book-inventory/<uuid:pk>/delete/', views.BookInventoryDeleteView.as_view(),
          name='bookinventorydelete'),
     
     path('shyamkumaryadav/', views.ShyamkumaryadavView.as_view(),
          name='shyamkumaryadav'),
]
