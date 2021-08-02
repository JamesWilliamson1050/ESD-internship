import numpy
from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

# Loading the strathclyde website
defaultURL = 'https://www.strath.ac.uk'

# This extension takes you to all the university's courses
courseSearchExtension = '/courses/undergraduate/'

# The next two lines are basically opening the html file
defaultPage = urlopen(defaultURL + courseSearchExtension)
defaultHtml = defaultPage.read().decode("utf-8")

# I think this parses the html, might've forgotten
soup = BeautifulSoup(defaultHtml, 'lxml')

# Basically finds all the classes individual extensions and stores them in a variable
courses = soup.find_all('a', class_="course-search-result__link")

# A dictionary with the module titles as the keys and module descriptions as values
moduleTitleDesc = dict()

# A list containing all information of each module
allModuleInfo = []

# Used for outputting headers of CSV file
headerInfo = ['Module Title', 'Module Description']
undergraduateList = []
postgraduateList = []


# Used to fill in the undergraduate Lisr
def fillUndergraduateList():
    with open('Class List Undergraduate 21-22.csv', 'r') as undergraduateCSV:
        reader = csv.reader(undergraduateCSV)

        for row in reader:
            if len(row) > 2:
                undergraduateList.append(row)

    undergraduateCSV.close()


def searchUndergraduate(moduleSearchUG):
    for mod in undergraduateList:
        if moduleSearchUG in mod:
            return mod[3]

def findModules():
    # Loops through all courses
    for course in courses:

        # Outputs a course's
        courseURL = (defaultURL + course['href'])

        # Opens the course webpage, in a format that can be understood
        coursePage = urlopen(courseURL)
        courseHtml = coursePage.read().decode("utf-8")

        # Beings web scraping the current web page
        courseContent = BeautifulSoup(courseHtml, 'lxml')

        courseLevel = course.find('div', {'class': ""})
        courseLevelText = courseLevel.text

        # This finds a specific module
        modules = courseContent.find_all('div', {'class': "course-module"})

        # loops through modules
        for module in modules:
            # Find module title and module description
            moduleTitle = module.find('h5')
            moduleDescription = module.find('div', {'class': "course-module-content-inner"})

            # Storing module titles and module descriptions as plain text
            moduleTitleText = moduleTitle.text
            moduleDescriptionText = moduleDescription.text

            # Removing new lines from module descriptions
            moduleDescriptionText = moduleDescriptionText.replace('\n', '')
            moduleDescriptionText = moduleDescriptionText.replace('\r', '')

            # Removing spaces from the beginning and end of module titles
            moduleTitleText = moduleTitleText.strip()

            # Stores information on the current module
            moduleInfo = []

            # Checks if a module title is in a dictionary
            if moduleTitleText not in moduleTitleDesc:
                # Add module title and description to the dictionary
                moduleTitleDesc[moduleTitleText] = moduleDescriptionText

                # Add any other relative information to a list, 'moduleInfo', then adds that list to a list of lists, 'allModuleInfo'
                moduleInfo.append(moduleTitleText)
                moduleInfo.append(moduleDescriptionText)
                moduleInfo.append(courseLevelText)
                allModuleInfo.append(moduleInfo)
                # print(moduleInfo)

                # This can be ignored for now
                # if 'Elective' in moduleTitleText:
                #     print('Elective' + moduleTitleText)

            # If module title is already in the dictionary
            else:
                # Check if module description has changed from the current one
                if moduleTitleDesc[moduleTitleText] != moduleDescriptionText:
                    # Keeps a list of the currently stored module Information
                    currentModuleInfo = []
                    currentModuleInfo.append(moduleTitleText)
                    currentModuleInfo.append(moduleTitleDesc[moduleTitleText])
                    currentModuleInfo.append(courseLevelText)

                    # Updates the module information
                    moduleInfo.append(moduleTitleText)
                    moduleTitleDesc[moduleTitleText] = moduleTitleDesc[moduleTitleText] + moduleDescriptionText
                    moduleInfo.append(moduleTitleDesc[moduleTitleText])
                    moduleInfo.append(courseLevelText)
                    currentModuleIndex = allModuleInfo.index(currentModuleInfo)
                    allModuleInfo[currentModuleIndex] = moduleInfo

            moduleLevel  = searchUndergraduate(moduleTitleText)


        break


def writeToCSV():
    # Writing all module information to a csv file
    with open('moduleInfo.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        # write the header
        writer.writerow(headerInfo)
        writer.writerows(allModuleInfo)
    f.close()


def writeToText():
    # Writing module title and module description to text file
    with open('moduleInfo.txt', 'w', encoding='UTF8', newline='') as f:
        f.write(", ".join(headerInfo) + "\n")
        for ModuleInfo in allModuleInfo:
            titleOfModule = ModuleInfo[0]
            descOfModule = ModuleInfo[1]

            f.write(titleOfModule + ':' + descOfModule + '\n')
        # write the header

    f.close()


if __name__ == '__main__':
    fillUndergraduateList()
    findModules()
    #searchUndergraduate('Strategy And Leadership')

# writeToCSV()
# writeToText()


# read_file = pd.read_csv('text.txt')
# read_file.to_csv(r'moduleInfo.csv', index=None)

# print(allModuleInfo)
