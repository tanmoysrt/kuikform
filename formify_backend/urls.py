from django.contrib import admin
from django.urls import path, include
from auth_system.views import login_page, register_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_page),
    path('register/', register_page),
    path('dashboard/', include('user_dashboard.urls')),
    path('api/v1/', include('form_process.urls'))
]
