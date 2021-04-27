from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import include, path

urlpatterns = [
    path('users/', views.UserList.as_view(), name="users_list"),
    path('ingredients/', views.IngredientList.as_view(), name='ingredient_list'),
    path('ingredients/<int:pk>/', views.IngredientDetail.as_view(),
        name='ingredient_detail'),
    path('ingredients/info/', views.IngredientInfoList.as_view()),
    path('ingredients/<int:pk>/swap/', views.IngredientContainerSwap.as_view()),
    path('pantry/', views.PantryList.as_view(), name='pantry_list'),
    path('pantry/add/', views.PantryAdd.as_view(), name='pantry_add'),
    path('pantry/<int:pk>/remove/', views.PantryRemove.as_view(), name='pantry_remove'),
    path('recipes/', views.RecipeList.as_view(), name='recipes_list'),
    path('recipes/<int:pk>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('shopping_list/', views.ShoppingListDetail.as_view(), name='shoppinglist_detail'),
    path('shopping_list/add/', views.ShoppingListAdd.as_view(), name='shoppinglist_add'),
    path('shopping_list/<int:pk>/remove/', views.ShoppingListRemove.as_view(), name='shoppinglist_remove'),
    path('recipe_history/', views.RecipeHistoryList.as_view(), name='recipehistory_list'),
    path('recipe_history/<int:pk>/', views.RecipeHistoryAdd.as_view(), name='recipehistory_add'),
    path('selected_recipes/', views.SelectedRecipesList.as_view(), name='selectedrecipes_list'),
    path('selected_recipes/<int:pk>/', views.SelectedRecipesAdd.as_view(), name='selectedrecipes_add'),
]

urlpatterns += format_suffix_patterns(urlpatterns)
