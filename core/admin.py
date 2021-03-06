from django.contrib import admin
from .models import (User, Pantry, RecipeIngredient, Ingredient, Recipe, ShoppingList, RecipeHistory,
SelectedRecipes, FavoriteRecipes)


admin.site.register(User)
admin.site.register(Pantry)
admin.site.register(RecipeIngredient)
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(ShoppingList)
admin.site.register(RecipeHistory)
admin.site.register(SelectedRecipes)
admin.site.register(FavoriteRecipes)