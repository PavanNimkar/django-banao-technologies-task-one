from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("logout", views.logout_view, name="logout"),
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login"),
    path("patient-dashboard/", views.patient_dashboard, name="patient_dashboard"),
    path("doctor-dashboard/", views.doctor_dashboard, name="doctor_dashboard"),
]
