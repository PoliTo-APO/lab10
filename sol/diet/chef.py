from diet.elements import Recipe


class Chef:
    def __init__(self, name: str, fav_recipe: Recipe) -> None:
        self._name = name
        self._fav_recipe = fav_recipe

    @property
    def name(self) -> str:
        return self._name

    @property
    def fav_recipe(self) -> Recipe:
        return self._fav_recipe
