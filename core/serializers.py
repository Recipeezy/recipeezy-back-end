from rest_framework import serializers

from .models import User, Pantry, Recipe, RecipeIngredient, Ingredient, ShoppingList


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', ]


class IngredientInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'pantry', 'shoppinglist', ]


class PantrySerializer(serializers.ModelSerializer):
    ingredients_list = IngredientSerializer(many=True, read_only=True)
    username = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Pantry
        fields = ['user', 'username', 'ingredients_list', ]


class RecipeIngredientSerializer(serializers.ModelSerializer):
    ingredient = serializers.ReadOnlyField(source="ingredient.name")

    class Meta:
        model = RecipeIngredient
        fields = ['measurement', 'ingredient', ] 


class RecipeSerializer(serializers.ModelSerializer):
    recipe_ingredients = RecipeIngredientSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = [
            'id', 'external_id', 'title', 'category', 'origin', 'instructions', 'recipe_ingredients',
        ]


class UserSerializer(serializers.ModelSerializer):
    recipes = serializers.ReadOnlyField(source="user.pantry.recipe")

    class Meta:
        model = User
        fields = ['id', 'username', 'recipes', ]


class ShoppingListSerializer(serializers.ModelSerializer):
    shopping_list = IngredientSerializer(many=True, read_only=True)

    class Meta:
        model = ShoppingList
        fields = ['id', 'shopping_list', ]
