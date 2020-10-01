from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def HomeOnlineScripts(request):
    if request.user.is_superuser:
        return render(request, 'OnlineScripts/OnlineScripts.html', {'title': 'Online Scripts'})
    else:
        return redirect('Site-Home')