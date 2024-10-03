from django.urls import path

from . import views

urlpatterns = [
    path("register/", views.landing_view, name="register"),
    path("login/", views.landing_view, name="login"),
]
