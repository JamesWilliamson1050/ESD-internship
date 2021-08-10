# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 12:30:16 2021

@author: Morrison
"""

import csv
import os

#import webscraper as ws
import fillWebForm
import pandas as pd


# kw = __import__('web outputs without electives')


# Gets the file name
def inspectFile(fileName):
    csvExtension = '.csv'
    txtExtension = '.txt'

    if fileName.endswith(csvExtension):
        readFromCSV(fileName)
    elif fileName.endswith(txtExtension):
        readFromTxt(fileName)
    else:
        print("Sorry file is not in correct format. Make sure the file ends in .txt or .csv")


# Reads from a csv

def readFromCSV(csvfile):
    try:
        csv_file = open(csvfile, 'r', encoding='utf-8')
    except:
        print("csv file could not be found")

    with csv_file:

        reader = csv.reader(csv_file)

        # Find out how to print column containing 'Module Title'. Probably just use an if
        moduleTitleList = ['Module Title', 'module title', 'Module title', 'module Title', 'Title', 'title']
        moduleDescriptionList = ['Module Description', 'module Description', 'Module Description',
                             'module Description',
                             'Description', 'description']
        moduleCodeList = ['Code', 'code']
        moduleCodeList = ['Code', 'code']

        for col in reader:

            # Lists of possible ways the module title and description could be spelled
            # These lines check if any of the module titles and description are in the csv file
            matchModuleTitle = next((mt for mt in moduleTitleList if mt in col), False)
            matchModuleDesc = next((md for md in moduleDescriptionList if md in col), False)
            matchModuleCode = next((mc for mc in moduleCodeList if mc in col), False)


            # Gets the index of the module title
            if matchModuleTitle:
                indexMT = col.index(matchModuleTitle)

            # Gets the index of the module description
            if matchModuleDesc:
                indexMD = col.index(matchModuleDesc)

            if matchModuleCode:
                indexMC = col.index(matchModuleCode)

            moduleTitle = col[indexMT]
            moduleDescription = col[indexMD]
            moduleCode = col[indexMC]

            if moduleCode == "":
                department.append('Empty department')
                faculty.append('Empty faculty')
            else:

                if moduleCode not in moduleCodeList and moduleCode is not None:
                    print(moduleCode)
                    departmentPlusFaculty = fillWebForm.fillForm(moduleCode)
                    department.append(departmentPlusFaculty[0])
                    faculty.append(departmentPlusFaculty[1])



            if moduleTitle not in moduleTitleList:
                filterKeywords(moduleTitle, moduleDescription, department, faculty)


    csv_file.close()


# Reads from a text file
def readFromTxt(txtfile):
    try:
        with open(txtfile, 'r') as txt_file:
            for module in txt_file:
                splitModule = module.split("`", 3)
                moduleTitle = splitModule[1]
                moduleDescription = splitModule[3]
                print(moduleDescription)
            txt_file.close()
    except:
        print("Text file not in the correct format")


def filterKeywords(moduleTitle, moduleDescription, moduleDepartment, moduleFaculty):
    sdg = {}
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
            
    output[moduleTitle] = sdgList


def writeOutput(output):
    with open('WebOutputs.csv', 'w', encoding="utf-8", newline='') as webOutputs:
        writer = csv.writer(webOutputs)
        writer.writerow(["Module Title", "Department"] + [("SDG" + str(sdgNo)) for sdgNo in range(1, 18)])
        
        for count, key in enumerate(output.keys()): 
            writer.writerow([key.replace(',', ';'), department[count]] + output[key])

        #print(department)

        webOutputs.close()

# Runs the program
if __name__ == '__main__':
    output = {}
    department = []
    faculty = []
    inspectFile('moduleInfo2codes.csv')
    writeOutput(output)
    # 2187 outputs!!!

    # ws.main()

    # Get users to enter file name
    # If file ends in txt read from text file
    # If file ends in csv read from csv
    # If file does not have an ending either let user choose to write to csv or text file  or both
    # Web scrape data where possible
    # Write web scraped data to chosen file type
    # Then read from file and compare to keywords csv
