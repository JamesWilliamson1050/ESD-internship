import csv
import ntpath
import time

import pandas as pd


def readCSV(file):
    openSuccess = True
    try:
        if file.endswith('.csv'):

            with open(file, 'r', encoding='utf-8') as csv_file:
                df = pd.read_csv(file)
                findFilePath(file)


        else:
            raise Exception

    except Exception as e:
        print("Could not open CSV file. Please try another file")
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

    try:
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

    except Exception as e:
            print("CSV file not in the correct format. Must contain Module Description")
            raise e





# TODO improve the program to be more robust and not rely on specific names i.e 'Module Description'

def writeCSV(df):
    try:
        global filepath

        df.to_csv(filepath +'/keywordComparison.csv', sep=',', encoding="utf-8", index=False)
        print("done")
    except Exception:
        print("Could not write to CSV file ")


def findFilePath(file):
    global  filepath
    filepath, file = ntpath.split(file)


if __name__ == '__main__':
    filepath = ''
