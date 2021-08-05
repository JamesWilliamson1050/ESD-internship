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
moduleTupleList = []

# A list containing all information of each module
allModuleInfo = []

# Used for outputting headers of CSV file
headerInfo = ['Code','Module Title', 'Module Description', 'Degree Level', 'Module Level' ]
undergraduateList = []
postgraduateList = []

filterList = ['Elective classes', 'Elective', 'Year 1', 'Transferable Skills', 'Course Summary']


# Used to fill in the undergraduate Lisr
def fillUndergraduateList():
    with open('Class List Undergradute 21-22.csv', 'r') as undergraduateCSV:
        reader = csv.reader(undergraduateCSV)

        for row in reader:
            if len(row) > 2:
                undergraduateList.append(row)

    undergraduateCSV.close()



def fillPostgraduateList():
    with open('Class List Postgraduate 21-22.csv', 'r') as postgraduateCSV:
        reader = csv.reader(postgraduateCSV)

        for row in reader:
            if len(row) > 2:
                postgraduateList.append(row)

    postgraduateCSV.close()



def searchUndergraduate(moduleSearchUG):
    # Returns the code and level of a course found in the class catalogue csv file
    for mod in undergraduateList:
        if moduleSearchUG.lower() == mod[1].lower():
            return (mod[0], mod[3])



def searchPostgraduate(moduleSearchPG):
    for mod in postgraduateList:
        if moduleSearchPG.lower() == mod[1].lower():
            return (mod[0], mod[3])






def andFilter(string):
    if '&' and 'And' in string:
        return string
    elif '&' in string:
        string = string.replace('&', 'And')
    elif 'And' in string:
        string = string.replace('And', '&')
    if '1 And 2' in string:
        s1 = string.split('1')
        s1 = s1[0]
        s2 = s1 + '2'
        s1 = s1 + '1'
        string = s1, s2
    if 'I And II' in string:
        s1 = string.split('I')
        s2 = s1[0] + 'Ii'
        s1 = s1[0] + 'I'
        string = s1, s2


    return string


def colonFilter(string):
    if ';' in string:
        string = string.replace(';', ':')
    elif ':' in string:
        string = string = string.replace(':', ';')
    return string



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

            if titleChanged:
                moduleTitleText = tempTitle

                titleChanged = False

            # Removing new lines from module descriptions
            moduleDescriptionText = moduleDescriptionText.replace('\n', '')
            moduleDescriptionText = moduleDescriptionText.replace('\r', '')

            # Removing spaces from the beginning and end of module titles
            moduleTitleText = moduleTitleText.strip()

            moduleDescriptionText = moduleDescriptionText.strip()

            # Removing spaces from course level
            courseLevelText = courseLevelText.strip()



            # Add duplicate of current module, except change the module title in the h5 tag
            # if '&':
            #     moduleTitleText = andFilter(moduleTitleText)
            #     if type(moduleTitleText) is tuple:
            #         t1 = moduleTitleText[0]
            #         tempTitle = moduleTitleText[1]
            #         moduleTitleText = t1
            #         temp = module
            #         modules.insert(modules.index(module) + 1, temp)
            #         titleChanged = True

            # Used to find course codes and levels
            if courseLevelText == 'Undergraduate':
                moduleLevel = searchUndergraduate(moduleTitleText)
                moduleCode = None
                if moduleLevel is not None:
                    print(moduleLevel, moduleTitleText)
                    moduleCode = moduleLevel[0]
                    moduleLevel = moduleLevel[1]
                elif moduleLevel is None:
                    if '&' in moduleTitleText:
                        moduleTitleText = andFilter(moduleTitleText)
                        if type(moduleTitleText) is tuple:
                            t1 = moduleTitleText[0]
                            tempTitle = moduleTitleText[1]
                            moduleTitleText = t1
                            temp = module
                            modules.insert(modules.index(module) + 1, temp)
                            titleChanged = True
                        moduleLevel = searchUndergraduate(moduleTitleText)
                    if moduleLevel is not None:
                        moduleCode = moduleLevel[0]
                        moduleLevel = moduleLevel[1]
                    elif moduleLevel is None:
                        if ';' in moduleTitleText or ':' in moduleTitleText:
                            moduleTitleText = colonFilter(moduleTitleText)
                            moduleLevel = searchUndergraduate(moduleTitleText)
                            if moduleLevel is not None:
                                moduleCode = moduleLevel[0]
                                moduleLevel = moduleLevel[1]
                            else:
                                moduleCode = None
                                moduleLevel = None

            elif 'Postgraduate' in courseLevelText:
                moduleLevel = searchPostgraduate(moduleTitleText)
                moduleCode = None
                if moduleLevel is not None:
                    moduleCode = moduleLevel[0]
                    moduleLevel = moduleLevel[1]
                elif moduleLevel is None:
                    if '&' in moduleTitleText:
                        moduleTitleText = andFilter(moduleTitleText)
                        if type(moduleTitleText) is tuple:
                            t1 = moduleTitleText[0]
                            tempTitle = moduleTitleText[1]
                            moduleTitleText = t1
                            temp = module
                            modules.insert(modules.index(module) + 1, temp)
                            titleChanged = True
                        moduleLevel = searchPostgraduate(moduleTitleText)
                    if moduleLevel is not None:
                        moduleCode = moduleLevel[0]
                        moduleLevel = moduleLevel[1]
                    elif moduleLevel is None:
                        if ';' in moduleTitleText or ':' in moduleTitleText:
                            moduleTitleText = colonFilter(moduleTitleText)
                            moduleLevel = searchPostgraduate(moduleTitleText)
                            if moduleLevel is not None:
                                moduleCode = moduleLevel[0]
                                moduleLevel = moduleLevel[1]
                            else:
                                moduleCode = None
                                moduleLevel = None



            # Stores information on the current module
            moduleInfo = []

            # if moduleTitleText in filterList:
            #     print("It is here", moduleTitleText)
            # Checks if a module title is in a dictionary
            if moduleTitleText not in moduleTitleDesc and moduleTitleText not in moduleTupleList:


                # Add module title and description to the dictionary
                moduleTitleDesc[moduleTitleText] = moduleDescriptionText

                # Add any other relative information to a list, 'moduleInfo', then adds that list to a list of lists, 'allModuleInfo'
                moduleInfo.append(moduleCode)
                moduleInfo.append(moduleTitleText)
                moduleInfo.append(moduleDescriptionText)
                moduleInfo.append(courseLevelText)
                moduleInfo.append(moduleLevel)
                allModuleInfo.append(moduleInfo)



                if moduleTitleDesc[moduleTitleText] != moduleDescriptionText:
                    # Keeps a list of the currently stored module Information
                    currentModuleInfo = []
                    currentModuleInfo.append(moduleCode)
                    currentModuleInfo.append(moduleTitleText)
                    currentModuleInfo.append(moduleTitleDesc[moduleTitleText])
                    currentModuleInfo.append(courseLevelText)
                    currentModuleInfo.append(moduleLevel)

                    # Updates the module information
                    moduleInfo.append(moduleCode)
                    moduleInfo.append(moduleTitleText)
                    moduleTitleDesc[moduleTitleText] = moduleTitleDesc[moduleTitleText] + moduleDescriptionText
                    moduleInfo.append(moduleTitleDesc[moduleTitleText])
                    moduleInfo.append(courseLevelText)
                    moduleInfo.append(moduleLevel)
                    currentModuleIndex = allModuleInfo.index(currentModuleInfo)
                    allModuleInfo[currentModuleIndex] = moduleInfo

        #break


def seperateClasses():
    print()
# Writes to a CSV file
def writeToCSV():
    # Writing all module information to a csv file
    with open('moduleInfo2codes.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        # write the header
        writer.writerow(headerInfo)
        writer.writerows(allModuleInfo)
    f.close()


# Writes to a text file
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
    fillPostgraduateList()
    findModules()
    writeToCSV()
    #print(searchPostgraduate('Maritime Safety & Risk'))




# writeToCSV()
# writeToText()


# read_file = pd.read_csv('text.txt')
# read_file.to_csv(r'moduleInfo.csv', index=None)



