from django.shortcuts import render, redirect  # type: ignore
from django.views.generic import View  # type: ignore
from django.contrib.auth import login, logout, authenticate  # type: ignore
from django.contrib import messages  # type: ignore

from django.contrib.auth.forms import AuthenticationForm  # type: ignore
from .forms import RegistroForm, ReestablecerContraseñaForm

from django.contrib.auth.models import User, Group  # type: ignore
from django.db.models.signals import post_save  # type: ignore


def add_user_to_group(sender, instance, created, **kwargs):
    if created:
        group, created = Group.objects.get(name='Investigadores')
        instance.groups.add(group)
    post_save.connect(add_user_to_group, sender=User)


class VRegistro(View):
    def get(self, request):
        form = RegistroForm()
        form.fields['username'].widget.attrs['placeholder'] = \
            'Nombre de usuario'
        form.fields['password1'].widget.attrs['placeholder'] = 'Contraseña'
        form.fields['password2'].widget.attrs['placeholder'] = \
            'Confirmar contraseña'
        form.fields['first_name'].widget.attrs['placeholder'] = 'Nombre(s)'
        form.fields['last_name'].widget.attrs['placeholder'] = 'Apellido(s)'
        form.fields['email'].widget.attrs['placeholder'] = 'Correo Electrónico'

        form.fields['username'].widget.attrs['class'] = \
            'form-control form-control-user'
        form.fields['password1'].widget.attrs['class'] = \
            'form-control form-control-user'
        form.fields['password2'].widget.attrs['class'] = \
            'form-control form-control-user'
        form.fields['first_name'].widget.attrs['class'] = \
            'form-control form-control-user'
        form.fields['last_name'].widget.attrs['class'] = \
            'form-control form-control-user'
        form.fields['email'].widget.attrs['class'] = \
            'form-control form-control-user'
        return render(request, "registro/registro.html", {'form': form})

    def post(self, request):
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, "registro/registro.html", {'form': form})


def cerrarSesion(request):
    logout(request)
    return redirect('iniciar_sesion')


def error404(request):
    logout(request)
    return render(request, "404.html")


def loguear(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")
            usuario = authenticate(
                username=nombre_usuario, password=contraseña)
            if usuario is not None:
                login(request, usuario)
                return redirect('home')
            else:
                # No muestra los mensajes
                messages.error(request, "Usuario no válido")
    else:
        messages.error(request, "Información incorrecta")
    form = AuthenticationForm()
    # Agregar placeholder al campo de nombre de usuario
    form.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
    # Agregar placeholder al campo de contraseña
    form.fields['password'].widget.attrs['placeholder'] = 'Contraseña'

    # Agregar clase al campo de nombre de usuario
    form.fields['username'].widget.attrs['class'] = \
        'form-control form-control-user'
    # Agregar clase al campo de contraseña
    form.fields['password'].widget.attrs['class'] = \
        'form-control form-control-user'
    return render(request, "login/login.html", {'form': form})


def reestablecer_contraseña(request):
    if request.method == "POST":
        form = ReestablecerContraseñaForm(request.POST)
        if form.is_valid():
            correo = form.cleaned_data.get("email")
            try:
                usuario = User.objects.get(email=correo)
                nueva_contraseña = form.cleaned_data.get("password1")
                usuario.set_password(nueva_contraseña)
                usuario.save()
                return redirect('iniciar_sesion')  # Redirigir en caso de éxito
            except User.DoesNotExist:
                messages.error(request, "Correo no existente")
                return redirect('reestablecer_contra')  # Redirigir en caso de correo no existente
        else:
            # Redirigir si el formulario no es válido
            return redirect('reestablecer_contra')
    else:
        form = ReestablecerContraseñaForm()
    return render(request, "registro/reestablecer.html", {'form': form})
