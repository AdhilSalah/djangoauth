
from email import message
from multiprocessing import context
from pyexpat.errors import messages
from unicodedata import name

from django.shortcuts import redirect, render

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.models import User

from auth1.models import User_data
from django.views.decorators.cache import never_cache

# Create your views here.


def home(request):
    if request.user.is_authenticated:
        return redirect('user_home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_superuser:
                messages.info(request, "incorrect password")
            else:

                login(request, user)
                return redirect('user_home')
        else:
            messages.info(request, "incorrect password")
            return redirect(home)

    return render(request, 'signin.html')


# signuphere


def signup(request):
    if request.user.is_authenticated:
        return redirect('user_home')

    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['pass1']
        pass2 = request.POST['pass2']

        if username == "":
            messages.info(request, "cant leave field empty")
            return redirect('signup')

        if password == pass2:

            if User.objects.filter(username=username).exists():

                messages.info(request, "username exist")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email exists")
            else:
                user = User.objects.create_user(
                    username=username, password=password, email=email)

                user.save()
                messages.info(request, "sucess")
                return redirect('home')
        else:
            messages.info(request, "password not same")

    return render(request, 'signup.html')


# userhomehre
@never_cache
def user_home(request):

    if request.user.is_authenticated:

        return render(request, 'user_home.html')

    return redirect('home')


# signouthere
def signout(request):

    if request.user.is_authenticated:
        logout(request)

    return redirect('home')


# adminhere

@never_cache
def adminpro(request):

    if request.user.is_authenticated:

        details = User.objects.all()

        return render(request, 'adminpro.html', {'details': details})

    return redirect('adminprologin')


# admindeletehere




def adminprologin(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_superuser:
                login(request, user)

                return redirect('adminpro')

            else:
                messages.info(request, "you are not an admin")

        else:
            messages.info(request, "incroect credentails")

    return render(request, 'adminprologin.html')


def fundelete(request, pk):
    User.objects.filter(id=pk).delete()
    User.objects.all()

    return redirect('adminpro')


# admidataupdation
def funcupdate(request, pk):
    user = User.objects.get(id=pk)
    details = User.objects.all()
    context = {
        'details': details,

        'user': user

    }

    if request.method == 'POST':

        usernameup = request.POST['username']
        emailup = request.POST['email']
        if usernameup == "" or emailup == "":
            messages.info(request, "cannot be null")
        else:
            user.username = usernameup
            user.email = emailup
            user.save()
            return render(request, 'adminpro.html', context)

    return render(request, 'confirmupdate.html',)


def adduser(request):
    if request.method == "POST":

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():

            messages.info(request, "useranme exist")
        elif User.objects.filter(email=email).exists():
            messages.info(request, "eamilexist")

        else:
            user = User.objects.create_user(
                username=username, email=email, password=password)
            user.save()
            messages.info(request, "user added")
            return redirect('adminpro')
    return redirect('adminpro')


# adminlogout
def adminprologout(request):

    
    if request.user.is_authenticated:
        logout(request)

    return redirect('adminprologin')


def search(request):
    if request.method == "POST":
        username = request.POST['search']
        if User.objects.filter(username=username).exists():

            messages.info(request, "user found")

            return redirect('adminpro')
        else:
            messages.info(request, "not found")
            return redirect('adminpro')

    else:
        return redirect('adminpro')
