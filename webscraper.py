from bs4 import BeautifulSoup
from urllib.request import urlopen
import webbrowser

testurl = 'https://www.strath.ac.uk/courses/undergraduate/'

testpage = urlopen(testurl)

testhtml = testpage.read().decode("utf-8")

testsoup = BeautifulSoup(testhtml, 'lxml')

courses = testsoup.find_all('a', class_="course-search-result__link")
x = 0
for course in courses:

    print(course['href'])
    webbrowser.open('https://www.strath.ac.uk' + course['href'])
    x += 1
    if x == 1:
        break





