from django.urls import path

from .views import (
    SignupAPIView,
    SigninAPIView,
    DeleteUserView
)

urlpatterns = [
    path("users/signup/", SignupAPIView.as_view()),
    path("users/signin/", SigninAPIView.as_view()),
    path("users/<int:pk>/", DeleteUserView.as_view()),
]