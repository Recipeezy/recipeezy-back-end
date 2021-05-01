from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.core.signals import request_finished
from django.dispatch import receiver


class User(AbstractUser):
    pass


@receiver(post_save, sender=User)
def create_pantry(sender, instance, created, **kwargs):
    if created:
        Pantry.objects.create(user=instance)

@receiver(post_save, sender=User)
def create_shopping_list(sender, instance, created, **kwargs):
    if created:
        ShoppingList.objects.create(user=instance)

@receiver(post_save, sender=User)
def create_selected_recipes(sender, instance, created, **kwargs):
    if created:
        SelectedRecipes.objects.create(user=instance)

@receiver(post_save, sender=User)
def create_recipe_history(sender, instance, created, **kwargs):
    if created:
        RecipeHistory.objects.create(user=instance)

@receiver(post_save, sender=User)
def create_favorite_recipes(sender, instance, created, **kwargs):
    if created:
        FavoriteRecipes.objects.create(user=instance)


class Pantry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_pantry')
    ingredients = models.ManyToManyField(
        'Ingredient', null=True, blank=True, related_name="pantry_ingredients")

    def __str__(self):
        return self.user.username


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100, null=True, blank=True)
    ingredients = models.ManyToManyField(
        Ingredient,
        through='RecipeIngredient',
        through_fields=('recipe', 'ingredient'),
        related_name='recipe_ingredient'
    )
    selectedrecipes = models.ForeignKey(
        'SelectedRecipes', on_delete=models.CASCADE, blank=True, null=True, related_name="selected_recipes")
    recipe_history = models.ForeignKey('RecipeHistory', on_delete=models.CASCADE,
        blank=True, null=True, related_name='recipe_history')
    favorite_recipes = models.ForeignKey('FavoriteRecipes', on_delete=models.CASCADE,
        blank=True, null=True, related_name='favorite_recipes')
    origin = models.CharField(max_length=100, null=True, blank=True)
    instructions = models.TextField(max_length=2500, null=True, blank=True)
    external_id = models.CharField(max_length=50, null=True, blank=True)
    img_id = models.CharField(max_length=150, null=True, blank=True)
    video_id = models.CharField(max_length=150, null=True, blank=True)
    
    def __str__(self):
        return self.title


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="recipe_ingredients")
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE, related_name="ingredients_list")
    measurement = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.recipe}, {self.ingredient}'


class ShoppingList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_shoppinglist')
    ingredients = models.ManyToManyField(
        Ingredient, null=True, blank=True, related_name="shoppinglist_ingredients")

    def __str__(self):
        return self.user.username


class SelectedRecipes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_recipes')

    def __str__(self):
        return self.user.username


class RecipeHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_recipehistory')

    def __str__(self):
        return self.user.username


class FavoriteRecipes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_favoriterecipes')

    def __str__(self):
        return self.user.username