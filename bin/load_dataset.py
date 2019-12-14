from bs4 import BeautifulSoup
import requests
import string
from conversion_and_format import *
from ingredient import Ingredient

URL = 'https://www.kingarthurflour.com/learn/ingredient-weight-chart'

def print_table(table):
    for row in table:
        print_row(row)
    return


# Format prints each row
def print_row(row):
    print(("{0:<25} | {1:<39} | {2:<15} | {3:<6} | {4:<6} |"
           .format(row[0], row[1], row[2], row[3], row[4])))
    print("-" * (77 + 28))
    return


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





if __name__ == "__main__":
    table = load_table_into_memory(URL)

    table_to_csv(table, "../resources/database.csv")
