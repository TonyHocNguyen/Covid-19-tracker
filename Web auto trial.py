from selenium import webdriver
from bs4 import BeautifulSoup
import time
#from selenium.webdriver.common.keys import Keys

country = input(str("Enter the country name: "))

driver = webdriver.Chrome()
driver.get('https://www.cdc.gov/coronavirus/2019-ncov/travelers/map-and-travel-notices.html')

time.sleep(2)

#acceptbutton = driver.find_element_by_xpath('//*[@id="closeModal"]')
#acceptbutton.click()

#country_tab = driver.find_element_by_xpath('//*[@id="tabs"]/li[4]/a')
#country_tab.click()

url = 'https://www.cdc.gov/coronavirus/2019-ncov/travelers/map-and-travel-notices.html'

#SearchBox = driver.find_element_by_xpath('//input[@id="singlecountry_header"]/div/div/div/div[1]')
#SearchBox.send_keys(country)
#SearchBox.submit()

#SearchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
#SearchButton.click()

country_tab = driver.find_element_by_link_text(country)
country_tab.click()



