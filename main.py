"""
This module provides functionality to adjust
recipes for different numbers of servings.

It includes functions to:
- Adjust the ingredient quantities in a recipe
based on the desired number of servings.
- Load a recipe from a JSON string format.

Functions:
- adjust_recipe(recipe, portions):
Adjusts ingredient quantities in a recipe
dictionary for a given number of servings.
- load_recipe(json_string):
Parses a JSON string to a Python dictionary
representing the recipe.

Example usage:
    Adjust a recipe for 2 servings:
        recipe_json = '{"title": "Spaghetti Bolognese",
        "ingredients":
        {"Spaghetti": 400,
        "Tomato Sauce": 300,
        "Minced Meat": 500},
        "servings": 4}'
        recipe_dict = load_recipe(recipe_json)
        new_adjusted_recipe = adjust_recipe(2, recipe_dict)
        print(json.dumps(new_adjusted_recipe))
"""

import json


def adjust_recipe(recipe, portions):
    """
    Adjusts the recipe for a given number of servings.

    Args:
        recipe (dict): The recipe as a Python dictionary.
        portions (int): The desired number of servings.

    Returns:
        dict: The adjusted recipe with updated ingredient quantities.
    """

    # Calculate the factor by which to adjust the ingredient quantities
    adjustment_factor = portions / recipe['servings']

    # Adjust the ingredient quantities
    adjusted_ingredients = {
        ingredient: quantity * adjustment_factor
        for ingredient, quantity in recipe['ingredients'].items()
    }

    # Create the adjusted recipe
    adjusted_recipe = {
        'title': recipe['title'],
        'ingredients': adjusted_ingredients,
        'servings': portions
    }

    return adjusted_recipe


def load_recipe(json_string):
    """
    Loads a recipe from a JSON string.

    Args:
        json_string (str): The recipe in JSON format.

    Returns:
        dict: The recipe as a Python dictionary.
    """
    return json.loads(json_string)


if __name__ == '__main__':
    # Example recipe data
    recipe_json = (
        '{"title": "Spaghetti Bolognese", '
        '"ingredients": {"Spaghetti": 400, '
        '"Tomato Sauce": 300, '
        '"Minced Meat": 500}, '
        '"servings": 4}'
    )
    recipe_dict = load_recipe(recipe_json)

    # Adjust the recipe for 2 servings
    new_adjusted_recipe = adjust_recipe(2, recipe_dict)

    # Print the adjusted recipe
    print(json.dumps(new_adjusted_recipe))
