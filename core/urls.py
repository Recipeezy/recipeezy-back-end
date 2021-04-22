from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import include, path

urlpatterns = [
    path('users/', views.UserList.as_view(), name="users_list"),
    path('ingredients/', views.IngredientList.as_view(), name='ingredient_list'),
    path('ingredients/<int:pk>/', views.IngredientDetail.as_view(),
         name='ingredient_detail'),
    path('ingredients/pantry/', views.IngredientPantryList.as_view()),
    # path('ingredients/shopping_list/', views.IngredientShoppingList.as_view()),
    path('pantry/', views.PantryList.as_view(), name='pantry_list'),
    path('pantry/add/', views.PantryAdd.as_view(), name="pantry_add"),
    path('recipes/', views.RecipeList.as_view(), name='recipes_list'),
    path('recipes/<int:pk>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('shopping_list/', views.ShoppingListDetail.as_view()),
]

urlpatterns += format_suffix_patterns(urlpatterns)
