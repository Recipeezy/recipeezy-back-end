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
        pantry = Pantry.objects.get(user=self.request.user)
        shoppinglist = ShoppingList.objects.get(user=self.request.user)
        ingredient = serializer.save()
        pantry.ingredients.add(ingredient)
        shoppinglist.ingredients.remove(ingredient)
        ingredient.save()



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
        serializer.save(user=self.request.user)


class PantryRemove(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSwapSerializer

    def perform_update(self, serializer):
        pantry = Pantry.objects.get(user=self.request.user)
        ingredient = serializer.save()
        pantry.ingredients.remove(ingredient)
        ingredient.save()


class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get_serializer_class(self):
        if self.request.method == "POST":
            return RecipePopulateSerializer
        return RecipeSerializer

    def perform_create(self, serializer):
        selectedrecipes = SelectedRecipes.objects.get(user=self.request.user)
        serializer.save(selectedrecipes=selectedrecipes)


class RecipePopulate(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipePopulateSerializer

    def perform_create(self, serializer):
        selectedrecipes = SelectedRecipes.objects.get(user=self.request.user)
        serializer.save(selectedrecipes=selectedrecipes)


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
        serializer.save(user=self.request.user)


class ShoppingListRemove(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSwapSerializer

    def perform_update(self, serializer):
        shoppinglist = ShoppingList.objects.get(user=self.request.user)
        ingredient = serializer.save()
        shoppinglist.ingredients.remove(ingredient)
        ingredient.save()


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

