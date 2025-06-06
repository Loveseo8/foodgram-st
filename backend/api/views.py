from rest_framework import viewsets
from recipes.models import Recipe
from api.serializers import RecipeWriteSerializer

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all().order_by('-id')
    serializer_class = RecipeWriteSerializer
