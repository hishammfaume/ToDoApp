from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("register/", views.landing_view, name="register"),
    path("login/", views.landing_view, name="login"),
    path('logout/', views.logout_view, name='logout'),
   # path('logout/', auth_views.LogoutView.as_view(next_page='landing-page'), name = 'logout')
]
