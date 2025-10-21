from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Notification
@login_required
def notification_list(request):
    qs = Notification.objects.filter(recipient=request.user)
    qs.filter(read=False).update(read=True)
    return render(request, 'notifications/list.html', {'notifications': qs})