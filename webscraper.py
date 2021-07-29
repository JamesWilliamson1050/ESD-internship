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

moduleTitleDesc = dict()

allModuleInfo = []

headerInfo = ['Module Title', 'Module Description']

count = 0

# Loops through all courses
for course in courses:

    # Outputs a course's
    courseURL = (defaultURL + course['href'])

    coursePage = urlopen(courseURL)
    courseHtml = coursePage.read().decode("utf-8")
    courseContent = BeautifulSoup(courseHtml, 'lxml')

    courseLevel = course.find('div', {'class': ""})

    ## This is used to try and find a specific div
    modules = courseContent.find_all('div', {'class': "course-module"})

    # loops through modules
    for module in modules:
        moduleTitle = module.find('h5')
        moduleDescription = module.find('div', {'class': "course-module-content-inner"})
        # moduleCode = module.find('div', {'class': "course-module-content"})
        # print(moduleCode)

        moduleTitleText = moduleTitle.text
        moduleDescriptionText = moduleDescription.text
        moduleDescriptionText = moduleDescriptionText.replace('\n', '')
        moduleDescriptionText = moduleDescriptionText.replace('\r', '')
        utfmoduleDescription = moduleDescriptionText.encode("UTF8")
        # moduleYearText = moduleYear.text

        moduleTitleText = moduleTitleText.strip()
        moduleTitleText = moduleTitleText.rstrip()

        moduleDescList = [moduleDescriptionText]

        moduleInfo = []
        if moduleTitleText not in moduleTitleDesc:
            moduleTitleDesc[moduleTitleText] = moduleDescriptionText
            moduleInfo.append(moduleTitleText)
            moduleInfo.append(moduleDescriptionText)
            allModuleInfo.append(moduleInfo)



        else:
            if moduleTitleDesc[moduleTitleText] != moduleDescriptionText:
                currentModuleInfo = []
                currentModuleInfo.append(moduleTitleText)
                currentModuleInfo.append(moduleTitleDesc[moduleTitleText])
                moduleInfo.append(moduleTitleText)
                moduleTitleDesc[moduleTitleText] = moduleTitleDesc[moduleTitleText] + moduleDescriptionText
                moduleInfo.append(moduleTitleDesc[moduleTitleText])
                currentModuleIndex = allModuleInfo.index(currentModuleInfo)
                allModuleInfo[currentModuleIndex] = moduleInfo

        count += 1







                #print("Hello")
            #print("Hello")
        #allModuleInfo.append(moduleInfo)




    break

if __name__ == '__main__':
    # with open('moduleInfo.csv', 'w', encoding='UTF8', newline='') as f:
    #     writer = csv.writer(f)
    #     # write the header
    #     writer.writerow(headerInfo)
    #     writer.writerows(allModuleInfo)
    # f.close()

    with open('test.txt', 'w', encoding='UTF8', newline='') as f:
        f.write(", ".join(headerInfo) + "\n")
        for ModuleInfo in allModuleInfo:
            f.write(", ".join(ModuleInfo) + "\n")

        # write the header

    f.close()
    print()
