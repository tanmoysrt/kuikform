from django.contrib.auth import login, authenticate
from django.shortcuts import render
from auth_system.models import UserProfile


def login_page(request):
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
    return render(request, "auth_system/login.html", data)


def register_page(request):
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

    return render(request, "auth_system/register.html", data)
