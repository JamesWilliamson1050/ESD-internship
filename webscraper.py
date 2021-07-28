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


moduleInfoDict = dict()
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



    for module in modules:
        moduleTitle = module.find('h5')
        moduleDescription = module.find('div', {'class': "course-module-content-inner"})
        # moduleCode = module.find('div', {'class': "course-module-content"})
        # print(moduleCode)

        moduleTitleText = moduleTitle.text
        moduleDescriptionText = moduleDescription.text
        # moduleYearText = moduleYear.text


        moduleTitleText = moduleTitleText.strip()
        moduleTitleText = moduleTitleText.rstrip()

        moduleDescList = []
        moduleDescList.append(moduleDescriptionText)

        # Opens, reads and writes data to test.txt

        if moduleTitleText not in moduleInfoDict:
            moduleInfoDict[moduleTitleText] = moduleDescList
        else:
            moduleInfoDict[moduleTitleText].append(moduleDescriptionText)#
        print(moduleDescriptionText)







# doesn't work properly
# def write_dic_to_file():
#     try:
#         file = open('test.txt', 'a')
#         file.write(json.dumps(moduleInfoDict))
#         file.close
#     except:
#         print("Unable to write to file")


if __name__ == '__main__':
    print()
    # write_dic_to_file()
    # print(moduleInfoDict.keys())

    with open('moduleInfo.csv', 'w', encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerows(moduleInfoDict.items())

    # Adding
