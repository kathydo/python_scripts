''' 
Python & Selenium Script to crawl, scrape, and download CSV reports from legacy site
'''

import scrapy
import IPython

from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import csv
import pandas as pd


# read in stored password for authorization
with open('password.txt', 'r') as content_file:
    pwd = content_file.read()

# login to webpage
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path="/Users/kdo/Downloads/chromedriver", chrome_options=option)
driver.get("[insert URL]")
driver.find_element_by_id("user").send_keys("kdo")
driver.find_element_by_id("password").send_keys(pwd)
driver.find_element_by_name("btnSubmit").click()

# navigate to web page we want to scrape
driver.find_element_by_id("searchSubmitButton").click()

# get list of all radio button elements and store the unique values in a list
groups_list = open("groups_list.txt").readlines()
groups_list = [item.strip() for item in groups_list]

# list of radio button elements
radio_list = driver.find_elements_by_name(("selectionIndex"))

# Getting values of radio buttons from web page
radio_values = []

# Extract unique value ID from html tag for each project group
for i in range(len(radio_list)):
	radio_values.append(radio_list[i].get_property("value"))

print(radio_values)

# Create a dictionary to match values to group names
dictionary = dict(zip(radio_values, groups_list))

print(dictionary)


for value_id in radio_values:
	# look up and select each radio button by value_id
	locator_query = "//input[@name='selectionIndex' and @value ='" + value_id + "']"
	print(locator_query)
	driver.implicitly_wait(3)
	driver.find_element_by_xpath(locator_query).click()
	driver.implicitly_wait(3)

	# Click to generate CSV Report 
	driver.find_element_by_xpath("//input[@value='CSV Report' and @name='submitType']").click()
	driver.implicitly_wait(3)
	report = driver.find_element_by_tag_name("body").text
	file_name = dictionary[value_id]

	# Write to csv
	new_csv = open(file_name + ".csv", "w")
	new_csv.write(report)
	new_csv.close()
	driver.back()

driver.close()
