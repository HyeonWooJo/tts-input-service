from django.urls import path

from .views import (
    SignupAPIView,
    SigninAPIView,
    DeleteUserView,
    ProjectMixins,
    ProjectDetailMixins
)


urlpatterns = [
    path("users/signup/", SignupAPIView.as_view()),
    path("users/signin/", SigninAPIView.as_view()),
    path("users/<int:pk>/", DeleteUserView.as_view()),
    path("projects/", ProjectMixins.as_view()),
    path('projects/<int:pk>/', ProjectDetailMixins.as_view()),
]