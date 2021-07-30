# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 09:24:49 2021

@author: Morrison
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen

with open("KEYWORDS.csv") as csv_file:
        sdg = {}
        
        for inc, line in enumerate(csv_file.readlines()):
            sdgNow = [word for word in line.lower().strip().split(',') if word not in ['', '\n', ' ']]       
            sdg[inc+1] = sdgNow
            

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

output={}
toWrite = ''
    

        
   
    
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
    
    toWrite = toWrite + course['href'] + ','
    
    for header in range(1,18):
        toWrite = toWrite + 'SDG' + str(header) + ','
    toWrite = toWrite + '\n'
    
    
    for module in modules:
        
        moduleTitle = module.find('h5')
        moduleDescription = module.find('div', {'class': "course-module-content-inner"})

        moduleTitleText = moduleTitle.text.strip()
     
        moduleDescriptionText = moduleDescription.text.lower()

        sdgList =[]

        for key in sdg.keys():
            CurrentWord = ''
            for word in sdg[key]:
                if word in moduleDescriptionText:
                    CurrentWord = CurrentWord + word + '; ' 
            if len(CurrentWord) > 0:
                CurrentWord = CurrentWord[:-2]
                        
                  
                    
            sdgList.append(CurrentWord)
                    
        output[moduleTitleText] = sdgList
        toWrite = toWrite + moduleTitleText.replace(',',';' ) + ',' + ','.join(sdgList) +'\n'
    toWrite = toWrite + '\n' + '\n'    
    
    #break
    #for key in output.keys():
     #       toWrite = toWrite + (key.replace(',',';' ) + ',' + ','.join(output[key]) + '\n')    
            
    
                    
with open('SDGwords.csv', 'w', encoding = "utf-8") as csvfile:
    #toWrite = ','
    
    # for header in range(1,18):
    #     toWrite = toWrite + 'SDG' + str(header) + ','
    # toWrite = toWrite + '\n'
        
    # for key in output.keys():
    #     toWrite = toWrite + (key.replace(',',';' ) + ',' + ','.join(output[key]) + '\n')    
        
    csvfile.write(toWrite)
    


with open('WebOutputs.csv', 'w', encoding="utf-8") as csvfile:
    toWrite = ','
    
    for header in range(1,18):
        toWrite = toWrite + 'SDG' + str(header) + ','
    toWrite = toWrite + '\n'
        
    for key in output.keys():
        toWrite = toWrite + (key.replace(',',';' ) + ',' + ','.join(output[key]) + '\n')    
        
    csvfile.write(toWrite)



