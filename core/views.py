from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .models import User, Pantry, Recipe, RecipeIngredient, Ingredient, ShoppingList, RecipeHistory
from .serializers import (IngredientSerializer, PantrySerializer, RecipeSerializer, UserSerializer,
ShoppingListSerializer, IngredientInfoSerializer, RecipeCreateSerializer, PantryRecipesSerializer,
RecipePantrySerializer, IngredientSwapSerializer, RecipeHistorySerializer, RecipeSwapSerializer)


class IngredientList(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class IngredientInfoList(generics.ListAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientInfoSerializer


class IngredientContainerSwap(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSwapSerializer

    def perform_update(self, serializer):
        serializer.save(pantry=self.request.user.pantry, shoppinglist=None)


class IngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientInfoSerializer


class PantryList(generics.ListAPIView):
    queryset = Pantry.objects.all()
    serializer_class = PantrySerializer

    def get_queryset(self):
        if self.request.user.id not in [pantry.user.id for pantry in Pantry.objects.all()]:
            Pantry.objects.create(user=self.request.user)

        return Pantry.objects.filter(user=self.request.user)


class PantryAdd(generics.CreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

    def perform_create(self, serializer):
        serializer.save(pantry=Pantry.objects.get(user=self.request.user))


class PantryRemove(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSwapSerializer

    def perform_update(self, serializer):
        serializer.save(pantry=None)


class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return RecipeCreateSerializer
        return RecipeSerializer

    def perform_create(self, serializer):
        serializer.save(pantry=self.request.user.pantry)


class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ShoppingListDetail(generics.ListAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = ShoppingListSerializer

    def get_queryset(self):
        if self.request.user.id not in [shop.user.id for shop in ShoppingList.objects.all()]:
            ShoppingList.objects.create(user=self.request.user)

        return ShoppingList.objects.filter(user=self.request.user)

class ShoppingListAdd(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

    def perform_create(self, serializer):
        serializer.save(shoppinglist=self.request.user.shoppinglist)


class ShoppingListRemove(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSwapSerializer

    def perform_update(self, serializer):
        serializer.save(shoppinglist=None)

class PantryRecipes(generics.ListAPIView):
    queryset = Pantry.objects.all()
    serializer_class = PantryRecipesSerializer

    def get_queryset(self):
        if self.request.user.id not in [pantry.user.id for pantry in Pantry.objects.all()]:
            Pantry.objects.create(user=self.request.user)

        return Pantry.objects.filter(user=self.request.user)


class PantryRecipeAdd(generics.RetrieveUpdateAPIView):
    querset = Pantry.objects.all()
    serializer_class = RecipeSerializer

    def perform_update(self, serializer):
        serializer.save(pantry=self.request.user.pantry)


class RecipeHistoryList(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeHistorySerializer

    def get_queryset(self):
        if self.request.user.id not in [rechist.user.id for rechist in RecipeHistory.objects.all()]:
            RecipeHistory.objects.create(user=self.request.user)

        return RecipeHistory.objects.filter(user=self.request.user)


class RecipeHistoryAdd(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSwapSerializer

    def perform_update(self, serializer):
        serializer.save(recipe_history=self.request.user.recipehistory, pantry=None)

