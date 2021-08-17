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
        moduleSearch = degreeSearch(moduleTitle)
        moduleCode = moduleSearch[0]
        moduleLevel = moduleSearch[1]
        moduleCodeType = type(moduleCode)



        # If a module has a single module code it's type is a string
        if moduleCodeType == str:
            df.at[index, 'Module Code'] = moduleCode
            df.at[index, 'Module Level'] = moduleLevel

        # If a module code has multiple values then it is an array
        elif moduleCodeType == numpy.ndarray:
            for i in range(len(moduleCode)):
                tempRow = row
                tempRow['Module Code', 'Module Level'] = [moduleCode[i], moduleLevel[i]]

                df = df.append(tempRow)

        # Module code hasn't been found
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
                moduleSearch = degreeSearch(title1)
                moduleCode = moduleSearch[0]
                moduleLevel = moduleSearch[1]
                row['Module Code'] = moduleCode
                row['Module Level'] = moduleLevel

                moduleSearch = degreeSearch(title2)
                moduleCode = moduleSearch[0]
                moduleLevel = moduleSearch[1]
                tempRow['Module Code'] = moduleCode
                tempRow['Module Level'] = moduleLevel

                df = df.append(tempRow)

            elif type(moduleTitle) == str:
                moduleSearch = degreeSearch(moduleTitle)
                moduleCode = moduleSearch[0]
                moduleLevel = moduleSearch[1]
                moduleCodeType = type(moduleCode)


                if moduleCodeType == numpy.ndarray:
                    for i in range(len(moduleCode)):
                        tempRow = row
                        tempRow['Module Code', 'Module Level'] = [moduleCode[i], moduleLevel[i]]
                        df = df.append(tempRow)

                # elif moduleCode is None:
                #     # print(moduleTitle.encode("utf-8"), moduleCode, moduleLevel)
                #     print()





    df = df.sort_values('Degree Level', ascending=False)
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


def readPGCSV():
    try:
        dataframe = pd.read_csv('Class List Postgraduate 21-22.csv', sep=',', encoding="utf-8")
        header_row = 7
        print(dataframe)

        dataframe.columns = dataframe.iloc[header_row]
        return dataframe
    except Exception:
        print("Postgraduate CSV file not found")
    dataframe.close()


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


def searchPostgraduateClassList(moduleTitle):
    df = readPGCSV()
    print(df)
    # df['TITLE']
    # search = df['TITLE'] == moduleTitle
    # moduleCodes = df.loc[search]['CODE']
    # moduleCode = moduleCodes.values
    # moduleLevels = df.loc[search]['LEVEL']
    # moduleLevel = moduleLevels.values
    #
    # if moduleCode.size == 0:
    #     moduleCode = None
    #     moduleLevel = None
    # elif moduleCode.size == 1:
    #     moduleCode = moduleCode[0]
    #     moduleLevel = moduleLevel[0]
    #
    # return moduleCode, moduleLevel

def writeToCSV(dataframe):
    print()






if __name__ == '__main__':
    # fillUndergraduateList()
    # searchUndergraduate('Year 3 Pedagogy And Placement Learning - Nursery')
    # print(searchUndergraduateClassList('Professional Skills: Curriculum And Pedagogy Chemistry 1'))
    print(searchPostgraduateClassList(''))
    # print(searchUndergraduateClassList(''))
    #updateModuleData('webScraping.csv')
