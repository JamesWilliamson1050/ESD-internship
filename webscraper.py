from bs4 import BeautifulSoup
from urllib.request import urlopen

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

moduleInfoList = []
# Loops through all courses
for course in courses:

    # Outputs a course's
    courseURL = (defaultURL + course['href'])

    # Will open course web page in a browser

    coursePage = urlopen(courseURL)
    courseHtml = coursePage.read().decode("utf-8")
    courseContent = BeautifulSoup(courseHtml, 'lxml')

    ## This is used to try and find a specific div
    modules = courseContent.find_all('div', {'class': "course-module"})

    for module in modules:
        moduleTitle = module.find('h5')
        moduleDescription = module.find('div', {'class': "course-module-content-inner"})

        moduleTitleText = moduleTitle.text
        moduleDescriptionText = moduleDescription.text
        # print(moduleTitleText)
        # print(moduleDescriptionText)
        # print()

        f = open('test.txt', 'a', encoding='utf-8')
        f.write(moduleTitleText)
        f.write(moduleDescriptionText)
        f.close()









    # print(modules)

    # Makes the code only run once
    break