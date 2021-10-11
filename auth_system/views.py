import random
import string

from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from auth_system.models import UserProfile, ResetLinkDirectory, VerifyMailLinkDirectory
from kuikform_backend.settings import DASHBOARD_LINK, USER_LOGIN_REDIRECT_URL, MAIN_ENDPOINT, MAIN_PROTOCOL
from kuikform_backend.utils import send_reset_mail, send_verification_link_mail


def login_page(request):
    if request.user.is_authenticated:
        return redirect(DASHBOARD_LINK)
    data = {}
    if request.method == "POST":
        action = request.POST.get("action", "")
        if action == "login":
            email = request.POST.get("email", "")
            password = request.POST.get("password", "")

            if email == "" and password == "":
                data[
                    "message"] = '<div class="alert alert-danger text-white" role="alert">Email and password can\'t be blank</div>'
            else:
                user = authenticate(email=email, password=password)
                if user is None:
                    data[
                        "message"] = '<div class="alert alert-danger text-white" role="alert">Email or password is wrong</div>'
                else:
                    login(request, user)
                    return redirect(DASHBOARD_LINK)
        elif action == "reset_pass":
            reset_mail = request.POST.get("reset_mail", "")
            if not UserProfile.objects.filter(email=reset_mail).exists():
                data[
                    "message"] = '<div class="alert alert-danger text-white" role="alert">Email Id is not registered</div>'
            else:
                uniqueKey = ''.join(random.choices(string.ascii_lowercase + string.digits, k=80))

                user = UserProfile.objects.get(email=reset_mail)
                record = ResetLinkDirectory.objects.create(
                    user=user,
                    verification_key=uniqueKey
                )
                send_reset_mail(user.first_name + " " + user.last_name, user.email,
                                f"{MAIN_PROTOCOL}{MAIN_ENDPOINT}/reset/?i={str(record.id)}&k={record.verification_key}")
                data["message"] = '<div class="alert alert-success text-white" role="alert">Reset link has been sent ' \
                                  'to mail id</div> '

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
            user.save()
            data["message"] = "Account created successfully"
            login(request, user)
            record = VerifyMailLinkDirectory.objects.create(
                user=request.user,
                verification_key=''.join(random.choices(string.ascii_lowercase + string.digits, k=80))
            )
            send_verification_link_mail(request.user.first_name + " " + request.user.last_name, request.user.email,
                                        f"{MAIN_PROTOCOL}{MAIN_ENDPOINT}/verifymail/?i={str(record.id)}&k={record.verification_key}")
            return redirect(DASHBOARD_LINK)

    return render(request, "auth_system/register.html", data)


def logout_user(request):
    logout(request)
    return redirect(USER_LOGIN_REDIRECT_URL)


def reset_link_verify(request):
    data = {}
    showForm = True
    resetid = request.GET.get("i", "");
    key = request.GET.get("k", "")

    try:
        record = ResetLinkDirectory.objects.get(id=resetid, verification_key=key)
        if request.method == "POST":
            password = request.POST.get("password", "")
            user = record.user
            user.set_password(password)
            record.delete()
            user.save()
            showForm = False
            return redirect("/login/")
    except:
        showForm = False
        data["message"] = "Invalid Link"
    data["showForm"] = showForm
    return render(request, "auth_system/reset_pass_verify.html", data)


def verify_mail_details_page(request):
    if request.user.verified:
        return redirect("/dashboard/")

    resend = int(request.GET.get("resend", 0))
    resend = 0
    if resend == 1:
        record = VerifyMailLinkDirectory.objects.create(
            user=request.user,
            verification_key=''.join(random.choices(string.ascii_lowercase + string.digits, k=80))
        )
        send_verification_link_mail(request.user.first_name + " " + request.user.last_name, request.user.email,
                                    f"{MAIN_PROTOCOL}{MAIN_ENDPOINT}/verifymail/?i={str(record.id)}&k={record.verification_key}")

    return render(request, "auth_system/verify_mail.html")


def verify_mail_id(request):
    data = {}
    recordid = request.GET.get("i", "");
    key = request.GET.get("k", "")
    successVerified = False

    try:
        record = VerifyMailLinkDirectory.objects.get(id=recordid, verification_key=key)
        user = record.user
        user.verified = True
        user.save()
        record.delete()
        successVerified = True
    except:
        successVerified = False
    data["verified"] = successVerified
    return render(request, "auth_system/verify_mail_confirmation.html", data)
