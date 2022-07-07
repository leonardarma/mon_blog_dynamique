from django.contrib import admin

from .models import Ingredient, Recette, Categorie, Commentaire, Membre

# admin.site.register(Ingredient)
admin.site.register(Categorie)
admin.site.register(Commentaire)
admin.site.register(Membre)

class IngredientInline(admin.TabularInline):
    model = Ingredient  
    
@admin.register(Recette)

class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline, ]

# Register your models here.
