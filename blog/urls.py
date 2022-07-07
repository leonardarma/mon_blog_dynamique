from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recette/<int:recette_id>', views.recette, name='recette'),
    path('inscription', views.inscription, name = 'inscription'),
    path('categorie/<int:idCategorie>', views.categorie, name= 'categorie'),
    path('deconnexion', views.deconnexion, name= 'deconnexion' ),
    path('connexion', views.connexion, name='connexion' )
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)