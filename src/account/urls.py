from django.urls import path
from django.utils.translation import gettext_lazy as _
from . import views

app_name = 'account'
urlpatterns = [
     path('logout/', views.UserLogoutView.as_view(), name="logout"),
     path('login/', views.UserLoginView.as_view(), name="signin"),
     path('signup/', views.UserCreateView.as_view(), name="signup"),
     path('user/<str:username>/', views.UserUpdateView.as_view(), name="update"),

     path('password/', views.UserPasswordChangeView.as_view(), name='password'),
     path('password-reset/', views.UserPasswordResetView.as_view(),
          name='password_reset'),
     path('reset/<uidb64>/<token>/', views.UserPasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
     path('email/<uid>/<token>/', views.UserEmailVerified.as_view(),
         name='email_confirm'),
]
