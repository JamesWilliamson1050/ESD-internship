import csv
import time

import pandas as pd


# Read in csv file
def readCSV(csvfile):
    # Used to check if file is opened successfully
    openSuccess = True
    try:
        # Check if file is csv file
        if csvfile.endswith('.csv'):

            with open(csvfile, 'r', encoding='utf-8') as csv_file:
                df = pd.read_csv(csvfile)

        else:
            raise Exception

    except Exception:
        e = Exception
        print("Could not open CSV file")
        openSuccess = False

    # if file is csv file
    if openSuccess:
        # Create a header for all 17 SDGs
        for sdgNo in range(1, 18):
            sdgHeader = 'SDG' + str(sdgNo)
            df[sdgHeader] = ''
        for index, row in df.iterrows():
            filterKeywords(row, df)

        writeCSV(df)


def filterKeywords(row, df):
    sdg = {}

    # Looks for header called 'Module Description'
    moduleDescription = str(row['Module Description'])

    # Set module description to lower case and remove any whitespace
    moduleDescription = moduleDescription.lower().strip()
    with open("KEYWORDS.csv") as keywords_file:

        # Creates a list for every sdg containing all the keywords and phrases
        for inc, line in enumerate(keywords_file.readlines()):
            sdgNow = [word for word in line.lower().strip().split(',') if word not in ['', '\n', ' ']]
            sdg[inc + 1] = sdgNow

    keywords_file.close()

    # Compares a module description to the sdg keywords. Marks "YES" if a keyword/phrase is in the module description else it marks "NO"
    for index in sdg.keys():

        if any(word in moduleDescription for word in sdg[index]):
            row['SDG' + str(index)] = "YES"
        else:
            row['SDG' + str(index)] = "NO"


# TODO improve the program to be more robust and not rely on specific names i.e 'Module Description'

# Writes to csv file
def writeCSV(df):
    try:
        df.to_csv('Test3.csv', sep=',', encoding="utf-8", index=False)
    except Exception:
        print("Could not write to CSV file ")


if __name__ == '__main__':
    readCSV('moduleInfoAll.csv')
