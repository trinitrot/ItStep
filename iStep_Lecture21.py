from pydantic import BaseModel, ValidationError
import json
import requests
from requests.exceptions import HTTPError, ConnectTimeout

URL = "https://crudcrud.com/api/348ac379ffd1459abb2b634a5f19b6d7/recipes"


class Recipe(BaseModel):
    name: str
    cuisine: str
    time_minutes: str

def main():
    data = [
        {
        "name": "Khachapuri",
        "cuisine": "Georgian",
        "time_minutes": "30"
        },
        {
        "name": "Khinkali",
        "cuisine": "Georgian",
        "time_minutes": "60"
        },
        {
        "name": "Mtsvadi",
        "cuisine": "Georgian",
        "time_minutes": "45"
        }
    ]

    with open("recipes.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)

    with open("recipes.json", "r", encoding="utf-8") as file:
        recipes_data = json.load(file)



    #POST all recipes
    for item in recipes_data:
        try:
            recipe = Recipe(**item)
            response = requests.post(
                URL,
                json=recipe.model_dump(),
                timeout=10
            )

            response.raise_for_status()

            print(f"POST status code:{response.status_code}")

        except ValidationError as e:
            print(f"Validation error: {e}")
            return

        except ConnectTimeout as e:
            print(f"Connection timeout: {e}")
            return

        except HTTPError as e:
            print(f"HTTP error: {e}")
            return

        except Exception as e:
            print(f"Unexpected error: {e}")
            return


    #GET all recipes (name & time_minutes)
    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()
        recipes = response.json()



        for recipe in recipes:
            print(f"GET all recipes: Name:{recipe['name']}, Minutes: {recipe['time_minutes']}")


    except ConnectTimeout as e:
        print(f"Connection timeout: {e}")
        return

    except HTTPError as e:
        print(f"HTTP error: {e}")
        return

    except Exception as e:
        print(f"Unexpected error: {e}")
        return


    #GET first recipe by ID
    try:
        first_recipe_id = recipes[0]["_id"]
        first_recipe_url = URL + "/" + first_recipe_id

        response_one_recipe = requests.get(
            first_recipe_url,
            timeout=10
        )

        response_one_recipe.raise_for_status()

        one_recipe = response_one_recipe.json()

        print(
            f"GET the first recipe: Name: {one_recipe['name']}, Cuisine: {one_recipe['cuisine']}, Time: {one_recipe['time_minutes']}")

    except ConnectTimeout as e:
        print(f"Connection timeout: {e}")
        return

    except HTTPError as e:
        print(f"HTTP error: {e}")
        return

    except Exception as e:
        print(f"Unexpected error: {e}")
        return

    #PUT first recipe
    try:
        updated_data = {
            "name": "Chakhokhbili",
            "cuisine": "Georgian",
            "time_minutes": "150"
        }

        response_put_first_recipe = requests.put(
            first_recipe_url,
            json=updated_data,
            timeout=10

        )
        response_put_first_recipe.raise_for_status()

        recipes_data[0] = updated_data

        with open("recipes.json", "w", encoding="utf-8") as file:
            json.dump(recipes_data, file, indent=2)

        print(f"The first recipe UPDATE status code: {response_put_first_recipe.status_code}")

    except ConnectTimeout as e:
        print(f"Connection timeout: {e}")
        return

    except HTTPError as e:
        print(f"HTTP error: {e}")
        return

    except Exception as e:
        print(f"Unexpected error: {e}")
        return


    #DELETE last recipe
    try:
        last_id = recipes[-1]["_id"]
        delete_url = URL + "/" + last_id

        response_delete_last_recipe = requests.delete(
            delete_url,
            timeout=10
        )

        response_delete_last_recipe.raise_for_status()

        print(f"The last recipe DELETE status code: {response_delete_last_recipe.status_code}")

        response = requests.get(URL, timeout=10)
        response.raise_for_status()
        recipes = response.json()

        for recipe in recipes:
            print(f"Print the remaining recipes after the last one deletion: Name: {recipe['name']}, Minutes: {recipe['time_minutes']}")

    except ConnectTimeout as e:
        print(f"Connection timeout: {e}")
        return

    except HTTPError as e:
        print(f"HTTP error: {e}")
        return

    except Exception as e:
        print(f"Unexpected error: {e}")
        return

main()


# import requests
#
# URL = "https://crudcrud.com/api/348ac379ffd1459abb2b634a5f19b6d7/recipes"
#
# response = requests.get(URL)
# recipes = response.json()
#
# for recipe in recipes:
#     recipe_id = recipe["_id"]
#     delete_url = URL + "/" + recipe_id
#
#     requests.delete(delete_url)