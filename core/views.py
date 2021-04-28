from django.shortcuts import render, get_object_or_404
from rest_framework import generics, viewsets
from rest_framework.exceptions import ValidationError
from .models import (User, Pantry, Recipe, RecipeIngredient, Ingredient, ShoppingList, 
RecipeHistory, SelectedRecipes)
from .serializers import (IngredientSerializer, PantrySerializer, RecipeSerializer, UserSerializer,
ShoppingListSerializer, IngredientInfoSerializer, RecipePopulateSerializer, IngredientSwapSerializer, 
RecipeHistorySerializer, RecipeSwapSerializer, SelectedRecipesSerializer, SelectedRecipesSwapSerializer,
PantryIngredientSerializer, ShoppingListIngredientSerializer, UserSerializer)


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
        serializer.save(pantry_ingredients=self.request.user.pantry, shoppinglist_ingredients=None)


class IngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientInfoSerializer


class PantryList(generics.ListCreateAPIView):
    queryset = Pantry.objects.all()
    serializer_class = PantrySerializer

    def get_queryset(self):
        if self.request.user.id not in [pantry.user.id for pantry in Pantry.objects.all()]:
            Pantry.objects.create(user=self.request.user)

        return Pantry.objects.filter(user=self.request.user)


class PantryAdd(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = PantryIngredientSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user.pantry.id)


class PantryRemove(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSwapSerializer

    def perform_update(self, serializer):
        serializer.save(pantry=None)


class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def perform_create(self, serializer):
        serializer.save(selectedrecipes=self.request.user.selectedrecipes)


class RecipePopulate(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipePopulateSerializer

    def perform_create(self, serializer):
        serializer.save(selectedrecipes=self.request.user.selectedrecipes)


class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ShoppingListDetail(generics.ListCreateAPIView):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer

    def get_queryset(self):
        if self.request.user.id not in [shop.user.id for shop in ShoppingList.objects.all()]:
            ShoppingList.objects.create(user=self.request.user)

        return ShoppingList.objects.filter(user=self.request.user)

class ShoppingListAdd(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = ShoppingListIngredientSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user.shoppinglist.id)


class ShoppingListRemove(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSwapSerializer

    def perform_update(self, serializer):
        serializer.save(shoppinglist=None)


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
        serializer.save(recipe_history=self.request.user.recipehistory, selectedrecipes=None)


class SelectedRecipesList(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = SelectedRecipesSerializer

    def get_queryset(self):
        if self.request.user.id not in [selectrec.user.id for selectrec in SelectedRecipes.objects.all()]:
            SelectedRecipes.objects.create(user=self.request.user)

        return SelectedRecipes.objects.filter(user=self.request.user)


class SelectedRecipesAdd(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = SelectedRecipesSwapSerializer

    def perform_update(self, serializer):
        serializer.save(selectedrecipes=self.request.user.selectedrecipes, recipe_history=None)

