from rest_framework import serializers

from .models import User, Pantry, Recipe, RecipeIngredient, Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name', ]


class PantrySerializer(serializers.ModelSerializer):
    ingredients_list = IngredientSerializer(many=True, read_only=True)

    class Meta:
        model = Pantry
        fields = ['user', 'ingredients_list', ]
