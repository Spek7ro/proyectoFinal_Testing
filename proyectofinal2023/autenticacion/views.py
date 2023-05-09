from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login,logout, authenticate
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

class VRegistro(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "registro/registro.html",{'form':form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
        
        else:
            for msg in form.error_messages:
                messages.error(request,form.error_messages[msg])
            return render(request, "registro/registro.html",{'form':form})


def cerrarSesion(request):
    logout(request)
    return redirect('home')

def loguear(request):
    if request.method=="POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario, password=contraseña)
            if usuario is not None:
                login(request,usuario)
                return redirect('home')
            else:
                messages.error(request, "Usuario no válido")
    else:
        messages.error(request, "Información incorrecta")  
    form = AuthenticationForm()
    return render(request, "login/login.html",{'form':form})
