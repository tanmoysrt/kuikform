from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from form_process import views

urlpatterns = [
    path("submit/", views.FormSubmission)
]
