from bs4 import BeautifulSoup
from urllib.request import urlopen
import webbrowser

defaultURL = 'https://www.strath.ac.uk'

coursesSearchURL = '/courses/undergraduate/'

defaultPage = urlopen(defaultURL + coursesSearchURL)

defaultHtml = defaultPage.read().decode("utf-8")

soup = BeautifulSoup(defaultHtml, 'lxml')

courses = soup.find_all('a', class_="course-search-result__link")
x = 0
for course in courses:

    #print(course['href'])

    courseURL = (defaultURL + course['href'])
  #  webbrowser.open(courseURL)
    coursePage = urlopen(courseURL)
    courseHtml = coursePage.read().decode("utf-8")
    courseContent = BeautifulSoup(courseHtml, 'lxml')
    test = courseContent.find('div', {"id": "coursecontent"})
    containerDiv = test('div', {'class': "container"})
    print(containerDiv)



    x += 1
    if x == 1:
        break




# <ul class="course-module-nav-tabs nav nav-tabs off-canvas-tabs" id="myTab" role="tablist">
#                             <li class="course-module-header nav-item" aria-controls="tab-0-panel"><a class="nav-link grey-block-button off-canvas-button-open active" id="" data-toggle="tab" href="#tab-0-panel" role="tab" aria-controls="home" aria-selected="true">Year 1</a></li><li class="course-module-header nav-item" aria-controls="tab-1-panel"><a class="nav-link grey-block-button off-canvas-button-open" id="" data-toggle="tab" href="#tab-1-panel" role="tab" aria-controls="home" aria-selected="true">Year 2</a></li><li class="course-module-header nav-item" aria-controls="tab-2-panel"><a class="nav-link grey-block-button off-canvas-button-open" id="" data-toggle="tab" href="#tab-2-panel" role="tab" aria-controls="home" aria-selected="true">Year 3</a></li><li class="course-module-header nav-item" aria-controls="tab-3-panel"><a class="nav-link grey-block-button off-canvas-button-open" id="" data-toggle="tab" href="#tab-3-panel" role="tab" aria-controls="home" aria-selected="true">Year 4</a></li></ul>

