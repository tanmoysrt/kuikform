from django.http import HttpResponse
from django.shortcuts import render
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
        "form": Form.objects.get(id=id)
    }

    form_responses = data["form"].form_responses.all()

    data["form_responses"] = form_responses

    return render(request, "user_dashboard/form_details.html", data)
