import time

import pandas as pd


def readCSV(csvFile):
    try:
        df = pd.read_csv(csvFile, sep=',', encoding="utf-8")
        return df
    except Exception:
        print("Could not open CSV file")


def findTitleAndDesc():
    moduleTitleList = ['Module Title', 'module title', 'Module title', 'module Title', 'Title', 'title', 'TITLE']
    moduleDescriptionList = ['Module Description', 'module Description', 'Module description', 'module Description'
                                                                                               'Description',
                             'description']


    moduleTitle = next((mt for mt in moduleTitleList if mt in dataframe.columns), False)
    moduleDesc = next((md for md in moduleDescriptionList if md in dataframe.columns), False)





    if moduleTitle and moduleDesc:
        writeHeaders()
        for index, row in dataframe.iterrows():
            filterKeywords(str(row[moduleTitle]), str(row[moduleDesc]))
    else:
        print("Could not find module title and description")


def filterKeywords(moduleTitle, moduleDescription):

    sdg = {}
    output = {}
    moduleDescription = moduleDescription.lower().strip()
    with open("KEYWORDS.csv") as keywords_file:


        for inc, line in enumerate(keywords_file.readlines()):
            sdgNow = [word for word in line.lower().strip().split(',') if word not in ['', '\n', ' ']]
            sdg[inc + 1] = sdgNow

    keywords_file.close()

    sdgList = []

    for index in sdg.keys():

        if any(word in moduleDescription for word in sdg[index]):
            sdgList.append("YES")
        else:
            sdgList.append("NO")
    writeOutput(sdgList)

    # output[moduleTitle] = sdgList







def writeHeaders():
    for sdgNo in range(1, 18):
        sdgHeader = 'SDG' + str(sdgNo)
        dataframe[sdgHeader] = ''




def writeOutput(list):
    try:

        global count
        if list:
            for sdgNo in range(1, 18):
                sdgHeader = 'SDG' + str(sdgNo)
                dataframe.loc[count][sdgHeader] = list[sdgNo - 1]

        count +=1
        dataframe.to_csv('Test.csv', sep=',', encoding="utf-8", index=False)

    except Exception:
        print("Error writing to CSV file")









if __name__ == '__main__':
    start = time.time()
    dataframe = readCSV('ModuleInfoAll.csv')
    count = 0
    findTitleAndDesc()
    print(time.time() - start)


