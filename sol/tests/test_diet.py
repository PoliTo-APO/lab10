import unittest
from diet.food import Food


class TestR1(unittest.TestCase):

    def test_get_raw_material(self):
        food = Food()
        food.define_raw_material("Salt", 3, 2.1, 1, 0)
        s = food.get_raw_material("Salt")
        self.assertEqual("Salt", s.name)

    def test_raw_materials(self):
        food = Food()
        food.define_raw_material("Salt", 3, 2.1, 1, 0)
        food.define_raw_material("Rice", 300, 9, 65.6, 3)
        self.assertEqual(len(food.raw_materials), 2)
        self.assertEqual(food.raw_materials[0].name, "Rice")
        self.assertEqual(food.raw_materials[1].name, "Salt")

    def test_properties(self):
        food = Food()
        food.define_raw_material("Salt", 3, 2.1, 1, 0)
        s = food.get_raw_material("Salt")
        self.assertEqual("Salt", s.name)
        self.assertAlmostEqual(3, s.calories)
        self.assertAlmostEqual(2.1, s.proteins)
        self.assertAlmostEqual(1, s.carbs)
        self.assertAlmostEqual(0, s.fats)
        self.assertEqual(True, s.per100g)

    def test_exception(self):
        food = Food()
        food.define_raw_material("Salt", 3, 2.1, 1, 0)
        with self.assertRaises(ValueError):
            food.define_raw_material("Salt", 3, 3, 3, 3)


class TestR2(unittest.TestCase):

    def test_get_product(self):
        food = Food()
        food.define_product("Brioche", 125, 7.5, 23.7, 45.1)
        b = food.get_product("Brioche")
        self.assertEqual("Brioche", b.name)

    def test_raw_materials(self):
        food = Food()
        food.define_product("Icecream cone", 150, 11.2, 10.1, 54.8)
        food.define_product("Brioche", 125, 7.5, 23.7, 45.1)
        self.assertEqual(len(food.products), 2)
        self.assertEqual(food.products[0].name, "Brioche")
        self.assertEqual(food.products[1].name, "Icecream cone")

    def test_properties(self):
        food = Food()
        food.define_product("Brioche", 125, 7.5, 23.7, 45.1)
        s = food.get_product("Brioche")
        self.assertEqual("Brioche", s.name)
        self.assertAlmostEqual(125, s.calories)
        self.assertAlmostEqual(7.5, s.proteins)
        self.assertAlmostEqual(23.7, s.carbs)
        self.assertAlmostEqual(45.1, s.fats)
        self.assertEqual(False, s.per100g)

    def test_exception(self):
        food = Food()
        food.define_product("Brioche", 125, 7.5, 23.7, 45.1)
        with self.assertRaises(ValueError):
            food.define_product("Brioche", 3, 3, 3, 3)


class TestR3(unittest.TestCase):

    def setUp(self):
        self._food = Food()
        self._food.define_raw_material("Salt", 3, 2.1, 1, 0)
        self._food.define_raw_material("Rice", 300, 9, 65.6, 3)
        self._food.define_raw_material("Zafferano", 12, 2, 34.3, 12.4)

    def test_create_recipe(self):
        r = self._food.create_recipe("Riso allo zafferano")
        self.assertEqual("Riso allo zafferano", r.name)

    def test_get_recipe(self):
        self._food.create_recipe("Riso allo zafferano")
        r = self._food.get_recipe("Riso allo zafferano")
        self.assertEqual("Riso allo zafferano", r.name)

    def test_recipes(self):
        self._food.create_recipe("Ricetta1")
        self._food.create_recipe("Ricetta2")
        recipes = self._food.recipes
        self.assertEqual(2, len(recipes))
        recipe_names = [r.name for r in recipes]
        self.assertTrue("Ricetta1" in recipe_names)
        self.assertTrue("Ricetta2" in recipe_names)

    def test_representation(self):
        r = self._food.create_recipe("Riso allo zafferano")
        r.add_ingredient("Salt", 5.7).add_ingredient("Rice", 120).add_ingredient("Zafferano", 3.6)
        repr_list = r.__repr__().split("\n")
        repr_list = [elm for elm in repr_list if elm]
        self.assertEqual(len(repr_list), 3)
        self.assertTrue("Salt 5.7" in repr_list)
        self.assertTrue("Rice 120.0" in repr_list)
        self.assertTrue("Zafferano 3.6" in repr_list)

    def test_properties(self):
        r = self._food.create_recipe("Riso allo zafferano")
        r.add_ingredient("Salt", 5.7).add_ingredient("Rice", 120).add_ingredient("Zafferano", 3.6)

        self.assertAlmostEqual(r.calories,  278.9, places=1)
        self.assertAlmostEqual(r.proteins, 8.5, places=1)
        self.assertAlmostEqual(r.carbs, 61.9, places=1)
        self.assertAlmostEqual(r.fats, 3.1, places=1)
        self.assertEqual(r.per100g, True)

    def test_properties_lambda(self):
        r = self._food.create_recipe("Riso allo zafferano")
        r.add_ingredient("Salt", 5.7).add_ingredient("Rice", 120).add_ingredient("Zafferano", 3.6)

        self.assertAlmostEqual(r.calculate_nutritional_value(lambda x: x.calories), 278.9, places=1)
        self.assertAlmostEqual(r.calculate_nutritional_value(lambda x: x.proteins), 8.5, places=1)
        self.assertAlmostEqual(r.calculate_nutritional_value(lambda x: x.carbs), 61.9, places=1)
        self.assertAlmostEqual(r.calculate_nutritional_value(lambda x: x.fats), 3.1, places=1)


class TestR4(unittest.TestCase):

    def setUp(self):
        self._food = Food()
        self._food.define_raw_material("Salt", 3, 2.1, 1, 0)
        self._food.define_raw_material("Rice", 300, 9, 65.6, 3)
        self._food.define_raw_material("Zafferano", 12, 2, 34.3, 12.4)
        self._food.define_product("Brioche", 125, 7.5, 23.7, 45.1)
        r = self._food.create_recipe("Riso allo zafferano")
        r.add_ingredient("Salt", 5.7).add_ingredient("Rice", 120).add_ingredient("Zafferano", 3.6)

    def test_create_menu(self):
        m = self._food.create_menu("Menù1")
        self.assertEqual(m.name, "Menù1")

    def test_properties(self):
        m = self._food.create_menu("Menù1")
        self.assertEqual(m.name, "Menù1")
        m.add_recipe("Riso allo zafferano", 150)
        m.add_product("Brioche")

        self.assertAlmostEqual(m.calories, 543.3, places=1)
        self.assertAlmostEqual(m.proteins, 20.3, places=1)
        self.assertAlmostEqual(m.carbs, 116.5, places=1)
        self.assertAlmostEqual(m.fats, 49.8, places=1)
        self.assertEqual(m.per100g, False)


class TestR5(unittest.TestCase):
    def setUp(self):
        self._food = Food()
        self._food.create_recipe("R1")
        self._food.create_recipe("R2")
        self._food.create_recipe("R3")
        self._food.create_recipe("R4")
        self._food.create_recipe("R5")
        self._food.create_recipe("R6")
        self._food.create_recipe("R7")
        self._food.create_recipe("R8")
        self._food.create_recipe("R9")
        self._food.create_recipe("R10")

        self._food.create_recipe("R11")
        self._food.create_recipe("R12")
        self._food.create_recipe("R13")

        self._food.add_chef("CH1", "R5", ["R1", "R2"])
        self._food.add_chef("CH2", "R7", ["R3", "R4"])
        self._food.add_chef("CH3", "R4", ["R5"])
        self._food.add_chef("CH4", "R2", ["R6", "R7", "R8"])
        self._food.add_chef("CH5", "R8", ["R9", "R10"])
        self._food.add_chef("CH6", "R7", [])

        self._food.add_chef("CH7", "R12", ["R11"])
        self._food.add_chef("CH8", "R13", ["R12"])
        self._food.add_chef("CH9", "R12", ["R13"])

    def test_chef_recognition(self):
        self.assertEqual(["CH4", "CH1", "CH3", "CH2"], self._food.chef_recognition("CH4"))

    def test_chef_recognition_alt(self):
        self.assertEqual(["CH2", "CH4", "CH1", "CH3"], self._food.chef_recognition("CH2"))

    def test_chef_recognition_alt2(self):
        self.assertEqual(["CH3", "CH2", "CH4", "CH1"], self._food.chef_recognition("CH3"))

    def test_chef_recognition_false(self):
        self.assertEqual([], self._food.chef_recognition("CH5"))

    def test_chef_recognition_false_alt(self):
        self.assertEqual([], self._food.chef_recognition("CH6"))

    def test_chef_recognition_loop(self):
        self.assertEqual([], self._food.chef_recognition("CH7"))





