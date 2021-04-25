from rest_framework import serializers, fields

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
        fields = ['user', 'username', 'ingredients_list',]


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
            'id', 'external_id', 'title', 'category', 'origin', 'instructions', 'pantry', 'recipe_ingredients', 'ingredients',
        ]


class RecipePantrySerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Recipe
        fields = [
            'id', 'external_id', 'title', 'category', 'origin', 'instructions', 'ingredients',
        ]


class PantryRecipesSerializer(serializers.ModelSerializer):
    ingredients_list = IngredientSerializer(many=True, read_only=True)
    username = serializers.ReadOnlyField(source="user.username")
    pantry_recipes = RecipePantrySerializer(many=True, read_only=True)

    class Meta:
        model = Pantry
        fields = ['user', 'username', 'ingredients_list', 'pantry_recipes',]


class UserSerializer(serializers.ModelSerializer):
    recipes = serializers.ReadOnlyField(source="user.pantry.recipe")

    class Meta:
        model = User
        fields = ['id', 'username', 'recipes',]


class ShoppingListSerializer(serializers.ModelSerializer):
    shopping_list = IngredientSerializer(many=True, read_only=True)

    class Meta:
        model = ShoppingList
        fields = ['id', 'shopping_list', ]


class RecipeCreateSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)
    
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'category', 'origin', 'instructions', 
            'ingredients', 'pantry',]
    
    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients')
        recipe = Recipe.objects.create(**validated_data)
        for ingredient_data in ingredients_data:
            ingredient = Ingredient.objects.create(name=ingredient_data['name'])
            recipe.ingredients.add(ingredient)
        return recipe
