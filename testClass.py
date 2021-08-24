import csv
import time

import pandas as pd

def readCSV(csvfile):
    try:
        with open (csvfile, 'r', encoding='utf-8') as csv_file:
           pass
        df = pd.read_csv(csvfile)
    except Exception:
        e = Exception
        print("Could not open CSV file")

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






def writeCSV(df):
    try:
        df.to_csv('Test3.csv', sep=',', encoding="utf-8", index=False)
    except Exception:
        print("Could not write to CSV file ")

if __name__ == '__main__':

    readCSV('moduleInfoAll.csv')
