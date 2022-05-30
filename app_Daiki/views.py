from distutils.log import info
from django.http import HttpResponse
from django.shortcuts import render
import app_Daiki
from app_Daiki.models import Manga, Anime, Pelicula
from app_Daiki.forms import UserRegisterForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import login, authenticate


# Create your views here.

#Formulario de registro

def register(request):

    if request.method == 'POST':

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request, "app_Daiki/inicio.html", {"mensaje": "Usuario creado exitosamente :D"})

    else:

        form = UserRegisterForm()

    return render(request, "app_Daiki/registro.html", {"form":form})

#Login

def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            usuario=form.cleaned_data.get('username')
            contrasena=form.cleaned_data.get('password')

            user=authenticate(username=usuario, password=contrasena)

            if user:

                login(request, user) #el usuario hace login

                return render(request, "app_Daiki/inicio.html", {'mensaje': f"Bienvenido {user}"})
            
        else: #si el usuario no es válido o no se encuentra registrado

            return render(request, "app_Daiki/inicio.html", {'mensaje': "Error. Los datos ingresados son incorrectos"})
    else:

        form = AuthenticationForm()

    return render(request, "app_Daiki/login.html", {'form':form})

#Editar usuarios

def editarUsuario(request):

    usuario = request.user

    if request.method == 'POST':

        editFormUser = UserRegisterForm(request.POST)

        if editFormUser.is_valid():

            informacion = editFormUser.cleaned_data

            usuario.username = informacion['username']
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password1']
            usuario.save()

            return render(request, "app_Daiki/inicio.html")

    else:

        editFormUser = UserRegisterForm(initial={'username':usuario.username, 'email':usuario.email})

    return render(request, "app_Daiki/editarUsuario.html", {'editFormUser':editFormUser, 'usuario':usuario.username})


#View Inicio
def inicio(request):

    return render(request, "app_Daiki/inicio.html")

#View Acerca de mi
def acercademi(request):

    return render(request, "app_Daiki/acercademi.html")

#Búsqueda Mangas:

def busquedaMangas(request):
        
    return render(request, "app_Daiki/busquedaManga.html")

def buscar(request):

    if request.GET["genero"]:

        genero = request.GET["genero"]
        mangas = Manga.objects.filter(genero__icontains=genero)

        return render(request, "app_Daiki/buscar.html", {"mangas":mangas, "genero":genero})
        
    else:

        respuesta = "No se han ingresado los datos"

    return HttpResponse(respuesta)

#CRUD Mangas:

class MangaList(ListView):

    model = Manga
    template_name = "app_Daiki/baseMangas.html"

class MangaDetalle(DetailView):

    model = Manga
    template_name = "app_Daiki/detalleMangas.html"

class MangaCrear(LoginRequiredMixin, CreateView):

    model = Manga
    success_url = "/app_Daiki/manga/baseMangas"
    fields = ['nombre', 'genero', 'autor', 'anio_lanzamiento', 'cantidad_tomos']

class MangaUpdate(LoginRequiredMixin, UpdateView):

    model = Manga
    success_url = "/app_Daiki/manga/baseMangas"
    fields = ['nombre', 'genero', 'autor', 'anio_lanzamiento', 'cantidad_tomos']

class MangaDelete(LoginRequiredMixin, DeleteView):

    model = Manga
    success_url = "/app_Daiki/manga/baseMangas"


#CRUD Animes:

class AnimeList(ListView):

    model = Anime
    template_name = "app_Daiki/baseAnimes.html"

class AnimeDetalle(DetailView):

    model = Anime
    template_name = "app_Daiki/detalleAnimes.html"

class AnimeCrear(LoginRequiredMixin, CreateView):

    model = Anime
    success_url = "/app_Daiki/anime/baseAnime"
    fields = ['nombre', 'estado_emision', 'estudio', 'temporadas']

class AnimeUpdate(LoginRequiredMixin, UpdateView):

    model = Anime
    success_url = "/app_Daiki/anime/baseAnimes"
    fields = ['nombre', 'estado_emision', 'estudio', 'temporadas']

class AnimeDelete(LoginRequiredMixin, DeleteView):

    model = Anime
    success_url = "/app_Daiki/anime/baseAnimes"


#CRUD Películas:

class PeliculaList(ListView):

    model = Pelicula
    template_name = "app_Daiki/basePeliculas.html"

class PeliculaDetalle(DetailView):

    model = Pelicula
    template_name = "app_Daiki/detallePeliculas.html"

class PeliculaCrear(LoginRequiredMixin, CreateView):

    model = Pelicula
    success_url = "/app_Daiki/pelicula/basePeliculas"
    fields = ['nombre', 'estudio', 'fecha_estreno', 'duracion']

class PeliculaUpdate(LoginRequiredMixin, UpdateView):

    model = Pelicula
    success_url = "/app_Daiki/pelicula/basePeliculas"
    fields = ['nombre', 'estudio', 'fecha_estreno', 'duracion']

class PeliculaDelete(LoginRequiredMixin, DeleteView):

    model = Pelicula
    success_url = "/app_Daiki/pelicula/basePeliculas"


