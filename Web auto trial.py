from selenium import webdriver
import time
#from selenium.webdriver.common.keys import Keys
def get_data():

    driver = webdriver.Chrome()

    driver.get('https://www.kayak.com/travel-restrictions?fbclid=IwAR2YLyQuyq4PDBDX1s5Z-k_K-uOiEPkevwuylWVXbU08r5UsWmbs-CICOR4')
     
    time.sleep(2)
    """
    terms_and_condition = driver.find_element_by_xpath('//*[@id="captcha_agree"]')
    terms_and_condition.click()

    captcha = driver.find_element_by_xpath('//*[@id="recaptcha-anchor"]/div[1]')
    captcha.click()

    country = input(str("Enter the country name: "))

    SearchBox = driver.find_element_by_xpath('//input[@id="singlecountry_header"]/div/div/div/div[1]')
    SearchBox.send_keys(country)
    SearchBox.submit()
    
    #SearchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
    #SearchButton.click()
    """
    
get_data()