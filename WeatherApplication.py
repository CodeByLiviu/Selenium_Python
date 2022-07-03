'''

Implementing a weather script

'''



# Importe relevant modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def startBrowser():
    '''
    This method is used to launch the chrome browser, opens this url https://www.google.com/ and accepts google cookies.
    :return:
    '''
    PATH = "chromedriver.exe"
    global driver
    driver = webdriver.Chrome(PATH)
    pathToTheGoogle = 'https://www.google.com/'
    driver.get(pathToTheGoogle)
    driver.maximize_window()
    cookiesBoxLocator = '//button[@id="L2AGLb"]'
    cookiesBox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, cookiesBoxLocator)))
    cookiesBox.click()


def searchOnGoogle(keyWord):
    '''
    This method is used to start the keyword search.
    :param keyWord: in our case, for this program, the key word is "weather".
    :return:
    '''
    searchBoxLocator = '//input[@class="gLFyf gsfi"]'
    searchBox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, searchBoxLocator)))
    searchBox.click()
    searchBox.send_keys(keyWord)
    searchBox.submit()


def getWeather():
    '''
    This method is used to obtain all day and night temperatures for the current day and the coming week.
    :return: data will be added to a dictionary like this: {day: {time of day: temperature, time of night: temperature}}
    '''
    bigDict = {}
    smallDict = {}
    for x in range(0,8):
        dayBoxLocator = '//div[@data-wob-di="{}"]'.format(x)
        dayBox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, dayBoxLocator)))
        dayBox.click()
        dayText = dayBox.text
        currentDay, currentTemp = dayText.split("\n")
        currentTempDay = currentTemp[:3]
        currentDayNight = currentTemp[3:]
        firstList = ["time of day", "time of night"]
        secondList = [currentTempDay, currentDayNight]
        for i in range(0,2):
            smallDict[firstList[i]] = [secondList[i]]
        bigDict[currentDay] = [smallDict]
    print(bigDict)
    driver.quit()


keyWord = "weather"
startBrowser()
searchOnGoogle(keyWord)
getWeather()

