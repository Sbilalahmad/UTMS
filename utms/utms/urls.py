from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from accounts.views import role_redirect   # top of file


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('redirect/', role_redirect, name='role-redirect'),  # <-- add
    path('accounts/', include('accounts.urls')),

    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('core/', include('core.urls')),   # <-- add this
    path('scheduler/', include('scheduler.urls')),

    # dashboard stubs – will be replaced in Step 3 with real views
    path('dashboard/admin/',  TemplateView.as_view(template_name='admin_dashboard.html'),  name='admin_dashboard'),
    path('dashboard/faculty/', TemplateView.as_view(template_name='faculty_dashboard.html'), name='faculty_dashboard'),
    path('dashboard/student/', TemplateView.as_view(template_name='student_dashboard.html'), name='student_dashboard'),
]