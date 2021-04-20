from django.shortcuts import render
from rest_framework import generics
from .models import User, Pantry, Recipe, RecipeIngredient, Ingredient
from .serializers import IngredientSerializer, PantrySerializer

# Create your views here.


class IngredientList(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

    def perform_create(self, serializer):
        new_pantry = Pantry.objects.get_or_create(user=self.request.user)
        serializer.save(pantry=new_pantry[0])


class IngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class PantryList(generics.ListAPIView):
    queryset = Pantry.objects.all()
    serializer_class = PantrySerializer
