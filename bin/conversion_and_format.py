from fractions import Fraction

METRIC_UNITS_VOLUME = {
    "milliliter": "milliliter",
    "ml": "milliliter",
    "liter": "liter",
    "l": "liter",
    "litre": "liter"
}
IMPERIAL_UNITS_VOLUME = {
    "gallon": "gallon",
    "gal": "gallon",
    "quart": "quart",
    "qt": "quart",
    "pint": "pint",
    "pt": "pint",
    "cup": "cup",
    "c": "cup",
    "teaspoon": "teaspoon",
    "tsp": "teaspoon",
    "tablespoon": "tablespoon",
    "tbsp": "tablespoon",
    "fluid ounce": "fluid ounce",
    "fl oz": "fluid ounce",
    "fl. oz": "fluid ounce"
}
METRIC_UNITS_WEIGHT = {
    "gram": "gram",
    "g": "gram",
    "milligram": "milligram",
    "mg": "milligram",
    "kilogram": "kilogram",
    "kg": "kilogram",
    "kilo": "kilogram"
}
IMPERIAL_UNITS_WEIGHT = {
    "pound": "pound",
    "lb": "pound",
    "#": "pound",
    "ounce": "ounce",
    "oz": "ounce"
}

IMPERIAL_VOLUME_TO_ML = {
    "gallon": 3785.41,
    "quart": 946.353,
    "pint": 473.176,
    "cup": 236.588,
    "fluid ounce": 29.5735,
    "tablespoon": 14.7868,
    "teaspoon": 4.92892,
}

IMPERIAL_WEIGHT_TO_G = {
    "pound": 453.592,
    "ounce": 28.3495
}

METRIC_VOLUME_TO_ML = {
    "liter": 1000,
    "milliliter": 1
}

METRIC_WEIGHT_TO_G = {
    "kilogram": 1000,
    "gram": 1
}

ALL_UNITS = {}
ALL_UNITS.update(METRIC_UNITS_VOLUME)
ALL_UNITS.update(IMPERIAL_UNITS_VOLUME)
ALL_UNITS.update(METRIC_UNITS_WEIGHT)
ALL_UNITS.update(IMPERIAL_UNITS_WEIGHT)


def replace_unit_abbrev(unit):
    if unit in ALL_UNITS:
        return ALL_UNITS.get(unit)
    return unit


# TODO
def convert_measure_to_smallest_metric(quantity, unit):
    """
    Converts a given measurement into the metric equivalent

    measure_in (str): the unit
    """
    if is_metric(unit):
        if is_weight_unit(unit):
            quantity, unit = metric_weight_to_g(quantity, unit)
        elif is_volume_unit(unit):
            quantity, unit = metric_volume_to_ml(quantity, unit)
    elif is_imperial(unit):
        if is_weight_unit(unit):
            quantity, unit = imperial_weight_to_g(quantity, unit)
        elif is_volume_unit(unit):
            quantity, unit = imperial_volume_to_ml(quantity, unit)

    return (quantity, unit)


def prettify_measure_into_metric(quantity, unit):
    if is_volume_unit(unit):
        quantity, unit = convert_ml_to_largest_metric(quantity, unit)
    elif is_weight_unit(unit):
        quantity, unit = convert_gram_to_largest_metric(quantity, unit)


def prettify_measure_into_imperial(quantity, unit):
    if is_volume_unit(unit):
        quantity, unit = convert_ml_to_largest_imperial(quantity, unit)
    elif is_weight_unit(unit):
        quantity, unit = convert_gram_to_largest_imperial(quantity, unit)


def convert_gram_to_largest_metric(quantity, unit):
    return convert_smallest_unit_to_largest_unit(quantity, unit, METRIC_WEIGHT_TO_G)


def convert_ml_to_largest_metric(quantity, unit):
    return convert_smallest_unit_to_largest_unit(quantity, unit, METRIC_VOLUME_TO_ML)


def convert_gram_to_largest_imperial(quantity, unit):
    return convert_smallest_unit_to_largest_unit(quantity, unit, IMPERIAL_WEIGHT_TO_G)


def convert_ml_to_largest_imperial(quantity, unit):
    return convert_smallest_unit_to_largest_unit(quantity,
                                          unit, IMPERIAL_VOLUME_TO_ML)


def convert_smallest_unit_to_largest_unit(quantity, unit, dictionary):
    smallest_q = quantity
    smallest_u = unit
    for (q, u) in dictionary:
        if quantity / q >= 1 and quantity / q < smallest_q:
            smallest_q, smallest_u = q, u
    return (smallest_q, smallest_u)


def imperial_weight_to_g(quantity, unit):
    quantity = quantity * IMPERIAL_WEIGHT_TO_G.get(unit)
    unit = "gram"
    return (quantity, unit)


def imperial_volume_to_ml(quantity, unit):
    quantity = quantity * IMPERIAL_VOLUME_TO_ML.get(unit)
    unit = "milliliter"
    return (quantity, unit)


def metric_weight_to_g(quantity, unit):
    quantity = METRIC_WEIGHT_TO_G.get(unit) * quantity
    unit = "gram"
    return (quantity, unit)


def metric_volume_to_ml(quantity, unit):
    quantity = quantity * METRIC_VOLUME_TO_ML.get(unit)
    unit = "milliliter"
    return (quantity, unit)


def is_weight_unit(unit):
    if (unit in METRIC_UNITS_WEIGHT.keys() or
            unit in IMPERIAL_UNITS_WEIGHT.keys()):
        return True
    return False


def is_volume_unit(unit):
    if (
        unit in METRIC_UNITS_VOLUME.keys() or
        unit in IMPERIAL_UNITS_VOLUME.keys()
    ):
        return True
    return False


def is_metric(unit):
    if (
        unit in METRIC_UNITS_VOLUME.keys() or
        unit in METRIC_UNITS_WEIGHT.keys()
    ):
        return True
    return False


def is_imperial(unit):
    if (
        unit in IMPERIAL_UNITS_VOLUME.keys() or
        unit in IMPERIAL_UNITS_WEIGHT.keys()
    ):
        return True
    return False


def is_convertable_unit(unit):
    if unit in ALL_UNITS:
        return True
    return False


def get_measure(ingredient_str):
    """
    ingredient_str: formatted string of ingredient
    RETURNS a tuple (quantity, unit)
    """
    sentence_length = len(ingredient_str)
    for i in range(sentence_length):
        word = ingredient_str[i]
        if word.isnumeric():
            quantity = float(word)
        if word in ALL_UNITS:
            unit = word
    return (quantity, unit)


def convert_to_cup(measurement_in):
    measurement_in = measurement_in.lower()

    # If measurement contains an empty string
    if not measurement_in.strip():
        return 0

    if ("tablespoon" in measurement_in or "teaspoon" in measurement_in):
        string_measurement = measurement_in[0:measurement_in.find('t')].strip()
        float_measurement = eval(string_measurement.replace(' ', '+'))

        # Convert tablespoon to cups
        if "tablespoon" in measurement_in:
            float_measurement = float_measurement / 16

        # Convert teaspoon to cups
        elif "teaspoon" in measurement_in:
            float_measurement = float_measurement / 48

    # Convert cups from measurement_in to int
    elif ("cup" in measurement_in):
        string_measurement = measurement_in[0:measurement_in.find('c')].strip()
        float_measurement = eval(string_measurement.replace(' ', '+'))

    # Units may not be in tsp/Tbsp/C: E.g. "1 Large Egg"
    else:
        return measurement_in

    return "{0:.2f}".format(float_measurement)


def format_weight(weight):
    if not isinstance(weight, str):
        return weight

    if ("to" in weight):
        temp = weight.split(" to ")
        temp[0] = sum(Fraction(s) for s in temp[0].split(' '))
        temp[1] = sum(Fraction(s) for s in temp[1].split(' '))
        weight = "{0:.2f}".format(float((temp[0] + temp[1]) / 2))
    elif (' ' in weight):
        if not weight.strip():
            weight = 0
            return weight
        weight = "{0:.2f}".format(
            (float(sum(Fraction(s) for s in weight.split(' ')))))
    elif weight.strip():
        weight = "{0:.2f}".format(float(Fraction(weight)))
    else:
        return 0
    return weight
