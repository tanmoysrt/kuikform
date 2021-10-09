from django.http import HttpResponse
from django.shortcuts import render, redirect
from auth_system.models import UserProfile
from form_process.models import Form, FormAccess, FormResponse
from kuikform_backend.login_gateway import login_check_redirection_gateway


def landing_page(request):
    return render(request, "user_dashboard/landing.html")


@login_check_redirection_gateway
def dashboard(request):
    data = {
        "title": "Dashboard",
        "page": "dashboard",
        "total_forms_count": FormAccess.objects.filter(user_id=request.user.id).exclude(access_level="read").count(),
        "active_forms_count": FormAccess.objects.filter(user_id=request.user.id, form__is_active=True).exclude(
            access_level="read").count(),
        "total_responses_count": FormResponse.objects.filter(form__form_accesses__user_id=request.user.id).count()
    }

    return render(request, "user_dashboard/dashboard.html", data)


@login_check_redirection_gateway
def all_forms(request):
    data = {
        "title": "All Forms",
        "page": "all_forms",
        "list_form_access": FormAccess.objects.filter(user_id=request.user.id).exclude(access_level="read")
    }
    return render(request, "user_dashboard/allforms.html", data)


@login_check_redirection_gateway
def form_details(request, id):
    # TODO check permission and form existance
    data = {
        "title": "Form details",
    }

    if "d" in request.GET:
        try:
            responseId = request.GET["d"]
            FormResponse.objects.get(id=responseId).delete()
            print("Deleted Successfully")
        except:
            print("Delete Failed")

    form = Form.objects.get(id=id)

    data["form"] = form
    form_responses = form.form_responses.all().order_by("-id")
    data["form_responses"] = form_responses

    return render(request, "user_dashboard/form_details.html", data)


@login_check_redirection_gateway
def form_edit(request, id):
    data = {
        "title": "Edit Form",
    }
    form = Form.objects.get(id=id)
    if request.method == "POST":
        whitelist_mode = int(request.POST.get("whitelist_mode", 0))
        form_status = int(request.POST.get("form_status", 0))
        whitelisted_websites = str(request.POST.get("whitelisted_websites", "")).strip()
        form.whitelist_mode = True if whitelist_mode == 1 else False
        form.is_active = True if form_status == 1 else False
        form.whitelist_websites = whitelisted_websites.split(",")
        form.save()
        data["message"] = "Updated Successfully"

    data["form"] = form
    return render(request, "user_dashboard/form_edit.html", data)


@login_check_redirection_gateway
def new_form(request):
    data = {
        "title": "New Form",
        "page": "create_form",
    }
    if request.method == "POST":
        title = str(request.POST.get("title", "")).strip()
        if title == "":
            data["message"] = "Please specify a title for your form"
        else:
            formRecord = Form.objects.create(title=title)
            FormAccess.objects.create(
                user=request.user,
                form=formRecord,
                access_level="admin"
            )
            return redirect("/dashboard/form/" + str(formRecord.id) + "/edit/#addToWebsiteCodeSnippet")
    return render(request, "user_dashboard/form_new.html", data)


@login_check_redirection_gateway
def delete_form(request, id):
    message = ""
    successful = 0
    try:
        form = Form.objects.get(id=id)
        form.delete()
        # TODO later update this with notification callback to redirect route
        message = "Form Deleted Successfully"
        successful = 1
    except:
        message = "Form Delete Unsuccessful"

    return redirect("/dashboard/?m=" + message + "&t=" + str(successful))


def handler404(request, exception):
    return render(request, "user_dashboard/404page.html", status=404)
