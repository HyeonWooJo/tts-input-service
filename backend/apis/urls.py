from django.urls import path

from .views import (
    SignupAPIView
)

urlpatterns = [
    path("signup/", SignupAPIView.as_view()),
    # path("signin/", SignInView.as_view()),
    # path("delete/<int:pk>", DeleteUserView.as_view()),
]