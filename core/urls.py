from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import include, path

urlpatterns = [
    path('users/', views.UserList.as_view(), name="users_list"),
    path('ingredients/', views.IngredientList.as_view(), name='ingredient_list'),
    path('ingredients/<int:pk>/', views.IngredientDetail.as_view(),
        name='ingredient_detail'),
    path('ingredients/info/', views.IngredientInfoList.as_view(), name='ingredients_info'),
    path('ingredients/swap_all/', views.IngredientSwapAll.as_view(), name='ingredients_swapall'),
    path('pantry/', views.PantryList.as_view(), name='pantry_list'),
    path('pantry/<int:pk>/', views.PantryRemove.as_view(), name='pantry_remove'),
    path('pantry/<int:pk>/ingredients/', views.IngredientToPantry.as_view(), name='ingredient_to_pantry'),
    path('recipes/', views.RecipeList.as_view(), name='recipes_list'),
    path('recipes/test/', views.RecipeTestList.as_view()),
    path('recipes/<int:pk>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('shopping_list/', views.ShoppingListDetail.as_view(), name='shoppinglist_detail'),
    path('shopping_list/<int:pk>/', views.ShoppingListRemove.as_view(), name='shoppinglist_remove'),
    path('shopping_list/<int:pk>/ingredients/', views.IngredientToShopList.as_view(), name='ingredient_to_shoplist'),
    path('recipe_history/', views.RecipeHistoryList.as_view(), name='recipehistory_list'),
    path('recipe_history/<int:pk>/', views.RecipeHistoryAdd.as_view(), name='recipehistory_add'),
    path('selected_recipes/', views.SelectedRecipesList.as_view(), name='selectedrecipes_list'),
    path('selected_recipes/<int:pk>/', views.SelectedRecipesAdd.as_view(), name='selectedrecipes_add'),
    path('favorite_recipes/', views.FavoriteRecipesList.as_view(), name='favoriterecipes_list'),
    path('favorite_recipes/<int:pk>/', views.FavoriteRecipesRemove.as_view(), name='favoriterecipes_remove'),
    path('favorite_recipes/<int:pk>/add/', views.FavoriteRecipesAdd.as_view(), name='favoriterecipes_add'),
]

urlpatterns += format_suffix_patterns(urlpatterns)
