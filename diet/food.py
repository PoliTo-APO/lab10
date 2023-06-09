from typing import List, Optional
from diet.nutritional import NutritionalElement
from diet.elements import Recipe, Menu


class Food:
    def __init__(self):
        pass

    # R1
    def define_raw_material(self, name: str, calories: float, proteins: float, carbs: float, fats: float) -> None:
        pass

    @property
    def raw_materials(self) -> List[NutritionalElement]:
        pass

    def get_raw_material(self, name: str) -> NutritionalElement:
        pass

    # R2
    def define_product(self, name: str, calories: float, proteins: float, carbs: float, fats: float) -> None:
        pass

    @property
    def products(self) -> List[NutritionalElement]:
        pass

    def get_product(self, name: str) -> NutritionalElement:
        pass

    # R3
    def create_recipe(self, name: str) -> Recipe:
        pass

    @property
    def recipes(self) -> List[Recipe]:
        pass

    def get_recipe(self, name: str) -> Recipe:
        pass

    # R4
    def create_menu(self, name: str) -> Menu:
        pass

    # R5
    def add_chef(self, chef_name: str, fav_recipe: str, recipes: Optional[List[str]] = None) -> None:
        pass

    def chef_recognition(self, chef_name: str) -> List[str]:
        pass
