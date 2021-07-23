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

moduleInfoList = set([])

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
    x = 0
    for module in modules:
        moduleTitle = module.find('h5')
        moduleDescription = module.find('div', {'class': "course-module-content-inner"})

        moduleTitleText = moduleTitle.text
        moduleDescriptionText = moduleDescription.text

        # Opens and appends data to test.txt
        readf = open('test.txt', 'r+', encoding='utf-8')
        fcontent = readf.read()
        # Only adding modules that aren't already in the text file



        if moduleTitleText not in fcontent:
            readf.write(moduleTitleText)
            readf.write(moduleDescriptionText)
            readf.write('\n')
    break
    readf.close()





    # print(modules)

    # Makes the code only run once
