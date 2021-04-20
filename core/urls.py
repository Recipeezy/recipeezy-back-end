from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import include, path

urlpatterns = [
    path('ingredients/', views.IngredientList.as_view(), name='ingredient_list'),
    path('pantry/', views.PantryList.as_view(), name='pantry_list'),
]

urlpatterns += format_suffix_patterns(urlpatterns)
