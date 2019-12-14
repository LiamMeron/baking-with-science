import unittest
from ingredient import Ingredient


class TestIngredientMethods(unittest.TestCase):
    def make_ingredient_no_modifier():
        ingred = "All-Purpose Flour"
        cups = 1
        ounces = 4.25
        grams = 120
        return Ingredient(ingred, cups,
                          ounces, grams)

    def make_ingredient_one_modifier():
        ingred = "Salt"
        cups = 0.06
        ounces = ''
        grams = 16
        modifiers = ["Morton's Kosher"]
        return Ingredient(ingred, cups,
                          ounces, grams, modifiers)

    def make_ingredient_two_modifiers():
        ingred = "Apples"
        cups = "1.00"
        ounces = "3.00"
        grams = 85
        modifiers = ["dried", "diced"]
        return Ingredient(ingred, cups,
                          ounces, grams, modifiers)

    def test_get_ingredient_no_modifier(self):
        ingred = TestIngredientMethods.make_ingredient_no_modifier()
        self.assertEqual(ingred.__str__(), "|All-Purpose "
                         "Flour|1|4.25|120")

    def test_get_ingredient_one_modifier(self):
        ingred = TestIngredientMethods.make_ingredient_one_modifier()
        self.assertEqual(ingred.__str__(), "Morton's Kosher|Salt|0.06||16")

    def test_get_ingredient_two_modifiers(self):
        ingred = TestIngredientMethods.make_ingredient_two_modifiers()
        self.assertEqual(ingred.__str__(),
                         "dried|Apples|1.00|3.00|85" +
                         "\ndiced|Apples|1.00|3.00|85")


if __name__ == "__main__":
    unittest.main()
