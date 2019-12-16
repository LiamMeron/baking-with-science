from fractions import Fraction


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


def table_to_csv(ingredients, outputFile):
    with open(outputFile, 'w+') as f:
        header = ingredients.pop(0)
        f.write("|".join(header))
        f.write("\n")
        for i in range(len(ingredients)):
            f.write("{}".format(ingredients[i].__str__()))
            if (i < len(ingredients) - 1):
                f.write("\n")
