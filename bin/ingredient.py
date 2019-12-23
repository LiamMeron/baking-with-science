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

        return_string = ""
        # if there are at least one modifiers
        if len(self.modifiers) > 0:
            for i in range(len(self.modifiers)):
                return_string += "{0:<25} | {1:<39} "
                "| {2:<15} | {3:<6} | {4:<6} |\n".format(
                    self.modifiers[i],
                    self.ingredient,
                    self.units,
                    self.ounces,
                    self.grams)
                return_string += ("-" * (77 + 28))
                if i < len(self.modifiers) - 1:
                    return_string += "\n"

        else:
            return_string = ("{0:<25} | {1:<39} | {2:<15}"
                             " | {3:<6} | {4:<6} |\n".
                             format("", self.ingredient,
                                    self.units,
                                    self.ounces,
                                    self.grams))
            return_string += ("-" * (77 + 28))
        print(return_string)
    # END __INIT__

    def __str__(self):
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
    # END __STR__
