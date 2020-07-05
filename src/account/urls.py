from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('logout/', views.UserLogoutView.as_view(), name="logout"),
    path('login/', views.UserLoginView.as_view(), name="signin"),
    path('user/<str:username>/', views.UserUpdateView.as_view(), name="update"),

    path('password/', views.UserPasswordChangeView.as_view(), name='password'),
    path('password_change/done/', views.UserPasswordChangeDoneView.as_view(),
         name='password_change_done'),

    path('password_reset/', views.UserPasswordResetView.as_view(),
         name='password_reset'),
    path('password_reset/done/', views.UserPasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.UserPasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/done/', views.UserPasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    path('signup/', views.UserCreateView.as_view(), name="signup"),
]
