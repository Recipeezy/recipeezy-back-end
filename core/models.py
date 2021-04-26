from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    pass


class Pantry(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    pantry = models.ForeignKey(
        Pantry, on_delete=models.CASCADE, null=True, blank=True, related_name="ingredients_list")
    shoppinglist = models.ForeignKey(
        'ShoppingList', on_delete=models.CASCADE, null=True, blank=True, related_name="shopping_list")

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100, null=True, blank=True)
    ingredients = models.ManyToManyField(
        Ingredient,
        through='RecipeIngredient',
        through_fields=('recipe', 'ingredient'),
        related_name='ingredients_info'
    )
    pantry = models.ForeignKey(
        Pantry, on_delete=models.CASCADE, blank=True, null=True, related_name="pantry_recipes")
    recipe_history = models.ForeignKey('RecipeHistory', on_delete=models.CASCADE,
        blank=True, null=True, related_name='recipe_history')
    origin = models.CharField(max_length=100, null=True, blank=True)
    instructions = models.TextField(max_length=2500, null=True, blank=True)
    external_id = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="recipe_ingredients")
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE, related_name="ingredients_list")
    measurement = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.recipe}, {self.ingredient}'


class ShoppingList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s shopping list"


class RecipeHistory(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s recipe history"