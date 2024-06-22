import os
import random
import PyPDF2


def extract_text(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text


def search_by_ingredient(folder_path, ingredient):
    recipes = {}
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(folder_path, filename)
            text = extract_text(pdf_path)
            if ingredient.lower() in text.lower():
                recipes[filename] = text
    return recipes


def search_by_time(folder_path, time_needed):
    recipes = {}
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(folder_path, filename)
            text = extract_text(pdf_path)
            if f'{time_needed} minutes' in text.lower() or f'{time_needed} mins' in text.lower():
                recipes[filename] = text
    return recipes


def get_all_recipes(folder_path):
    recipes = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            recipes.append(filename)
    return recipes


def get_random_recipes(recipes, num_days):
    return random.sample(recipes, num_days)


def search_recipes_by_ingredient(folder_path):
    ingredient = input("Search by ingredient: ")
    ingredient_results = search_by_ingredient(folder_path, ingredient)

    print(f"Recipes containting '{ingredient}': ")
    for recipe in ingredient_results:
        print(recipe)


def search_recipes_by_time(folder_path):
    time_needed = input("Search by time to make recipe: ")
    time_results = search_by_time(folder_path, time_needed)

    print(f"\nRecipes that take '{time_needed}' minutes: ")
    for recipe in time_results:
        print(recipe)


def meal_planning(folder_path):
    all_recipes = get_all_recipes(folder_path)

    while True:
        try:
            num_days = int(input("Enter the number of days you need meal planning for: "))
            if num_days > len(all_recipes):
                print(f"Number of days requested exceeds available recipes ({len(all_recipes)}). ")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number. ")

    random_recipes = get_random_recipes(all_recipes, num_days)

    print(f"\nRandom recipes for the next {num_days} days: ")
    for day, recipe in enumerate(random_recipes, 1):
        print(f"Day {day}: {recipe} ")


def main():
    folder_path = 'C:\\Users\\nicol\\OneDrive\\Desktop\\Recipes Github Project\\'

    while True:
        print("\nRecipe App Menu: ")
        print("1. Search by Ingredient")
        print("2. Search by Time")
        print("3. Meal Planner")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            search_recipes_by_ingredient(folder_path)
        elif choice == '2':
            search_recipes_by_time(folder_path)
        elif choice == '3':
            meal_planning(folder_path)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
