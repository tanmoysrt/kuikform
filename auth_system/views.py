from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from auth_system.models import UserProfile
from kuikform_backend.settings import DASHBOARD_LINK, USER_LOGIN_REDIRECT_URL


def login_page(request):
    if request.user.is_authenticated:
        return redirect(DASHBOARD_LINK)
    data = {}
    if request.method == "POST":
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")

        if email == "" and password == "":
            data["message"] = "Email and password can't be blank"
        else:
            user = authenticate(email=email, password=password)
            if user is None:
                data["message"] = "Email or password is wrong"
            else:
                login(request, user)
                return redirect(DASHBOARD_LINK)

    return render(request, "auth_system/login.html", data)


def register_page(request):
    if request.user.is_authenticated:
        return redirect(DASHBOARD_LINK)
    data = {}
    if request.method == "POST":
        first_name = request.POST.get("first_name", "")
        last_name = request.POST.get("last_name", "")
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")

        if email == "" and password == "" and first_name == "" and last_name == "":
            data["message"] = "Email and password can't be blank"
        elif UserProfile.objects.filter(email=email).exists():
            data["message"] = "Email Id already exists"
        else:
            user = UserProfile.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email
            )
            user.set_password(password)
            user.save()
            data["message"] = "Account created successfully"
            login(request,user)
            return redirect(DASHBOARD_LINK)

    return render(request, "auth_system/register.html", data)


def logout_user(request):
    logout(request)
    return redirect(USER_LOGIN_REDIRECT_URL)
