from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from user_dashboard import views


urlpatterns = [
    path("", views.dashboard),
    path("createform/", views.new_form),
    path("form/<uuid:id>/", views.form_details),
    path("form/<uuid:id>/edit/", views.form_edit),
    path("form/<uuid:id>/delete/", views.delete_form),
]
