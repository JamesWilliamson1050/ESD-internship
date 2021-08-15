import csv
import wordFilter

import pandas as pd
from comtypes.safearray import numpy


def updateModuleData(webScrapedcsvFile):
    df = pd.read_csv(webScrapedcsvFile, sep=',', encoding="utf-8")

    df['Module Code'] = ''
    df['Module Level'] = ''


    for index, row in df.iterrows():
        moduleTitle = df.loc[index]['Module Title']
        moduleSearch = searchUndergraduateClassList(moduleTitle)
        moduleCode = moduleSearch[0]
        moduleLevel = moduleSearch[1]
        moduleCodeType = type(moduleCode)



        if moduleCodeType == str:
            df.at[index, 'Module Code'] = moduleCode
            df.at[index, 'Module Level'] = moduleLevel
        elif moduleCodeType == numpy.ndarray:
            for i in range(len(moduleCode)):
               tempRow = row
               tempRow['Module Code', 'Module Level'] =[moduleCode[i], moduleLevel[i]]
               df.append(tempRow)
        else:
            if 'And' in moduleTitle:
                print(moduleTitle)
                moduleTitle = wordFilter.andFilter(moduleTitle)
                print(moduleTitle)

            # Add in filtering code and search for the data again
                break










def readUGCSV():
        try:
            df = pd.read_csv('Class List Undergraduate 21-22.csv', sep=',', encoding="utf-8")
            header_row = 7

            df.columns = df.iloc[header_row]
            return df
        except Exception:
            print("Undergraduate CSV file not found")
        df.close()



def searchUndergraduateClassList(moduleTitle):
    df = readUGCSV()
    search = df['TITLE'] == moduleTitle
    moduleCodes = df.loc[search]['CODE']
    moduleCode = moduleCodes.values
    moduleLevels = df.loc[search]['LEVEL']
    moduleLevel = moduleLevels.values

    if moduleCode.size == 0:
        moduleCode = None
        moduleLevel = None
    elif moduleCode.size == 1:
        moduleCode = moduleCode[0]
        moduleLevel = moduleLevel[0]


    return moduleCode, moduleLevel


def writeToCSV(dataframe):
    print()


undergraduateList = []


# Used to fill in the undergraduate List
def fillUndergraduateList():
    with open('Class List Undergraduate 21-22.csv', 'r', encoding="utf-8") as undergraduateCSV:
        reader = csv.reader(undergraduateCSV)

        for row in reader:
            if len(row) > 2:
                undergraduateList.append(row)

    undergraduateCSV.close()


def searchUndergraduate(moduleSearchUG):
    # Returns the code and level of a course found in the class catalogue csv file

    for mod in undergraduateList:
        if 'TITLE' in mod:
            titleIndex = mod.index('TITLE')
            print(titleIndex)
            title = mod[titleIndex]
            print(title)


if __name__ == '__main__':

    # fillUndergraduateList()
    # searchUndergraduate('Year 3 Pedagogy And Placement Learning - Nursery')
    # print(searchUndergraduateClassList('Mechanics And Waves'))
    updateModuleData('webScraping.csv')
