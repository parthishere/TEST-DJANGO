from django.contrib.auth import (login,
                                 authenticate,
                                 logout,
                                 get_user_model
                                 )
from django.shortcuts import (render,
                              HttpResponseRedirect,
                              redirect,
                              reverse,)
from .forms import UserProfileInfoForm, UserRegister
from django.contrib.auth.decorators import login_required

User = get_user_model()


def login_user(request):
    form = UserProfileInfoForm(request.POST or None)
    context = {
        'form': form
    }
    if request.POST:
        if form.is_valid():
            name = form.cleaned_data.get('name')
            # email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
         #    phone_num = form.cleaned_data.get('phone_num')

            user = authenticate(request, username=name, password=password)
            if user is not None:
                login(request, user)
                form = UserProfileInfoForm(request.POST or None)
                return redirect('profile')
            else:
                print("User not found")
    else:
        form = UserProfileInfoForm(request.POST or None)
    return render(request, 'guvi/login.html', context)


def register_user(request):
    form = UserRegister(request.POST or None)
    context = {
        'form': form
    }
    if request.POST:
        if form.is_valid():
            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            User = authenticate(request, username=name,
                                password=password)
            print(User)
            if User is None:
                new_user = User.objects.create_user(
                    username=name, email=email, password=password)
                new_user.save()
                return redirect('profile')
    return render(request, 'guvi/register.html', context)


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


@login_required(login_url="login-user")
def profile(request):
    return render(request, "guvi/profile.html", {})
