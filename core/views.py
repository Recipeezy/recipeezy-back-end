from django.shortcuts import render
from rest_framework import generics
from .models import User, Pantry, Recipe, RecipeIngredient, Ingredient
from .serializers import IngredientSerializer, PantrySerializer

# Create your views here.


class IngredientList(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

    def perform_create(self, serializer):
        try:
            new_pantry = Pantry.objects.get(user=self.request.user)
        except self.model.DoesNotExist:
            new_pantry = Pantry.objects.create(user=self.request.user)
        serializer.save(pantry=new_pantry)


class PantryList(generics.ListAPIView):
    queryset = Pantry.objects.all()
    serializer_class = PantrySerializer
