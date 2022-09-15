import email
from email import message
from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Users

# Create your views here.

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if Users.objects.filter(username=username):
            messages.error(request, "Nom déja existant")
            return redirect('register')

        if Users.objects.filter(email=email):
            messages.error(request, "Compte existe déja !")
            return redirect('register')

        if not username.isalnum():
            messages.error(request, 'Entrer un nom valide.')
            return redirect('register')

        if password1 != password2:
            messages.error(request, 'Ooops! Les deux mots de passe doivent être identiques')
            return redirect('register')


        mon_utilisateur = Users.objects.create_user(username, email, password1)
        mon_utilisateur.first_name = firstname
        mon_utilisateur.last_name = lastname
        mon_utilisateur.save()
        messages.success(request, 'Votre compte a été crée avec success')
        return redirect('login')

    return render(request, 'accounts/register.html')

def logIn(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)

            if user.is_professeur:
                return redirect('professeur')
            else:
                return render(request, 'face/index.html')
        else:
            messages.error(request, 'Mauvaise authentification')
            return redirect('login')

    return render(request, 'accounts/login.html')


def logOut(request):
    logout(request)
    messages.success(request, 'Vous éte déconnecté')
    return redirect('index')

def professeur(request):
    return render(request, 'accounts/professeur.html')
