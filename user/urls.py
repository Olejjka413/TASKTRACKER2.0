from .views import DeleteView, RegisterView, LoginView, LogoutView, UserView, UpdateView
from django.urls import path

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("login/", LoginView.as_view()),
    path("logout/", LogoutView.as_view()),
    path("delete/", DeleteView.as_view()),
    path("update/", UpdateView.as_view()),
    path("", UserView.as_view()),
]
