from selenium import webdriver
import pytest
import time

driver = webdriver.Chrome("/Users/sindhu/PycharmProjects/Chromedriver/chromedriver 2")
driver.get("https://cosmocode.io/automation-practice-webtable/")
time.sleep(2)
driver.maximize_window()

rows = len(driver.find_elements_by_xpath("/html/body/div[2]/div/div/main/article/div/div/table/tbody/tr"))
cols = len(driver.find_elements_by_xpath("/html/body/div[2]/div/div/main/article/div/div/table/tbody/tr[1]/td"))

print(rows)
print(cols)

driver.find_element_by_xpath("//td[contains(text(),'New Delhi')]/preceding-sibling::td/input[@type = 'checkbox']").click()
print("Selected India")
driver.find_element_by_xpath("//td[contains(text(),'Washington')]/preceding-sibling::td/input[@type = 'checkbox']").click()
print("Selected US")
driver.find_element_by_xpath("//td[contains(text(),'Australian Dollar')]/preceding-sibling::td/input[@type='checkbox']").click()
print("Selected Australia")
driver.find_element_by_xpath("//td[contains(text(),'Portuguese')]/preceding-sibling::td/input[@type='checkbox']").click()
print("Selected Brazil")