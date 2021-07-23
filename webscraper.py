from bs4 import BeautifulSoup
from urllib.request import urlopen
from requests_html import HTMLSession
import webbrowser

# Loading the strathclyde website
defaultURL = 'https://www.strath.ac.uk'

session = HTMLSession()


# This extension takes you to all the university's courses
courseSearchExtension = '/courses/undergraduate/'

# The next two lines are basically opening the html file
defaultPage = urlopen(defaultURL + courseSearchExtension)

defaultHtml = defaultPage.read().decode("utf-8")

# I think this parses the html, might've forgotten
soup = BeautifulSoup(defaultHtml, 'lxml')

# Basically finds all the classes individual extensions and stores them in a variable
courses = soup.find_all('a', class_="course-search-result__link")

x = 0
# Loops through all courses
for course in courses:

# Outputs a course's



    courseURL = (defaultURL + course['href'])

    renderSession = session.get(courseURL)

    # The first time this runs it will download chromium, the opensource version of google chrome
    # renderSession.html.render(sleep=1,  keep_page=True, scrolldown=1)
    #
    # modules = renderSession.html.find('#moduel-content')

    # for module in modules:
    #     print(module)

# Will open course web page in a browser
    #webbrowser.open(courseURL)
    coursePage = urlopen(courseURL)
    courseHtml = coursePage.read().decode("utf-8")
    courseContent = BeautifulSoup(courseHtml, 'lxml')

## This is used to try and find a specific div
    test = courseContent.find_all('div', {'class': "course-module"})
    #containerDiv = test('div', {'class': "tab-inner"})
    print(test)



    # Makes the code only run once
    break




