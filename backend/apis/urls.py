from django.urls import path

from .views import (
    SignupAPIView,
    SigninAPIView,
    DeleteUserView,
    ProjectMixins,
    ProjectDetailMixins
)


urlpatterns = [
    path("users/signup/", SignupAPIView.as_view(), name='signup'),
    path("users/signin/", SigninAPIView.as_view(), name='signin'),
    path("users/<int:pk>/", DeleteUserView.as_view(), name='user-delete'),
    path("projects/", ProjectMixins.as_view(), name='project-c'),
    path('projects/<int:pk>/', ProjectDetailMixins.as_view(), name='project-rud'),
]