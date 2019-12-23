from bs4 import BeautifulSoup
import requests
import string
from conversion_and_format import *
from ingredient import Ingredient

URL = 'https://www.kingarthurflour.com/learn/ingredient-weight-chart'


def print_table(table):
    header = table[0]
    table.remove(header)
    print(header)
    for row in table:
        print_row(row)
    table.insert(0, header)
    return


# Format prints each row
def print_row(row):
    row.pretty_print()


def load_table_into_memory(url):

    page = requests.get(url)

    if not page.ok:
        print('ERROR LOADING PAGE')
        exit()

    # Create soup object
    soup = BeautifulSoup(page.text, 'lxml')

    # Find the table
    table = soup.find('table')

    # Create the header array

    tableHeader = [th.get_text() for th in table.find('thead')
                   .find('tr').find_all('th')]
    tableHeader.insert(0, "Modifier[s]")
    tableHeader[2] = "Volume (cups)"
    tableBody = [tableHeader]

    # Create the table body

    # for row in table
    for tr in table.find('tbody').find_all('tr'):
        line = []
        # First element is the name of the item
        rowName = tr.find('th').get_text()
        modifier = []

        # Split the modifiers away from the name. If there are multiple
        # modifiers each modifier is split into an element in an array.
        if '(' in rowName:
            splitIndex = rowName.find('(')
            modifier = rowName[splitIndex + 1: -1].split(',')

            # for each modifier, strip excess whitespace and unwanted character
            for i in range(len(modifier)):
                if "or" in modifier[i]:
                    modifier[i] = modifier[i].replace(' or', '')
                modifier[i] = modifier[i].strip()
            # Remove the modifier from the rowName
            rowName = rowName[0:splitIndex].strip()

        line.append(rowName)

        # Following elements are measurements. Append each cell in the
        # current line to the 'line' array
        for td in tr.find_all('td'):
            # The "".join(...) statement removes non-printable characters
            # from the cell before appending
            line.append("".join(filter(lambda x: x in string.printable,
                                       td.get_text())))

        ingredient = line[0]
        cups = convert_to_cup(line[1])
        ounces = format_weight(line[2])
        grams = format_weight(line[3])

        if len(modifier) < 1:
            modifier = ['']
        tableBody.append(Ingredient(ingredient, cups, ounces, grams, modifier))

    return tableBody

# END load_table_into_memory


def table_to_csv(ingredients, outputFile):
    with open(outputFile, 'w+') as f:
        header = ingredients.pop(0)
        f.write("|".join(header))
        f.write("\n")
        for i in range(len(ingredients)):
            f.write("{}".format(ingredients[i].__str__()))
            if (i < len(ingredients) - 1):
                f.write("\n")
# END table_to_csv


if __name__ == "__main__":
    table = load_table_into_memory(URL)
    print_table(table)
    # table_to_csv(table, "../resources/database.csv")
