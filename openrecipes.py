import pprint


def read_recipes_from_file(file_path):
    cook_book = {}

    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.read().split("\n\n")

    for block in lines:
        block_lines = block.splitlines()
        if len(block_lines) >= 3:
            recipe_name = block_lines[0].strip()
            number_of_ingredients = int(block_lines[1])
            ingredients = block_lines[2:]

            cook_book[recipe_name] = []
            for ingredient_line in ingredients:
                parts = ingredient_line.split(" | ")
                ingredient_name = parts[0].strip()
                quantity = int(parts[1])
                measure = parts[2].strip()

                cook_book[recipe_name].append(
                    {
                        "ingredient_name": ingredient_name,
                        "quantity": quantity,
                        "measure": measure,
                    }
                )

    return cook_book


# Пример использования функции
file_path = "recipes.txt"
cook_book = read_recipes_from_file(file_path)
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(cook_book)
