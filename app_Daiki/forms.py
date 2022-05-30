from dataclasses import fields
import email
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MangaFormulario(forms.Form):
    nombre = forms.CharField()
    genero = forms.CharField()
    autor = forms.CharField()
    anio_lanzamiento = forms.IntegerField()
    cantidad_tomos = forms.IntegerField()

class AnimeFormulario(forms.Form):
    nombre = forms.CharField()
    estado_emision = forms.CharField()
    estudio = forms.CharField()
    temporadas = forms.IntegerField()

class PeliculaFormulario(forms.Form):
    nombre = forms.CharField()
    estudio = forms.CharField()
    fecha_estreno = forms.DateField()
    duracion = forms.IntegerField()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la constraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

