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

        # If only one module code is found
        if moduleCodeType == str:
            row['Module Code'] = moduleCode
            row['Module Level'] = moduleLevel

        # If a module has multiple codes
        elif moduleCodeType == numpy.ndarray:
            row['Module Code'] = moduleCode[0]
            row['Module Level'] = moduleLevel[0]

        # No modulle code is found
        elif moduleCode is None:
            # Put the module title through the and filter and then searches for it again
            moduleTitle = wordFilter.andFilter(moduleTitle)
            moduleSearch = degreeSearch(moduleTitle)
            moduleCode = moduleSearch[0]
            moduleLevel = moduleSearch[1]
            moduleCodeType = type(moduleCode)

            # One module code found
            if moduleCodeType == str:
                row['Module Code'] = moduleCode
                row['Module Level'] = moduleLevel
                row['Module Title'] = moduleTitle

            # Multiple module codes found
            elif moduleCodeType == numpy.ndarray:
                row['Module Code'] = moduleCode[0]
                row['Module Level'] = moduleLevel[0]
                row['Module Title'] = moduleTitle

            # No module codes found
            elif moduleCode is None:

                # If module title contains a colon or semi colon put it through the colon filter and search again
                if ';' in moduleTitle or ':' in moduleTitle:
                    moduleTitle = wordFilter.colonFilter(moduleTitle)
                    moduleSearch = degreeSearch(moduleTitle)
                    moduleCode = moduleSearch[0]
                    moduleLevel = moduleSearch[1]
                    moduleCodeType = type(moduleCode)

                    # One module code is found
                    if moduleCodeType == str:
                        row['Module Code'] = moduleCode
                        row['Module Level'] = moduleLevel
                        row['Module Title'] = moduleTitle

                    # Multiple code is found
                    elif moduleCodeType == numpy.ndarray:
                        row['Module Code'] = moduleCode[0]
                        row['Module Level'] = moduleLevel[0]
                        row['Module Title'] = moduleTitle

        # Not entirely sure why this is here as it is essentially repeating itself. Could potentially be removed
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

    # Sort the modules by their module codes
    df = df.sort_values('Module Code', ascending=False)

    # Passes the dataframe to writeTOCSV function
    writeToCSV(df)


# Reads in 21-22 undergraduate class list csv file and converts it to a dataframe
def readUGCSV():
    try:
        df = pd.read_csv('Class List Undergraduate 21-22.csv', sep=',', encoding="utf-8")

        # Sets the header to the 7th row. Makes the headers CODE, TITLE, etc rather than the original file header.
        header_row = 7
        df.columns = df.iloc[header_row]
        return df
    except Exception:
        print("Undergraduate CSV file not found")

# Reads in 21-22 postgraduate class list csv file and converts it to a dataframe
def readPGCSV():
    try:
        df = pd.read_csv('Class List Postgraduate 21-22.csv')

        # Sets the header to the 7th row. Makes the headers CODE, TITLE, etc rather than the original file header.
        header_row = 7
        df.columns = df.iloc[header_row]
        return df
    except Exception:
        print("Postgraduate CSV file not found")

# Searches for module title in the undergraduate class list
def searchUndergraduateClassList(moduleTitle):
    df = readUGCSV()
    title = df['TITLE']

    search = title == moduleTitle

    # Finds the module code and level
    moduleCodes = df.loc[search]['CODE']
    moduleCode = moduleCodes.values
    moduleLevels = df.loc[search]['LEVEL']
    moduleLevel = moduleLevels.values

    # if module isn't found code and level are left empty
    if moduleCode.size == 0:
        moduleCode = None
        moduleLevel = None
    # if module found set code and level
    elif moduleCode.size == 1:
        moduleCode = moduleCode[0]
        moduleLevel = moduleLevel[0]

    return moduleCode, moduleLevel

# Searches for module title in the postgraduate class list
def searchPostgraduateClassList(moduleTitle):
    df = readPGCSV()
    df['TITLE']
    # Returns any rows with the same module title as the one selected
    search = df['TITLE'] == moduleTitle

    # Finds the module code and level
    moduleCodes = df.loc[search]['CODE']
    moduleCode = moduleCodes.values
    moduleLevels = df.loc[search]['LEVEL']
    moduleLevel = moduleLevels.values

    # if module isn't found code and level are left empty
    if moduleCode.size == 0:
        moduleCode = None
        moduleLevel = None

    # if module found set code and level
    elif moduleCode.size == 1:
        moduleCode = moduleCode[0]
        moduleLevel = moduleLevel[0]

    return moduleCode, moduleLevel


# writes to csv file
def writeToCSV(dataframe):
    dataframe.to_csv('moduleInfoClassCodes.csv', sep=',', encoding="utf-8", index=False)


if __name__ == '__main__':
    # fillUndergraduateList()
    # searchUndergraduate('Year 3 Pedagogy And Placement Learning - Nursery')
    # print(searchUndergraduateClassList('Professional Skills: Curriculum And Pedagogy Chemistry 1'))
    # print(searchPostgraduateClassList('5g Communications Networks'))
    # print(searchUndergraduateClassList(''))
    updateModuleData('webScraping.csv')
