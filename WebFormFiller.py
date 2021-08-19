from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

# Come back to this later
PATH = "C:\Program Files (x86)\chromedriver.exe"


def fillForm(Code):
    driver = webdriver.Chrome(PATH)
    driver.get("https://but.mis.strath.ac.uk/classcatalogue/control/searchpage")
    wait = WebDriverWait(driver, 10)

    # Used to find and click on accept cookies button
    cookies = wait.until(ec.visibility_of_element_located((By.ID, 'ccc-notify-accept')))
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
    department = driver.find_element_by_xpath(
        '//*[@id="commonContent"]/table[2]/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/table/tbody/tr[5]/td').text

    faculty = driver.find_element_by_xpath(
        '//*[@id="commonContent"]/table[2]/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/table/tbody/tr[6]/td').text

    # Close driver
    driver.close()

    return (department, faculty)



if __name__ == '__main__':
    fillForm('AG409')
