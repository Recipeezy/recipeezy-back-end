from django.shortcuts import render
from rest_framework import generics
from .models import User, Pantry, Recipe, RecipeIngredient, Ingredient, ShoppingList
from .serializers import IngredientSerializer, PantrySerializer, RecipeSerializer, UserSerializer, ShoppingListSerializer

# Create your views here.


class IngredientList(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class IngredientPantryList(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

    def perform_create(self, serializer):
        serializer.save(pantry=self.request.user.pantry)


# class IngredientShoppingList(generics.ListCreateAPIView):
#     queryset = Ingredient.objects.all()
#     serializer_class = IngredientSerializer

#     def perform_create(self, serializer):
#         serializer.save(shopping_list=self.request.shopping_list)


class IngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


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


class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


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