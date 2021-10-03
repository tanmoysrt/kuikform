from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from user_dashboard import views


urlpatterns = [
    path("", views.dashboard),
    path("form/<uuid:id>/", views.form_details)
]
