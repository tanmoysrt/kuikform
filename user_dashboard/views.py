from django.http import HttpResponse
from django.shortcuts import render, redirect
from auth_system.models import UserProfile
from form_process.models import Form, FormAccess, FormResponse


def dashboard(request):
    data = {
        "title": "Dashboard",
        "list_form_access": FormAccess.objects.filter(user_id=request.user.id).exclude(access_level="read")
    }
    return render(request, "user_dashboard/dashboard.html", data)


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
    form_responses = data["form"].form_responses.all()
    data["form_responses"] = form_responses

    return render(request, "user_dashboard/form_details.html", data)


def form_edit(request, id):
    data = {
        "title": "Form details",
    }
    form = Form.objects.get(id=id)
    if request.method == "POST":
        whitelist_mode = int(request.POST.get("whitelist_mode", 0))
        whitelisted_websites = str(request.POST.get("whitelisted_websites", "")).strip()
        form.whitelist_mode = True if whitelist_mode == 1 else False
        form.whitelist_websites = whitelisted_websites.split(",")
        form.save()
        data["message"] = "Updated Successfully"

    data["form"] = form
    return render(request, "user_dashboard/form_edit.html", data)


def new_form(request):
    data = {
        "title": "New Form",
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
            return redirect("/dashboard/form/" + str(formRecord.id) + "/edit/")
    return render(request, "user_dashboard/form_new.html", data)


def delete_form(request, id):
    data = {
        "title": "Delete Form"
    }
    try:
        form = Form.objects.get(id=id)
        form.delete()
        # TODO later update this with notification callback to redirect route
        data["message"] = "Form Deleted Successfully"
    except:
        data["message"] = "Form Delete Unsuccessful"

    return render(request, "user_dashboard/delete_form_info.html", data)
