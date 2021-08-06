import csv
import os

import webscraper as ws
import pandas


# kw = __import__('web outputs without electives')


# Gets the file name
def inspectFile(fileName):
    csvExtension = '.csv'
    txtExtension = '.txt'

    if fileName.endswith(csvExtension):
        readFromCSV(fileName)
    elif fileName.endswith(txtExtension):
        readFromTxt(fileName)
    else:
        print("Sorry file is not in correct format. Make sure the file ends in .txt or .csv")


# Reads from a csv
def readFromCSV(csvfile):
    try:
        csv_file = open(csvfile, 'r')
    except:
        print("csv file could not be found")
    try:
        with csv_file:
            reader = csv.reader(csv_file)

            # Find out how to print column containing 'Module Title'. Probably just use an if
            for col in reader:

                # Lists of possible ways the module title and description could be spelled
                moduleTitle = ['Module Title', 'module title', 'Module title', 'module Title', 'Title', 'title']
                moduleDescription = ['Module Description', 'module Description', 'Module Description',
                                     'module Description',
                                     'Description', 'description']

                # These lines check if any of the module titles and description are in the csv file
                matchModuleTitle = next((mt for mt in moduleTitle if mt in col), False)
                matchModuleDesc = next((md for md in moduleDescription if md in col), False)

                # Gets the index of the module title
                if matchModuleTitle:
                    indexMT = col.index(matchModuleTitle)

                # Gets the index of the module description
                if matchModuleDesc:
                    indexMD = col.index(matchModuleDesc)

                print(col[indexMT], col[indexMD])

        csv_file.close()

    except:
        print("CSV file not in correct format")


# Reads from a text file
def readFromTxt(txtfile):
    try:
        with open(txtfile, 'r') as txt_file:
            for i in txt_file:
                print(i)
            txt_file.close()
    except:
        print("Text file opened")


# Runs the program
if __name__ == '__main__':
    inspectFile('test.csv')

    # ws.main()

    # Get users to enter file name
    # If file ends in txt read from text file
    # If file ends in csv read from csv
    # If file does not have an ending either let user choose to write to csv or text file  or both
    # Web scrape data where possible
    # Write web scraped data to chosen file type
    # Then read from file and compare to keywords csv
