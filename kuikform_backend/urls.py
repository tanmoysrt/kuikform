from django.contrib import admin
from django.urls import path, include
from auth_system.views import login_page, register_page, logout_user, reset_link_verify,verify_mail_details_page, verify_mail_id
from user_dashboard.views import landing_page

urlpatterns = [
    path('',landing_page, name="landing_page"),
    path('admin/', admin.site.urls),
    path('login/', login_page, name="user_login_page"),
    path('logout/', logout_user, name="user_logout_route"),
    path('register/', register_page, name="user_registration_page"),
    path('reset/', reset_link_verify, name="reset_link_verify_route"),
    path('verifymailplease/',verify_mail_details_page),
    path('verifymail/',verify_mail_id),
    path('dashboard/', include('user_dashboard.urls'), name="user_dashboard"),
    path('api/v1/', include('form_process.urls'))
]

handler404 = "user_dashboard.views.handler404"