import csv
import time

import pandas as pd


def readCSV(csvfile):
    openSuccess = True
    try:
        if csvfile.endswith('.csv'):

            with open(csvfile, 'r', encoding='utf-8') as csv_file:
                df = pd.read_csv(csvfile)

        else:
            raise Exception

    except Exception:
        e = Exception
        print("Could not open CSV file")
        openSuccess = False

    if openSuccess:
        for sdgNo in range(1, 18):
            sdgHeader = 'SDG' + str(sdgNo)
            df[sdgHeader] = ''
        for index, row in df.iterrows():
            filterKeywords(row, df)

        writeCSV(df)




def filterKeywords(row, df):
    sdg = {}
    output = {}
    moduleDescription = str(row['Module Description'])
    moduleDescription = moduleDescription.lower().strip()
    with open("KEYWORDS.csv") as keywords_file:

        for inc, line in enumerate(keywords_file.readlines()):
            sdgNow = [word for word in line.lower().strip().split(',') if word not in ['', '\n', ' ']]
            sdg[inc + 1] = sdgNow

    keywords_file.close()

    sdgList = []

    for index in sdg.keys():

        if any(word in moduleDescription for word in sdg[index]):
            row['SDG' + str(index)] = "YES"
        else:
            row['SDG' + str(index)] = "NO"


# TODO improve the program to be more robust and not rely on specific names i.e 'Module Description'

def writeCSV(df):
    try:
        df.to_csv('Test3.csv', sep=',', encoding="utf-8", index=False)
    except Exception:
        print("Could not write to CSV file ")


if __name__ == '__main__':
    readCSV('KEYWORDS.csv')
