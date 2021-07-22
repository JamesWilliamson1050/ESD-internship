from bs4 import BeautifulSoup
from urllib.request import urlopen

testurl = 'https://www.strath.ac.uk/courses/undergraduate/'

testpage = urlopen(testurl)

testhtml = testpage.read().decode("utf-8")

testsoup = BeautifulSoup(testhtml, 'lxml')

atags = testsoup.find_all('a', class_="course-search-result__link")

for hyperlinks in atags:
    print(hyperlinks['href'])
#
# for atag in atags:
#     print(atag.text)


