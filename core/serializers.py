from rest_framework import serializers, fields

from .models import (User, Pantry, Recipe, RecipeIngredient, Ingredient, ShoppingList, 
RecipeHistory, SelectedRecipes, FavoriteRecipes)


class UserSerializer(serializers.ModelSerializer):
    recipes = serializers.ReadOnlyField(source="user.pantry.recipe")

    class Meta:
        model = User
        fields = ['id', 'username', 'recipes',]


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name',]
        validators = []


class IngredientInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'pantry_ingredients', 'shoppinglist_ingredients',]


class IngredientSwapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'pantry_ingredients', 'shoppinglist_ingredients',]


class PantrySerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)
    username = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Pantry
        fields = ['user', 'username', 'ingredients',]


class PantryIngredientSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Pantry
        fields = ['id', 'user', 'ingredients',]

    def create(self, validated_data: dict):
        ingredients_data = validated_data.pop('ingredients')
        pantry = Pantry.objects.get(user=validated_data['user'])
        for ingredient_data in ingredients_data:
            name, created = Ingredient.objects.get_or_create(name=ingredient_data['name'].lower())
            pantry.ingredients.add(name)
        return pantry


class RecipeIngredientSerializer(serializers.ModelSerializer):
    ingredient = serializers.ReadOnlyField(source="ingredient.name")
    ingredient_id = serializers.ReadOnlyField(source="ingredient.id")

    class Meta:
        model = RecipeIngredient
        fields = ['ingredient_id', 'ingredient', 'measurement',] 


class RecipeSerializer(serializers.ModelSerializer):
    recipe_ingredients = RecipeIngredientSerializer(many=True)
    ingredients = IngredientSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = [
            'id', 'external_id', 'title', 'category', 'origin', 'instructions', 'img_id', 'video_id', 'selectedrecipes',
                'recipe_history', 'recipe_ingredients', 'ingredients',
        ]


class ShoppingListSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)
    username = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = ShoppingList
        fields = ['user', 'username', 'ingredients',]


class ShoppingListSwapSerializer(serializers.ModelSerializer):
    ingredients = IngredientSwapSerializer(many=True)
    username = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = ShoppingList
        fields = ['username', 'ingredients',]


class ShoppingListMoveArraySerializer(serializers.ModelSerializer):
    ingredients = serializers.ListField(child=serializers.CharField())
    user = UserSerializer(read_only=True)

    class Meta:
        model = ShoppingList
        fields = ['id', 'user', 'ingredients']

    def create(self, validated_data: dict):
        ingredients_data = validated_data.pop('ingredients')
        pantry = Pantry.objects.get(user=validated_data['user'])
        shoppinglist = ShoppingList.objects.get(user=validated_data['user'])
        for ingredient_data in ingredients_data:
            name, created = Ingredient.objects.get_or_create(name=ingredient_data.lower())
            pantry.ingredients.add(name)
            shoppinglist.ingredients.remove(name)
        return shoppinglist


class ShoppingListIngredientSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = ShoppingList
        fields = ['id', 'user', 'ingredients']

    def create(self, validated_data: dict):
        ingredients_data = validated_data.pop('ingredients')
        shoppinglist = ShoppingList.objects.get(**validated_data)
        for ingredient_data in ingredients_data:
            name, created = Ingredient.objects.get_or_create(name=ingredient_data['name'].lower())
            shoppinglist.ingredients.add(name)
        return shoppinglist


class RecipeCreateSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'category', 'origin', 'instructions', 'img_id', 'video_id',
            'ingredients', 'selectedrecipes',]

    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients')
        recipe = Recipe.objects.create(**validated_data)
        for ingredient_data in ingredients_data:
            ingredient, created = Ingredient.objects.get_or_create(name=ingredient_data['name'].lower())
            recipe.ingredients.add(ingredient)
        return recipe


class RecipeCreateTestSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)
    recipe_ingredients = RecipeIngredientSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'category', 'origin', 'instructions', 'img_id', 'video_id',
            'ingredients', 'selectedrecipes', 'recipe_ingredients',]

    def create(self, validated_data: dict):
        ingredients_data = self.context['request'].data['ingredients']
        recipe = Recipe.objects.create(title=validated_data['title'], selectedrecipes=validated_data['selectedrecipes'],
            category=validated_data['category'], origin=validated_data['origin'], instructions=validated_data['instructions'],
            img_id=validated_data['img_id'], video_id=validated_data['video_id'])
        for ingredient_data in ingredients_data:
            ingredient, created = Ingredient.objects.get_or_create(name=ingredient_data['name'].lower())
            recipe.ingredients.add(ingredient, through_defaults={'measurement': ingredient_data['measurement']})
        return recipe


class RecipeSwapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'selectedrecipes', 'recipe_history', 'favorite_recipes']


class RecipeHistorySerializer(serializers.ModelSerializer):
    recipe_history = RecipeSerializer(many=True, read_only=True)

    class Meta:
        model = RecipeHistory
        fields = ['id', 'user', 'recipe_history',]


class SelectedRecipesSerializer(serializers.ModelSerializer):
    selected_recipes = RecipeSerializer(many=True, read_only=True)

    class Meta:
        model = SelectedRecipes
        fields = ['id', 'user', 'selected_recipes',]


class RecipeFavoritesSerializer(serializers.ModelSerializer):
    recipe_ingredients = RecipeIngredientSerializer(many=True, read_only=True)
    ingredients = IngredientSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = [
            'id', 'external_id', 'title', 'category', 'origin', 'instructions', 'img_id', 'video_id', 'notes',
                'selectedrecipes', 'recipe_history', 'recipe_ingredients', 'ingredients',
        ]


class FavoriteRecipesSerializer(serializers.ModelSerializer):
    favorite_recipes = RecipeFavoritesSerializer(many=True)

    class Meta:
        model = FavoriteRecipes
        fields = ['id', 'user', 'favorite_recipes',]
