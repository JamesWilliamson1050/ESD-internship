import csv
import wordFilter

import pandas as pd
from comtypes.safearray import numpy


def updateModuleData(webScrapedcsvFile):
    df = pd.read_csv(webScrapedcsvFile, sep=',', encoding="utf-8")

    df['Module Code'] = ''
    df['Module Level'] = ''

    for index, row in df.iterrows():
        moduleTitle = df.loc[index]['Module Title'].title()
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
                tempRow['Module Code', 'Module Level'] = [moduleCode[i], moduleLevel[i]]
                df.append(tempRow)
        elif moduleCode is None:
            moduleTitle = wordFilter.andFilter(moduleTitle)

            # If course has been split into 2
            if type(moduleTitle) is tuple:  #

                # The titles of the 2 courses
                title1 = moduleTitle[0]
                title2 = moduleTitle[1]

                # Keeping a copy of the current row
                tempRow = row.copy()


                # Setting the titles of the row and copy of the row to the new courses
                row['Module Title'] = title1
                tempRow['Module Title'] = title2

                # Searching for the course title
                moduleSearch = searchUndergraduateClassList(title1)
                moduleCode = moduleSearch[0]
                moduleLevel = moduleSearch[1]
                row['Module Code'] = moduleCode
                row['Module Level'] = moduleLevel


                moduleSearch = searchUndergraduateClassList(title2)
                moduleCode = moduleSearch[0]
                moduleLevel = moduleSearch[1]
                tempRow['Module Code'] = moduleCode
                tempRow['Module Level'] = moduleLevel

                df = df.append(tempRow)




            elif moduleCodeType == str:
                moduleSearch = searchUndergraduateClassList(title1)
                moduleCode = moduleSearch[0]
                moduleLevel = moduleSearch[1]
                df.at[index, 'Module Code'] = moduleCode
                df.at[index, 'Module Level'] = moduleLevel
    df = df.sort_values('Degree Level')
    df.to_csv('moduleInfoClassCodes.csv', sep=',', encoding="utf-8", index=False)





            # Add in filtering code and search for the data again
            # break


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
    df['TITLE']
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
    # print(searchUndergraduateClassList('Professional Skills: Curriculum And Pedagogy Chemistry 1'))
    updateModuleData('webScraping.csv')
