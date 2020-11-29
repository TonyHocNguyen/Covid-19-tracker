from selenium import webdriver
import time
#from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('https://worldhealthorg.shinyapps.io/covid/')

time.sleep(2)

acceptbutton = driver.find_element_by_xpath('//*[@id="closeModal"]')
acceptbutton.click()

country_tab = driver.find_element_by_xpath('//*[@id="tabs"]/li[4]/a')
country_tab.click()

country = input(str("Enter the country name: "))

#SearchBox = driver.find_element_by_xpath('//input[@id="singlecountry_header"]/div/div/div/div[1]')
#SearchBox.send_keys(country)
#SearchBox.submit()

#SearchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
#SearchButton.click()