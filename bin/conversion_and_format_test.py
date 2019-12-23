import unittest
from conversion_and_format import *


class Test_Conversion_And_Format(unittest.TestCase):

    """
    TEST CASES: is_metric
    """
    def test_is_metric_true(self):
        self.assertEqual(is_metric("mg"), True)

    def test_is_metric_false(self):
        self.assertEqual(is_metric("cup"), False)

    """
    TEST CASES: is_unit
    """

    def test_is_unit_true(self):
        self.assertEqual(is_convertable_unit("cup"), True)

    def test_is_unit_false(self):
        self.assertEqual(is_convertable_unit("1"), False)

    """
    TEST CASES: is_weight
    """

    def test_is_weight_true_metric(self):
        self.assertEqual(is_weight_unit("gram"), True)

    def test_is_weight_true_imperial(self):
        self.assertEqual(is_weight_unit("lb"), True)

    def test_is_weight_false_metric(self):
        self.assertEqual(is_weight_unit("ml"), False)

    def test_is_weight_false_imperial(self):
        self.assertEqual(is_weight_unit("cup"), False)

    """
    TEST CASES: replace_abbrev
    """

    def test_replace_abbrev_mg(self):
        self.assertEqual(replace_unit_abbrev("mg"), "milligram")

    def test_replace_abbrev_lb(self):
        self.assertEqual(replace_unit_abbrev("lb"), "pound")

    def test_replace_abbrev_egg(self):
        self.assertEqual(replace_unit_abbrev("egg"), "egg")

    """
    TEST CASES: convert_measure_to_smallest
    """

    def test_convert_measure_to_smallest_pound(self):
        self.assertEqual(convert_measure_to_smallest_metric(
            2.5, "pound"), (1133.98, "gram"))

    def test_convert_measure_to_smallest_kilogram(self):
        self.assertEqual(convert_measure_to_smallest_metric(2.5, "kilogram"),
                         (2500, "gram"))

    def test_convert_measure_to_smallest_cup(self):
        self.assertEqual(convert_measure_to_smallest_metric(
            2.5, "cup"), (591.47, "milliliter"))

    def test_convert_measure_to_smallest_liter(self):
        self.assertEqual(convert_measure_to_smallest_metric(
            2.5, "liter"), (2500, "milliliter"))

    def test_convert_measure_to_smallest_flounce(self):
        self.assertEqual(convert_measure_to_smallest_metric(
            2.5, "fluid ounce"), (73.93375, "milliliter"))

    def test_convert_measure_to_smallest_ml(self):
        self.assertEqual(convert_measure_to_smallest_metric(
            2.5, "milliliter"), (2.5, "milliliter"))

    """
    TEST CASES: prettify_measure_into_metric
    """

    def test_prettify_measure_into_metric_pound(self):
        self.assertEqual(prettify_measure_into_metric(
            2.5, "pound"), (1.13398, "kilogram"))

    def test_prettify_measure_into_metric_kilogram(self):
        self.assertEqual(prettify_measure_into_metric(2.5, "kilogram"),
                         (2.5, "kilogram"))

    def test_prettify_measure_into_metric_cup(self):
        self.assertEqual(prettify_measure_into_metric(
            25, "cup"), (5.91471, "milliliter"))

    def test_prettify_measure_into_metric_liter(self):
        self.assertEqual(prettify_measure_into_metric(
            2.5, "liter"), (2.5, "liter"))

    def test_prettify_measure_into_metric_flounce(self):
        self.assertEqual(prettify_measure_into_metric(
            40, "fluid ounce"), (1.18294, "milliliter"))

    def test_prettify_measure_into_metric_ml(self):
        self.assertEqual(prettify_measure_into_metric(
            2.5, "milliliter"), (2.5, "milliliter"))


def main():
    unittest.main()


if __name__ == "__main__":
    main()
