from rest_framework import serializers, fields

from .models import (User, Pantry, Recipe, RecipeIngredient, Ingredient, ShoppingList, 
RecipeHistory, SelectedRecipes)


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name',]


class IngredientInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'pantry', 'shoppinglist',]


class IngredientSwapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'pantry', 'shoppinglist',]


class PantrySerializer(serializers.ModelSerializer):
    pantry_ingredients = IngredientSerializer(many=True, read_only=True)
    username = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Pantry
        fields = ['user', 'username', 'pantry_ingredients',]


class RecipeIngredientSerializer(serializers.ModelSerializer):
    ingredient = serializers.ReadOnlyField(source="ingredient.name")

    class Meta:
        model = RecipeIngredient
        fields = ['measurement', 'ingredient',] 


class RecipeSerializer(serializers.ModelSerializer):
    recipe_ingredients = RecipeIngredientSerializer(many=True, read_only=True)
    ingredients = IngredientSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = [
            'id', 'external_id', 'title', 'category', 'origin', 'instructions', 'selectedrecipes',
                'recipe_history', 'recipe_ingredients', 'ingredients'
        ]


class UserSerializer(serializers.ModelSerializer):
    recipes = serializers.ReadOnlyField(source="user.pantry.recipe")

    class Meta:
        model = User
        fields = ['id', 'username', 'recipes',]


class ShoppingListSerializer(serializers.ModelSerializer):
    shoppinglist_ingredients = IngredientSerializer(many=True, read_only=True)

    class Meta:
        model = ShoppingList
        fields = ['id', 'shoppinglist_ingredients',]


class RecipeCreateSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)
    
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'category', 'origin', 'instructions', 
            'ingredients', 'selectedrecipes',]
    
    # def update(self, instance, validated_data):


    # def create(self, validated_data):
    #     ingredients_data = validated_data.pop('ingredients')
    #     recipe = Recipe.objects.create(**validated_data)
    #     for ingredient_data in ingredients_data:
    #         ingredient = Ingredient.objects.create(name=ingredient_data['name'])
    #         recipe.ingredients.add(ingredient)
    #     return recipe


class RecipeHistorySerializer(serializers.ModelSerializer):
    recipe_history = RecipeSerializer(many=True, read_only=True)

    class Meta:
        model = RecipeHistory
        fields = ['id', 'recipe_history',]


class RecipeSwapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'selectedrecipes', 'recipe_history',]


class SelectedRecipesSerializer(serializers.ModelSerializer):
    selected_recipes = RecipeSerializer(many=True, read_only=True)

    class Meta:
        model = SelectedRecipes
        fields = ['id', 'selected_recipes',]


class SelectedRecipesSwapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'selectedrecipes', 'recipe_history',]