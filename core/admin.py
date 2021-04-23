from django.contrib import admin
from .models import User, Pantry, RecipeIngredient, Ingredient, Recipe, ShoppingList


admin.site.register(User)
admin.site.register(Pantry)
admin.site.register(RecipeIngredient)
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(ShoppingList)