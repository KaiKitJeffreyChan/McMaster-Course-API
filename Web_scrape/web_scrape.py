from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv

driver = webdriver.Chrome(executable_path="./Drivers/chromedriver")

driver.get(
    "https://academiccalendars.romcmaster.ca/content.php?catoid=41&navoid=8647")
driver.implicitly_wait(5)

for i in range(1, 10):
    # returns the number of rows within the table
    list_rows = driver.find_elements_by_xpath(
        '//*[@id="table_block_n2_and_content_wrapper"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[2]/tbody/tr')

    # iterate all rows and print info,
    for j in range(1, len(list_rows)-1):
        # printing units(all course stuff)
        try:
            open_link = driver.find_element_by_xpath(
                f'//*[@id="table_block_n2_and_content_wrapper"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[{j}]/td[2]/a')
            open_link.click()

            units = driver.find_element_by_xpath(
                f'//*[@id="table_block_n2_and_content_wrapper"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[{j}]/td[2]/table/tbody/tr/td/div[2]').text
            print(units)
        except:
            print("no course units")

    next_page = driver.find_element_by_xpath(
        f'//*[@id="table_block_n2_and_content_wrapper"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[104]/td/a[{i}]')
    next_page.click()

# instead of increment by 1 on this xpath, find the last row of the table


# printing course name first
# try:
#     open_link = driver.find_element_by_xpath(
#         f'//*[@id="table_block_n2_and_content_wrapper"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[{i}]/td[2]/a')
#     open_link.click()
#     driver.implicitly_wait(100)

#     title = driver.find_element_by_xpath(
#         f'//*[@id="table_block_n2_and_content_wrapper"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[{i}]/td[2]/table/tbody/tr/td/div[2]/h3').text
#     print(title)
# except:
#     print("There is no course name here")


# THIS WORKS FOR ONE TITLE
# link = driver.find_element_by_xpath(
#     '//*[@id="table_block_n2_and_content_wrapper"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[3]/td[2]/a')
# link.click()
# driver.implicitly_wait(100)

# title = driver.find_element_by_xpath(
#     '//*[@id="table_block_n2_and_content_wrapper"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[3]/td[2]/table/tbody/tr/td/div[2]/h3'
# ).text


# IDEA TO LOOP THROUGH ALL THE THINGS
# for i in range(3, 10):
#     current_name = driver.find_element_by_xpath(
#         f'//*[@id="table_block_n2_and_content_wrapper"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[{i}]/td[2]/table/tbody/tr/td/div[2]/h3').text
#     print(current_name)
