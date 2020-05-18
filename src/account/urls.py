from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('logout/', views.UserLogoutView.as_view(), name="logout"),
    path('login/', views.UserLoginView.as_view(), name="login"),
    path('signup/', views.UserCreateView.as_view(), name="signup"),
]
