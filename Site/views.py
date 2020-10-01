from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'Site/home.html', {'title': 'Home'})

@login_required
def Guides(request):
    return render(request, 'Site/Guides.html', {'title': 'Guides'})

@login_required
def Scripts(request):
    return render(request, 'Site/Scripts.html', {'title': 'Scripts'})

@login_required
def test(request):
    if request.user.is_superuser:
        return render(request, 'Site/test.html', {'title': 'Test'})
    else:
        return redirect('Site-Home')
