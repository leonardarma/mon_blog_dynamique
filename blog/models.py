from django.db import models

class Categorie(models.Model):
    """
    Les catégories des recettes. S'affichent en haut de pages et permet de trier
    """
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Membre(models.Model):
    """
    Les membres qui peuvent créer des recettes.
    """
    name = models.CharField(max_length=100, default="name")
    pseudo = models.CharField(max_length=100, default="pseudo")
    mdp = models.CharField(max_length=100, default="mdp")
    email = models.CharField(max_length=100, default="mail")
    date_inscription = models.DateTimeField(auto_now_add=True, auto_now= False)
    def __str__(self):
        return self.name
    
class Recette(models.Model):
    """
    Les recettes importées sur le site via l'interface admin. Une liste d'ingrédients est liée à une recette.
    """
    name = models.CharField(max_length=100, default='recette_name')
    image = models.ImageField( upload_to="recette_img")
    describe = models.TextField()
    pub_date = models.DateTimeField(auto_now_add= True, auto_now= False)
    categori = models.ForeignKey(Categorie, on_delete=models.PROTECT)
    membre = models.ForeignKey(Membre, on_delete=models.PROTECT, related_name= "membre", null=True)
    def __str__(self):
        return self.name

class Commentaire(models.Model):
    crecette = models.ForeignKey(Recette, on_delete=models.PROTECT, related_name= "comments", null=True)
    autor = models.CharField(max_length=100, default='autor name')
    content = models.TextField(max_length=1000)
    note = models.IntegerField()
    date_post = models.DateTimeField(auto_now_add= True, auto_now= False)
    def __str__(self):
        return self.content
    
    
class Ingredient(models.Model):
    """
    Les ingredients des recettes.
    """
    name = models.CharField(max_length=100, default='ingredient name')
    quantity = models.CharField(max_length=20, default='10')
    unite = models.CharField(max_length=20, default="g")
    recette = models.ForeignKey(Recette, on_delete=models.PROTECT, related_name= "ingredients", null=True)
    def __str__(self):
        return self.name

# Create your models here.
