from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Recette, Categorie, Membre, Commentaire
from .forms import ConnexionForm, InscriptionForm, CommentaireForm
from django.contrib.auth.hashers import make_password, check_password


def index(request):
    membr = None
    membr_id = request.session.get('membr_id')
    if membr_id:
        membr = Membre.objects.get(pk = membr_id)
    
    list_recette = Recette.objects.order_by('image')
    categories = Categorie.objects.all()
    context = {
        'list_recette':list_recette,
        'categories':categories,
        'membr':membr  
        }
    return render(request, 'blog/index.html', context)

def recette(request, recette_id):
    recette = get_object_or_404(Recette, pk= recette_id)
    commentaires = Commentaire.objects.filter(crecette_id = recette_id)
    categories = Categorie.objects.all()
    if request.method == 'POST':
        form = CommentaireForm(request.POST)
        if form.is_valid():
            autor = form.cleaned_data['autor']
            content = form.cleaned_data['content']
            note = form.cleaned_data['note']
            crecette = Recette.objects.get(pk=recette_id)
            comment = Commentaire(autor=autor, content = content, note = note, crecette = crecette)
            comment.save()
            return HttpResponseRedirect(f'/recette/{recette_id}')
    else:
        form = CommentaireForm()
    context = {
        'form':form,
        'commentaires':commentaires,
        'recette':recette,
        'categories':categories
        }
            
    return render(request, 'blog/recette.html', context)

def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            pseudo = form.cleaned_data['pseudo']
            mdp = form.cleaned_data['mdp']
            mdp_encoded = make_password(mdp)
            print(mdp_encoded)
            
            email = form.cleaned_data['mail']
            membr = Membre(name = name, pseudo = pseudo, mdp = mdp_encoded, email=email)
            membr.save()
            request.session['membr_id'] = membr.id
            return HttpResponseRedirect('/')
    else:
        form = InscriptionForm()
        
    return render(request, 'blog/inscription.html', {'form':form})

def categorie(request, idCategorie):
    list_recette = Recette.objects.filter(categori_id = idCategorie)
    categories = Categorie.objects.all()
    context = {
        'idCategorie':idCategorie,
        'list_recette':list_recette,
        'categories':categories
        }
    return render(request, 'blog/categorie.html', context)

def deconnexion(request):
    del request.session['membr_id']
    return HttpResponseRedirect('/')

def connexion(request):
    if request.method == 'POST':
        form = ConnexionForm(request.POST)
        if form.is_valid():
            pseudo = form.cleaned_data['pseudo']
            mdp = form.cleaned_data['mdp']
            try:
                membr = get_object_or_404(Membre, pseudo = pseudo)
                if check_password(mdp, membr.mdp):
                    request.session['membr_id'] = membr.id
                    return HttpResponseRedirect('/')
                else:
                    raise
            except:
                form.errors['__all__'] = form.error_class(["Votre pseudo ou votre mot de passe est incorrect"]) 
    else:
        form = ConnexionForm
    context = {'form':form}
    
    return render(request, 'blog/connexion.html', context)
    
    
    
# Create your views here.
