from django.contrib.auth import views as auth_views
from django.shortcuts import redirect

from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from .forms import CrispyAuthenticationForm, CrispyPasswordChangeForm
class LoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'
    form_class = CrispyAuthenticationForm
class LogoutView(auth_views.LogoutView):
    next_page = 'accounts:login'
class PasswordChangeView(auth_views.PasswordChangeView):
    template_name = 'accounts/password_change.html'
    form_class = CrispyPasswordChangeForm
    success_url = reverse_lazy('home')


def role_redirect(request):
    """
    After login, bounce user to the right dashboard.
    """
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    role = request.user.role
    if role == 'admin':
        return redirect('admin_dashboard')
    elif role == 'faculty':
        return redirect('faculty_dashboard')
    else:  # student
        return redirect('student_dashboard')