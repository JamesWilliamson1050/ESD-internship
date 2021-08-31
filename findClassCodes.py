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
        degreeLevel = df.loc[index]['Degree Level'].split()[0]
        # Searching for module depending on degree level
        degreeSearch = 'search' + degreeLevel + 'ClassList'
        degreeSearch = eval(degreeSearch)

        # if '(' in moduleTitle:
        #     moduleTitle = wordFilter.bracketFilter(moduleTitle)

        moduleSearch = degreeSearch(moduleTitle)
        moduleCode = moduleSearch[0]
        moduleLevel = moduleSearch[1]
        moduleCodeType = type(moduleCode)

        if moduleCodeType == str:
            row['Module Code'] = moduleCode
            row['Module Level'] = moduleLevel

        elif moduleCodeType == numpy.ndarray:
            row['Module Code'] = moduleCode[0]
            row['Module Level'] = moduleLevel[0]

        elif moduleCode is None:
            moduleTitle = wordFilter.andFilter(moduleTitle)
            moduleSearch = degreeSearch(moduleTitle)
            moduleCode = moduleSearch[0]
            moduleLevel = moduleSearch[1]
            moduleCodeType = type(moduleCode)

            if moduleCodeType == str:
                row['Module Code'] = moduleCode
                row['Module Level'] = moduleLevel
                row['Module Title'] = moduleTitle


            elif moduleCodeType == numpy.ndarray:
                row['Module Code'] = moduleCode[0]
                row['Module Level'] = moduleLevel[0]
                row['Module Title'] = moduleTitle

            elif moduleCode is None:
                if ';' in moduleTitle or ':' in moduleTitle:
                    moduleTitle = wordFilter.colonFilter(moduleTitle)
                    moduleSearch = degreeSearch(moduleTitle)
                    moduleCode = moduleSearch[0]
                    moduleLevel = moduleSearch[1]
                    moduleCodeType = type(moduleCode)

                    if moduleCodeType == str:
                        row['Module Code'] = moduleCode
                        row['Module Level'] = moduleLevel
                        row['Module Title'] = moduleTitle


                    elif moduleCodeType == numpy.ndarray:
                        row['Module Code'] = moduleCode[0]
                        row['Module Level'] = moduleLevel[0]
                        row['Module Title'] = moduleTitle

        elif '&' not in moduleTitle or 'And' not in moduleTitle:
            if ';' in moduleTitle or ':' in moduleTitle:
                moduleTitle = wordFilter.colonFilter(moduleTitle)
                moduleSearch = degreeSearch(moduleTitle)
                moduleCode = moduleSearch[0]
                moduleLevel = moduleSearch[1]
                moduleCodeType = type(moduleCode)

                if moduleCodeType == str:
                    row['Module Code'] = moduleCode
                    row['Module Level'] = moduleLevel
                    row['Module Title'] = moduleTitle


                elif moduleCodeType == numpy.ndarray:
                    row['Module Code'] = moduleCode[0]
                    row['Module Level'] = moduleLevel[0]
                    row['Module Title'] = moduleTitle

    df = df.sort_values('Module Code', ascending=False)
    writeToCSV(df)


def readUGCSV():
    try:
        df = pd.read_csv('Class List Undergraduate 21-22.csv', sep=',', encoding="utf-8")
        header_row = 7

        df.columns = df.iloc[header_row]
        return df
    except Exception:
        print("Undergraduate CSV file not found")


def readPGCSV():
    try:
        df = pd.read_csv('Class List Postgraduate 21-22.csv')
        header_row = 7
        df.columns = df.iloc[header_row]
        return df
    except Exception:
        print("Postgraduate CSV file not found")


def searchUndergraduateClassList(moduleTitle):
    df = readUGCSV()
    title = df['TITLE']
    search = title == moduleTitle
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


def searchPostgraduateClassList(moduleTitle):
    df = readPGCSV()
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
    dataframe.to_csv('moduleInfoClassCodes.csv', sep=',', encoding="utf-8", index=False)


if __name__ == '__main__':
    # fillUndergraduateList()
    # searchUndergraduate('Year 3 Pedagogy And Placement Learning - Nursery')
    # print(searchUndergraduateClassList('Professional Skills: Curriculum And Pedagogy Chemistry 1'))
    # print(searchPostgraduateClassList('5g Communications Networks'))
    # print(searchUndergraduateClassList(''))
    updateModuleData('webScraping.csv')
