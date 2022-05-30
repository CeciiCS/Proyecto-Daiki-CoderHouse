from django.urls import path
from app_Daiki import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('inicio/', views.inicio, name="Inicio"),
    path('acercademi/', views.acercademi, name="AcercaDeMi"),
    
    path('busquedaMangas/', views.busquedaMangas, name="busquedaMangas"),
    path('buscar/', views.buscar),

    path('manga/baseMangas', views.MangaList.as_view(), name="BaseMangas"),
    path(r'^detalleManga/(?P<pk>\d+)$', views.MangaDetalle.as_view(), name="DetalleMangas"),
    path(r'^nuevoManga$', views.MangaCrear.as_view(), name="NewMangas"),
    path(r'^editarManga/(?P<pk>\d+)$', views.MangaUpdate.as_view(), name="EditMangas"),
    path(r'^eliminarManga/(?P<pk>\d+)$', views.MangaDelete.as_view(), name="DeleteMangas"),

    path('anime/baseAnimes', views.AnimeList.as_view(), name="BaseAnimes"),
    path(r'^detalleAnime/(?P<pk>\d+)$', views.AnimeDetalle.as_view(), name="DetalleAnimes"),
    path(r'^nuevoAnime$', views.AnimeCrear.as_view(), name="NewAnimes"),
    path(r'^editarAnime/(?P<pk>\d+)$', views.AnimeUpdate.as_view(), name="EditAnimes"),
    path(r'^eliminarAnime/(?P<pk>\d+)$', views.AnimeDelete.as_view(), name="DeleteAnimes"),

    path('pelicula/basePeliculas', views.PeliculaList.as_view(), name="BasePeliculas"),
    path(r'^detallePelicula/(?P<pk>\d+)$', views.PeliculaDetalle.as_view(), name="DetallePeliculas"),
    path(r'^nuevoPelicula$', views.PeliculaCrear.as_view(), name="NewPeliculas"),
    path(r'^editarPelicula/(?P<pk>\d+)$', views.PeliculaUpdate.as_view(), name="EditPeliculas"),
    path(r'^eliminarPelicula/(?P<pk>\d+)$', views.PeliculaDelete.as_view(), name="DeletePeliculas"),

    path('register', views.register, name='Register'),
    path('login', views.login_request, name='Login'),
    path('logout', LogoutView.as_view(template_name= 'app_Daiki/logout.html'), name='Logout'),
    path('editarUsuario', views.editarUsuario, name="EditarUsuario"),
    

]