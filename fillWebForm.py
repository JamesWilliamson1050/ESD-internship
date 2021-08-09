import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Come back to this later
PATH = "C:\Program Files (x86)\chromedriver.exe"


def getSite():
    print()


def fillForm(Code):

    driver = webdriver.Chrome(PATH)
    driver.get("https://but.mis.strath.ac.uk/classcatalogue/control/searchpage")
    # assert "Python" in driver.title
    # elem = driver.find_element_by_name("q")
    # elem.clear()
    # elem.send_keys("pycon")
    # elem.send_keys(Keys.RETURN)
    # assert "No results found." not in driver.page_source
    #driver.close()
    # this waits to load the entire page
    time.sleep(0.5)


    # Used to find and click on accept cookies button
    cookies = driver.find_element_by_id('ccc-notify-accept')
    cookies.click()

    # Find and click on search link
    searchLink = driver.find_element_by_link_text('Search')
    searchLink.click()

    # Filling and submit class catalogue form with a code
    classCode = driver.find_element_by_name('code')
    classCode.send_keys(Code)
    classCode.submit()

    # Click on the link to get the classes information
    classTitleLink = driver.find_element_by_xpath('//*[@id="commonContent"]/table[4]/tbody/tr[2]/td[2]/a')
    classTitleLink.click()

    # Finding a printing the department of a module
    department = driver.find_element_by_xpath('//*[@id="commonContent"]/table[2]/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/table/tbody/tr[5]/td').text


    faculty = driver.find_element_by_xpath('//*[@id="commonContent"]/table[2]/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/table/tbody/tr[6]/td').text



    # Close driver
    driver.close()

    return (department, faculty)


    # print(cookies)




# if __name__ == '__main__':
#     test1()
