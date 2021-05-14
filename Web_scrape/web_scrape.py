from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv

driver = webdriver.Chrome(executable_path="./Drivers/chromedriver")

driver.get(
    "https://academiccalendars.romcmaster.ca/content.php?catoid=41&navoid=8647")
driver.implicitly_wait(5)

# how many pages of courses there are
for i in range(2, 33):

    # returns the number of rows within the table
    list_rows = driver.find_elements_by_xpath(
        '//*[@id="table_block_n2_and_content_wrapper"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[2]/tbody/tr')

    # iterate all rows and print info, first 3 rows are empty last row also empty
    for j in range(3, len(list_rows)-1):
        # printing units(all course stuff)
        try:
            open_link = driver.find_element_by_xpath(
                f'//*[@id="table_block_n2_and_content_wrapper"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[{j}]/td[2]/a')
            open_link.click()

            units = driver.find_element_by_xpath(
                f'//*[@id="table_block_n2_and_content_wrapper"]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[{j}]/td[2]/table/tbody/tr/td/div[2]').text

            with open('courseInfo.csv', 'a', newline='') as f:
                thewriter = csv.writer(f)
                thewriter.writerow([units])

            print(units)
        except:
            print("no course units")

    # find last row of table, then press the next page
    last_row = driver.find_element_by_css_selector(
        f'[aria-label = "Page {i}"]')
    last_row.click()

driver.quit()
