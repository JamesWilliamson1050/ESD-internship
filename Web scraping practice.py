# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 09:31:52 2021

@author: Morrison
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen
import webbrowser


def keyword():
    with open("KEYWORDS.csv") as csv_file:
        sdg = {}

        for inc, line in enumerate(csv_file.readlines()):
            sdgNow = [word for word in line.lower().split(',') if word not in ['', '\n', ' ']]
            sdg[inc + 1] = sdgNow

    # print(sdg)
    return (sdg)


# creating a way to search through the key words (currently hard coded just as example)
def test():
    # we can export the key word sheet for each SDG here as CSV
    sdg = keyword()
    # here we would have the text from the descriptions
    inputText = ("The adder is an accredited mechanical energy boi in Africa!".lower())
    output = {}
    sdgList = []
    print(inputText)

    for index in sdg.keys():
        if any(word in inputText for word in sdg[index]):
            sdgList.append("YES")
        else:
            sdgList.append("NO")

    # I though yes no would be better than just listing the SDGs present but let me know if not
    # can then be changed in a loop to go through every course
    output['Accounting (N400)'] = sdgList

    print(output)

    # 273 undergraduate class codes --> dictionary of 273 keys
    # {'Accounting (N400)' } : ['YES', 'NO']


test()

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

x = 0
# Loops through all courses
for course in courses:
    # Outputs a course's
    print(course['href'])

    courseURL = (defaultURL + course['href'])

    # Will open course web page in a browser
    #  webbrowser.open(courseURL)
    coursePage = urlopen(courseURL)
    courseHtml = coursePage.read().decode("utf-8")
    courseContent = BeautifulSoup(courseHtml, 'lxml')

    ## This is used to try and find a specific div
    test = courseContent.find('div', {"id": "coursecontent"})
    containerDiv = test('div', {'class': "container"})
    # print(containerDiv)

    # Makes the code only run once
    break

