from django.urls import path
from user_dashboard import views


urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("forms/", views.all_forms, name="all_forms"),
    path("createform/", views.new_form, name="create_form"),
    path("form/<uuid:id>/", views.form_details, name="view_form_response"),
    path("form/<uuid:id>/edit/", views.form_edit, name="edit_form"),
    path("form/<uuid:id>/delete/", views.delete_form, name="delete_form"),
]
