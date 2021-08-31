
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
moduleTupleList = []

# A list containing all information of each module
allModuleInfo = []

# Used for outputting headers of CSV file
headerInfo = ['Module Title', 'Module Description', 'Degree Level']
undergraduateList = []
postgraduateList = []

filterList = set(['elective classes', 'elective class', 'elective', 'year 1', 'transferable skills', 'course summary',
                  'year 1 - fundamentals', 'year 2 - core chemical engineering', 'year 4 - chemical engineering design',
                  'year 2', 'year 3', 'year 4', 'year 5 - advanced chemical engineering', 'year abroad', 'Year 3 Course Summary', 'Year 4 Course Summary'])


def findModules():
    # Loops through all courses
    titleChanged = False
    tempTitle = ""
    for course in courses:

        # Outputs a course's
        courseURL = (defaultURL + course['href'])

        # Opens the course webpage, in a format that can be understood
        try:
            coursePage = urlopen(courseURL)
        except Exception:
            print("Could not open")

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

            # if titleChanged:
            #     moduleTitleText = tempTitle
            #     titleChanged = False

            # Removing new lines from module descriptions
            # moduleDescriptionText = moduleDescriptionText.replace('\n', '')
            # moduleDescriptionText = moduleDescriptionText.replace('\r', '')

            # Removing spaces from the beginning and end of module titles
            moduleTitleText = moduleTitleText.strip()

            moduleDescriptionText = moduleDescriptionText.strip()

            # Removing spaces from course level
            courseLevelText = courseLevelText.strip()



            # Stores information on the current module
            moduleInfo = []



            # if moduleTitleText in filterList:
            #     print("It is here", moduleTitleText)
            # Checks if a module title is in a dictionary
            if moduleTitleText not in moduleTitleDesc and moduleTitleText.lower() not in filterList:

                # Add module title and description to the dictionary
                moduleTitleDesc[moduleTitleText] = moduleDescriptionText

                # Add any other relative information to a list, 'moduleInfo', then adds that list to a list of lists, 'allModuleInfo'
                moduleInfo.append(moduleTitleText)
                moduleInfo.append(moduleDescriptionText)
                moduleInfo.append(courseLevelText)
                allModuleInfo.append(moduleInfo)

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




# Writes to a CSV file
def writeToCSV():
    # Writing all module information to a csv file
    with open('webScraping.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        # write the header
        writer.writerow(headerInfo)
        writer.writerows(allModuleInfo)

    f.close()



def main():
    print("Start")
    findModules()
    print("End")


if __name__ == '__main__':
    findModules()
    writeToCSV()

