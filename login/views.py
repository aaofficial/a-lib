from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='admin').exists():
            return redirect('select')
        else:
            return redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        remember_me = request.POST.get('remember_me', False)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)

                # Set the session expiry duration
                if remember_me:
                    request.session.set_expiry(settings.SESSION_COOKIE_AGE)
                else:
                    request.session.set_expiry(0)

                if user.groups.filter(name='admin').exists():
                    return redirect('select')
                else:
                    return redirect('home')
            else:
                return render(request, 'login.html', {'error': 'حساب کاربری غیرفعال است'})
        else:
            return render(request, 'login.html', {'error': 'اطلاعات ورودی اشتباه است'})
    else:
        return render(request, 'login.html')




def logout_view(request):
    logout(request)
    return redirect('login')


# def select_view(request):
#     return render(request, 'select.html')

@login_required
def select_view(request):
    user = request.user
    if user.groups.filter(name='admin').exists():
        return render(request, 'select.html')
    else:
        return redirect('login')
    

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             if user.groups.filter(name='admin').exists():
#                 return redirect('dashboard')  # هدایت به صفحه داشبورد برای ادمین‌ها
#             else:
#                 return redirect('home')  # هدایت به صفحه خانه برای سایر کاربران
#         else:
#             return render(request, 'login.html', {'error': 'اطلاعات ورودی اشتباه است'})
#     else:
#         return render(request, 'login.html')