from django.urls import path

from .views import (
    SignupAPIView,
    SigninAPIView,
    DeleteUserView,
    ProjectMixins
)


urlpatterns = [
    path("users/signup/", SignupAPIView.as_view()),
    path("users/signin/", SigninAPIView.as_view()),
    path("users/<int:pk>/", DeleteUserView.as_view()),
    path("projects/", ProjectMixins.as_view()),
]