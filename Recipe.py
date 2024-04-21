import os
import requests


class Recipe:
    def __init__(self, name, description, cook_time, prep_time, recipe_yield, ingredients) -> None:
        self.name = name
        self.description = description
        self.cook_time = cook_time
        self.prep_time = prep_time
        self.recipe_yield = recipe_yield
        self.ingredients = ingredients

    # get the name of the recipe
    def get_name(self):
        return self.name

    # returns the cookTime for a recipe in HH:MM format with leading zeros
    def get_cook_time(self):
        return self.cook_time

    # returns the prepTime for a recipe in HH:MM format with leading zeros
    def get_prep_time(self):
        return self.prep_time

    def get_description(self):
        return self.description

    # returns the recipeYield for a given recipe
    def get_recipe_yield(self):
        return self.recipe_yield

    #downloads an image from the web and displays it in the UI. An ASCII-based progress-bar must be
    #displayed in the command line as images are downloaded. This should include the index of the image downloaded so
    #far. (Example: ! Downloading image 10 of xxx . . . ) <- look at PDF
    def set_image(self, url):     
        file_name = url.split('/')[-1]
        self.image = f"images/{file_name}"

        if not os.path.exists(self.image):
            open(self.image, 'wb+').write(requests.get(url).content)

    # returns the name of an image file for saving or displaying in the UI
    def get_image(self):
        return self.image