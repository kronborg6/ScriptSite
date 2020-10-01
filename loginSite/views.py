from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('Site-Home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('Site-Home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'loginSite/loginSite.html', context)


@login_required
def logoutUser(request):
    logout(request)
    messages.success(request, 'You have ben Logout! have a nice day')
    return redirect('loginS')
