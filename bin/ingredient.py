class Ingredient:

    def __init__(self, ingredient, cups, ounces, grams, modifiers=[]):
        self.ingredient = ingredient
        self.cups = cups
        self.ounces = ounces
        self.grams = grams
        self.modifiers = modifiers

        # if self.cups < 0:
        #     self.cups = 0
        # if self.ounces < 0:
        #     self.ounces = 0
        # if self.grams < 0:
        #     self.grams = 0

    def get_ingredient(self):
        return self.ingredient

    def get_cups(self):
        return self.cups

    def get_ounces(self):
        return self.ounces

    def get_grams(self):
        return self.grams

    def get_modifiers(self):
        return self.modifiers

    def __str__(self):
        return_string = ""
        # if there are at least one modifiers
        if len(self.modifiers) > 0:
            for i in range(len(self.modifiers)):
                return_string += "{0}|{1}|{2}|{3}|{4}".format(
                    self.modifiers[i],
                    self.ingredient,
                    self.cups,
                    self.ounces, self.grams)
                if i < len(self.modifiers) - 1:
                    return_string += "\n"
        else:
            return_string = ("|{0}|{1}|{2}|{3}".
                             format(self.ingredient,
                                    self.cups, self.ounces, self.grams))
        return return_string
