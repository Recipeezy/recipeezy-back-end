from django.shortcuts import render
from rest_framework import generics
from .models import User, Pantry, Recipe, RecipeIngredient, Ingredient
from .serializers import IngredientSerializer, PantrySerializer, RecipeSerializer, UserSerializer

# Create your views here.


class IngredientList(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

    def perform_create(self, serializer):
        new_pantry = Pantry.objects.get_or_create(
            user=User.objects.get(username=self.request.user.username))
        serializer.save(pantry=new_pantry[0])


class IngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class PantryList(generics.ListAPIView):
    queryset = Pantry.objects.all()
    serializer_class = PantrySerializer


class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
