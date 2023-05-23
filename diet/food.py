from typing import List, Optional
from diet.nutritional import NutritionalElement
from diet.elements import RawMaterial, Product, Recipe, Menu
from diet.chef import Chef


class Food:
    def __init__(self):
        self._materials = {}
        self._products = {}
        self._recipes = {}
        self._chefs = {}

    # R1
    def define_raw_material(self, name: str, calories: float, proteins: float, carbs: float, fats: float) -> None:
        if name in self._materials:
            raise ValueError("Raw material already present")
        self._materials[name] = RawMaterial(name, calories, proteins, carbs, fats)

    @property
    def raw_materials(self) -> List[NutritionalElement]:
        # creo lista raw_materials (valori dizionario)
        raw_materials = list(self._materials.values())
        # creo lambda che, dato un raw material, ne ritorna il nome
        # uso la lambda come chiave ordinamento, così i raw material sono ordinate per nome
        raw_materials.sort(key=lambda recipe: recipe.name)
        return raw_materials

    def get_raw_material(self, name: str) -> NutritionalElement:
        return self._materials[name]

    # R2
    def define_product(self, name: str, calories: float, proteins: float, carbs: float, fats: float) -> None:
        if name in self._products:
            raise ValueError("Product already present")
        self._products[name] = Product(name, calories, proteins, carbs, fats)

    @property
    def products(self) -> List[NutritionalElement]:
        # creo lista prodotti (valori dizionario)
        product_list = list(self._products.values())
        # ordino lista prodotti sfruttando __lt__ (metodo alternativo alla lambda)
        product_list.sort()
        return product_list

    def get_product(self, name: str) -> NutritionalElement:
        return self._products[name]

    # R3
    def create_recipe(self, name: str) -> Recipe:
        recipe = Recipe(name, self)
        self._recipes[name] = recipe
        return recipe

    @property
    def recipes(self) -> List[Recipe]:
        return list(self._recipes.values())

    def get_recipe(self, name: str) -> Recipe:
        return self._recipes[name]

    # R4
    def create_menu(self, name: str) -> Menu:
        return Menu(name, self)

    # R5
    def add_chef(self, chef_name: str, fav_recipe: str, recipes: Optional[List[str]] = None) -> None:
        chef = Chef(chef_name, self._recipes[fav_recipe])
        self._chefs[chef_name] = chef
        if recipes:
            for recipe in recipes:
                self._recipes[recipe].chef = chef

    def chef_recognition(self, chef_name: str) -> List[str]:
        chef = self._chefs[chef_name]
        circle = []
        visited = set()
        self._loop_finder(chef, chef, circle, visited)
        return circle

    def _loop_finder(self, start_chef, curr_chef: Chef, circle: List[str], visited: set[str]) -> bool:
        visited.add(curr_chef.name)
        circle.append(curr_chef.name)
        curr_chef = curr_chef.fav_recipe.chef
        if curr_chef.name == start_chef.name:
            return True
        if curr_chef.name not in visited:
            if self._loop_finder(start_chef, curr_chef, circle, visited):
                return True
        circle.pop()
        return False
