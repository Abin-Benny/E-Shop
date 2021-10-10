from django.shortcuts import render,redirect
from .forms import UserForm
from django.contrib.auth import authenticate, login,logout

# Create your views here.
def user_register(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        else:
            form = UserForm()
        return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request,username=username, password=password)

            if user is not None:
                login(request,user)
                return redirect("index")
            else:
                return render(request, "login.html",{'msg':"Invalid Credentials"})
        return render(request,"login.html")


def user_logout(request):
    logout(request)
    return redirect("login")



