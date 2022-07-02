'''
The task:
Create a program that makes instagram acccounts really fast:
the user must input:
an email, first name and last name, a username, a password, the date of birth.

a big problem:
***    THIS PROGRAM IS ONE HALF OF INSTAGRAM ACCOUNT CREATOR, BECAUSE THERE IS ONE MORE STEP TO COMPLETE THE PROCESS AND THAT IS:
YOU NEED TO GET THE ACTIVATION CODE FROM YOUR EMAIL. AND ENTER IT INTO THE LAST FORM, AFTER WHICH YOU'RE GOOD TO GO!    ***
'''

# THE SOLUTION:

# Imported relevant modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def startBrowser():
    '''
    This method is used to open the chromebrowser in instagram website.
    :return:
    '''
    global driver
    PATH = "chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    url = 'https://www.instagram.com/accounts/emailsignup/'
    driver.get(url)
    driver.maximize_window()


def acceptCookies():
    '''
    This method is used to accept all instagram cookies.
    :return:
    '''
    cookiesBoxLocator = '//button[@class="aOOlW   HoLwm "]'
    cookiesBox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, cookiesBoxLocator)))
    cookiesBox.click()
    time.sleep(2)

    
# Let's start filling in first forms!
def completeForms(mail, fullName, userName, password):
    '''
    This method is used to complete the first form with the data requested below:
    :param mail: choose a valid mail
    :param name: write your full name
    :param username: create a username
    :param password: create a password
    :return:
    '''
    emailBoxLactor = '//input[@aria-label="Mobile Number or Email"]'
    emailBox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, emailBoxLactor)))
    emailBox.send_keys(mail)
    nameBoxLocator = '//input[@aria-label="Full Name"]'
    nameBox = WebDriverWait(driver, 10).until(EC.presence_of_element_located(((By.XPATH, nameBoxLocator))))
    nameBox.send_keys(fullName)
    userNameBoxLocator = '//input[@aria-label="Username"]'
    userNameBox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, userNameBoxLocator)))
    userNameBox.send_keys(userName)
    passwordBoxLocator = '//input[@aria-label="Password"]'
    passwordBox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, passwordBoxLocator)))
    passwordBox.send_keys(password)
    passwordBox.submit()

    
# Let's start filling in second forms!
def setBirthday(month, day, year):
    '''
    This method is used to complete the second form with the data requested below:
    :param month: complete with month of birth
    :param day: complete with day of birth
    :param year: complete with year of birth
    :return:
    '''
    monthBoxlocator = '//option[@title="{}"]'.format(month)
    monthBox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, monthBoxlocator)))
    monthBox.click()
    dayBoxLocator = '//option[@title="{}"]'.format(day)
    dayBox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, dayBoxLocator)))
    dayBox.click()
    yearBoxLocator = '//option[@title="{}"]'.format(year)
    yearBox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, yearBoxLocator)))
    yearBox.click()
    confirmBoxLocator = '//button[@class="sqdOP  L3NKy _4pI4F  y3zKF     "]'
    confirmBox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, confirmBoxLocator)))
    confirmBox.click()

    
def mainFunction(mail, fullName, userName, password, month, day, year):
    '''
    This is the main method that combines all functions for the final result.
    :param mail: choose a valid mail
    :param fullName: write your full name
    :param userName: create a username
    :param password: create a password
    :param month: complete with month of birth
    :param day: complete with day of birth
    :param year: complete with year of birth
    :return:
    '''
    try:
        startBrowser()
        acceptCookies()
        completeForms(mail, fullName, userName, password)
        setBirthday(month, day, year)
    except:
        print("You entered the wrong parameter... please try again!")
        driver.quit()

        
mail = input("Please enter a valid e-mail address: ")
fullName = input("Please enter your full name: ")
userName = input("Please create a valid username: ")
password = input("Please create a strong password: ")
month = input("Please enter your month of birth: ")
day = input("Please enter your day of birth: ")
year = input("Please enter your year of birth: ")

mainFunction(mail, fullName, userName, password, month, day, year)
