from django.urls import path
from . import views

app_name = "account"


urlpatterns = [
    path("", views.HomepageView.as_view(), name="homepage_view"),
    path("registration/", views.RegistrationView.as_view(), name="registration_view"),
    path("login/", views.LoginView.as_view(), name="login_view"),
    path("dashboard/", views.DashboardView.as_view(), name="dashboard_view"),
]
