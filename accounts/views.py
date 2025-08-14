# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import CustomUser


def home_view(request):
    return render(request, "home.html")


def signup_view(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        user_type = request.POST.get("user_type")
        address_line1 = request.POST.get("address_line1")
        city = request.POST.get("city")
        state = request.POST.get("state")
        pincode = request.POST.get("pincode")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        profile_picture = request.FILES.get("profile_picture")

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return render(request, "signup.html")
        elif CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        elif CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
        else:

            CustomUser.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                user_type=user_type,
                address_line1=address_line1,
                city=city,
                state=state,
                pincode=pincode,
                password=password,
                profile_picture=profile_picture,
            )
            messages.success(request, "Account created successfully!")
        return redirect("login")

    return render(request, "signup.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if user.user_type == "patient":
                messages.success(
                    request, f"Welcome back to Patient Dashboard, {user.first_name}!"
                )
                return redirect("patient_dashboard")
            elif user.user_type == "doctor":
                messages.success(
                    request, f"Welcome back to Doctor Dashboard, {user.first_name}!"
                )
                return redirect("doctor_dashboard")
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, "login.html")
    return render(request, "login.html")


def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("login")


@login_required
def patient_dashboard(request):
    return render(request, "patient_dashboard.html", {"user": request.user})


@login_required
def doctor_dashboard(request):
    return render(request, "doctor_dashboard.html", {"user": request.user})
