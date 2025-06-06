from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    measurement_unit = models.CharField(max_length=200)

class Recipe(models.Model):
    author = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='recipes')
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='recipes/')
    text = models.TextField()
    cooking_time = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.PositiveSmallIntegerField()
