from selenium import webdriver
import time

#from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('https://www.cdc.gov/coronavirus/2019-ncov/travelers/map-and-travel-notices.html?fbclid=IwAR1PWJ9ycocek7qcagrm7MqjGczOqvtvlqsp0vOs1-u3AslRRoFeEGZG2Rk')

time.sleep(2)

#acceptbutton = driver.find_element_by_xpath('//*[@id="closeModal"]')
#acceptbutton.click()

#country_tab = driver.find_element_by_xpath('//*[@id="tabs"]/li[4]/a')
#country_tab.click()

country = input(str("Enter the country name: "))
country_tab = driver.find_element_by_link_text(country)
country_tab.click()

level = (driver.find_element_by_xpath('//*[@id="contentArea"]/div[2]/div[1]/div/div')).text
print(level)

if 'Low' in level:
    print('low')
#SearchBox = driver.find_element_by_xpath('//input[@id="singlecountry_header"]/div/div/div/div[1]')
#SearchBox.send_keys(country)
#SearchBox.submit()

#SearchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
#SearchButton.click()
