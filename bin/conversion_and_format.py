from fractions import Fraction

def convert_to_cup(measurement_in):
    measurement_in = measurement_in.lower()

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
    else:
        return measurement_in

    return "{0:.2f}".format(float_measurement)

def format_weight(weight):

    if ("to" in weight):
        temp = weight.split(" to ")
        temp[0] = float(sum(Fraction(s) for s in temp[0].split(' ')))
        temp[1] = float(sum(Fraction(s) for s in temp[1].split(' ')))
        weight = "{0:.2f}".format((temp[0] + temp[1]) / 2)
    elif (' ' in weight):
        weight = "{0:.2f}".format(
            (float(sum(Fraction(s) for s in weight.split(' ')))))
    elif (weight):
        weight = "{0:.2f}".format(float(Fraction(weight)))
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
