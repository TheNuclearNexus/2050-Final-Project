
import os
import json
import re
import time

from Recipe import Recipe


class RecipeProcessor:
    recipes: list = []
    recipe_num = 0

    def __init__(self) -> None:
        pass 

    def convert_time(self, time: str) -> str:
        if time == "":
            return "00:00"
        elif match := re.match(r"PT([0-9]+H)?([0-9]+M)?", time):
            hours = match.group(1)
            if hours == None:
                hours = 0
            else:
                hours = int(hours[:-1])
            
            minutes = match.group(2)
            if minutes == None:
                minutes = 0
            else:
                minutes = int(minutes[:-1])
            
            return f"{hours:02d}:{minutes:02d}"
        else:
            return "00:00"

            
            

    def load_recipes(self, json_file: str):
        if not os.path.exists(json_file):
            raise FileNotFoundError("JSON File does not exist")
        
        if not os.path.exists('./images'):
            os.mkdir("./images")
        
        json_data: list[dict] = json.loads(open(json_file, 'r', encoding='utf8').read()) 
        print("""
 /$$$$$$$                      /$$                           /$$$$$$$$ /$$       /$$                    
| $$__  $$                    |__/                          |__  $$__/| $$      |__/                    
| $$  \ $$  /$$$$$$   /$$$$$$$ /$$  /$$$$$$   /$$$$$$          | $$   | $$$$$$$  /$$ /$$$$$$$   /$$$$$$ 
| $$$$$$$/ /$$__  $$ /$$_____/| $$ /$$__  $$ /$$__  $$         | $$   | $$__  $$| $$| $$__  $$ /$$__  $$
| $$__  $$| $$$$$$$$| $$      | $$| $$  \ $$| $$$$$$$$         | $$   | $$  \ $$| $$| $$  \ $$| $$  \ $$
| $$  \ $$| $$_____/| $$      | $$| $$  | $$| $$_____/         | $$   | $$  | $$| $$| $$  | $$| $$  | $$
| $$  | $$|  $$$$$$$|  $$$$$$$| $$| $$$$$$$/|  $$$$$$$         | $$   | $$  | $$| $$| $$  | $$|  $$$$$$$
|__/  |__/ \_______/ \_______/|__/| $$____/  \_______/         |__/   |__/  |__/|__/|__/  |__/ \____  $$
                                  | $$                                                         /$$  \ $$
                                  | $$                                                        |  $$$$$$/
                                  |__/                                                         \______/ """)
        print()

        for i in range(len(json_data)):
            recipe_data = json_data[i]
            name: str = recipe_data["name"]
            description: str = recipe_data["description"]
            image_url: str = recipe_data["image"]
            recipe_yield: str = recipe_data["recipeYield"]
            cook_time: str = recipe_data["cookTime"]
            prep_time: str = recipe_data["prepTime"]
            ingredients: list[str] =recipe_data["ingredients"]

            cook_time = self.convert_time(cook_time)
            prep_time = self.convert_time(prep_time)

            recipe = Recipe(name, description, cook_time, prep_time, recipe_yield, ingredients)

            print(f"\rDownloading image {i + 1} / {len(json_data)}", end="")
            recipe.set_image(image_url)
            self.recipe_num = self.recipe_num + 1
            self.recipes.append(recipe)
        
        print()

    def get_recipe_num(self):
        return self.recipe_num

    def get_recipes(self):
        return self.recipes

if __name__ == "__main__":
    RecipeProcessor().load_recipes("recipes.json")