from django.contrib import admin
from .models import User, Pantry, RecipeIngredient, Ingredient, Recipe

# Register your models here.

admin.site.register(User)
admin.site.register(Pantry)
admin.site.register(RecipeIngredient)
admin.site.register(Ingredient)
admin.site.register(Recipe)