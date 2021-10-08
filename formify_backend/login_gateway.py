from django.shortcuts import redirect
from functools import wraps
from formify_backend.settings import USER_LOGIN_REDIRECT_URL


def login_check_redirection_gateway(view_func):
    @wraps(view_func)
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)

        return redirect(USER_LOGIN_REDIRECT_URL)

    return wrap
