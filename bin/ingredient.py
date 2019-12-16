class Ingredient(object):

    """ Conversion units for a single ingredient

    Attributes:
        ingredient: A string representing the name of the ingredient
        units: A string representing the number of units for the conversion
        ounces: A string representing the number of ounces for the conversion
        grams: An int representing the number of grams for the given oz/units
        modifiers: A list of strings modifying the ingredient.
            E.g. ["fresh", "dried", etc]
    """

    def __init__(self, ingredient, units, ounces, grams, modifiers=[]):
        self.ingredient = ingredient
        self.units = units
        self.ounces = ounces
        self.grams = grams
        self.modifiers = modifiers

    # Getter methods
    def get_ingredient(self):
        return self.ingredient

    def get_units(self):
        return self.units

    def get_ounces(self):
        return self.ounces

    def get_grams(self):
        return self.grams

    def get_modifiers(self):
        return self.modifiers

    """ String representation of the object

        Prints out a string formatted as:
            "{modifier} {ingredient} {units} {ounces} {grams}"

        If there are multiple modifiers, the string will be repeated several
        times with each modifier on a new line:
        {modifier1} {ingredient} {units} {ounces} {grams}
        {modifier2} {ingredient} {units} {ounces} {grams}
        ...
        {modifierN} {ingredient} {units} {ounces} {grams}
    """
    def __str__(self):
        return_string = ""
        # if there are at least one modifiers
        if len(self.modifiers) > 0:
            for i in range(len(self.modifiers)):
                return_string += "{0}|{1}|{2}|{3}|{4}".format(
                    self.modifiers[i],
                    self.ingredient,
                    self.units,
                    self.ounces, self.grams)
                if i < len(self.modifiers) - 1:
                    return_string += "\n"
        else:
            return_string = ("|{0}|{1}|{2}|{3}".
                             format(self.ingredient,
                                    self.units, self.ounces, self.grams))
        return return_string
