from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

class InscriptionForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':"Votre nom *", "class":'inputChamp'}))
    pseudo = forms.CharField( max_length=100, widget=forms.TextInput(attrs={'placeholder':"Votre pseudo *", "class":'inputChamp'}))
    mail = forms.CharField( max_length=100, validators=[validators.validate_email], widget=forms.TextInput(attrs={'placeholder':"Votre email *", "class":'inputChamp'}))
    mdp = forms.CharField( max_length=100, widget=forms.TextInput(attrs={'placeholder':"Votre mdp *", "class":'inputChamp'}))
    conf_mdp = forms.CharField( max_length=100, widget=forms.TextInput(attrs={'placeholder':"Confirmation de votre mdp *", "class":'inputChamp'}))
    
    def clean_mail(self):
        data = self.cleaned_data['mail']
        
        if "test" in data:
            raise ValidationError("Votre email n'est pas une adresse valide")
        return data
    
    def clean(self):
        cleaned_data = super().clean()
        
        if len(cleaned_data):
            cleaned_mdp = cleaned_data['mdp']
            cleaned_conf_mdp = cleaned_data['conf_mdp']
            
            if cleaned_mdp != cleaned_conf_mdp:
                raise ValidationError("Vos mots de passe ne sont pas identiques")
        return cleaned_data
    
class CommentaireForm(forms.Form):
    autor = forms.CharField(label='Your name', max_length=100)
    content = forms.CharField(widget=forms.Textarea)
    note = forms.IntegerField(min_value=0, max_value=5)
    
class ConnexionForm(forms.Form):
    pseudo = forms.CharField(label="Your Pseudo", max_length=100, widget=forms.TextInput(attrs={'placeholder':"Votre pseudo *", "class":'inputChamp'}))
    mdp = forms.CharField(label="Your Password", max_length=100, widget=forms.TextInput(attrs={'placeholder':"Votre mdp", "class":'inputChamp'}))
    
