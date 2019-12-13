#!python3
from bs4 import BeautifulSoup
import requests
import string

def printTable(table):
  for row in table:
    printRow(row)
  return


# Format prints each row
def printRow(row):
  print("{0:<25} | {1:<39} | {2:<15} | {3:<6} | {4:<6} |".format(row[0], row[1], row[2], row[3], row[4]))
  print ("-" * (77 + 28))
  return


# Converts all measurements from tsp/Tbsp to cups
def convertToCup(string):
  string = string.lower()

  if ("tablespoon" in string or "teaspoon" in string):
    stringMeasurement = string[0:string.find('t')].strip()
    floatMeasurement = eval(stringMeasurement.replace(' ', '+'))

    if "tablespoon" in string:
      floatMeasurement = floatMeasurement / 16

    elif "teaspoon" in string:
      floatMeasurement = floatMeasurement / 48

  elif ("cup" in string):
    stringMeasurement = string[0:string.find('c')].strip()
    floatMeasurement = eval(stringMeasurement.replace(' ', '+'))
  else:
   return string

  return "{0:.2f}".format(floatMeasurement)



def loadTableIntoMemory(url):

  page = requests.get(url)

  if not page.ok:
    print('ERROR LOADING PAGE')
    exit()

  # Create soup object
  soup = BeautifulSoup(page.text, 'lxml')

  # Find the table
  table = soup.find('table')

  # Create the header array

  tableHeader = [th.get_text() for th in table.find('thead').find('tr').find_all('th')]
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

    # Split the modifiers away from the name. If there are multiple modifiers
    # each modifier is split into an element in an array.
    if '(' in rowName:
      splitIndex = rowName.find('(')
      modifier = rowName[splitIndex +1: -1].split(',')

      # for each modifier, strip excess whitespace and unwanted characters
      for i in range(len(modifier)):
        if "or" in modifier[i]:
          modifier[i] = modifier[i].replace(' or', '')
        modifier[i] = modifier[i].strip()
      # Remove the modifier from the rowName
      rowName = rowName[0:splitIndex].strip()
    line.append(rowName)

    # Following elements are measurements. Append each cell in the current line
    # to the 'line' array
    for td in tr.find_all('td'):
      # The "".join(...) statement removes non-printable characters from the cell before appending
      line.append("".join(filter(lambda x: x in string.printable, td.get_text())))

    if len(modifier) < 1:
      modifier = ['']
    for eachModifier in modifier:
      temp = line[:]
      temp.insert(0,eachModifier)
      tableBody.append(temp)
      temp = []

    # Append each line to the tableBody object. Each line is its own array
    #tableBody.append(line)


  return tableBody

## END loadTableIntoMemory

def formatTable(table):
  for i in range(len(table)):
    # Skip the header
    if i == 0:
      continue
    table[i][2] = convertToCup(table[i][2])
    if (table[i][3] != "" ):

      if ("to" in table [i][3]):
        temp = table[i][3].split(" to ")
        temp[0] = eval(temp[0].replace(' ', '+'))
        temp[1] = eval(temp[1].replace(' ', '+'))
        table[i][3] = (temp[0] + temp[1]) / 2
        continue
      table[i][3] = eval(table[i][3].replace(' ', '+'))
      #print (table[i][3])
  return table

def tableToCSV(table, outputFile):
  with open(outputFile, 'w') as file:
    for line in table:
      for cell in line:
        file.write("{}".format(cell))
      file.write("\n")



if __name__ == "__main__":
  table = loadTableIntoMemory('https://www.kingarthurflour.com/learn/ingredient-weight-chart')
  table = formatTable(table)
  # printTable(table)
  tableToCSV(table, "./csv.txt")


