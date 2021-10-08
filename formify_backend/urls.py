from django.contrib import admin
from django.urls import path, include
from auth_system.views import login_page, register_page, logout_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_page, name="user_login_page"),
    path('logout/', logout_user, name="user_logout_route"),
    path('register/', register_page, name="user_registration_page"),
    path('dashboard/', include('user_dashboard.urls'), name="user_dashboard"),
    path('api/v1/', include('form_process.urls'))
]

handler404 = "user_dashboard.views.handler404"