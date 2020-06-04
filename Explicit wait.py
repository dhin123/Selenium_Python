from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("/Users/sindhu/PycharmProjects/chromedriver")
driver.maximize_window()
driver.get("https://expedia.com")
driver.implicitly_wait(5)
driver.find_element_by_id("tab-flight-tab-hp").click()
time.sleep(2)

driver.find_element_by_id("flight-origin-hp-flight").send_keys("SFO")
time.sleep(2)
driver.find_element_by_id("flight-destination-hp-flight").send_keys("NYC")
driver.find_element_by_id("flight-departing-hp-flight").clear()
driver.find_element_by_id("flight-departing-hp-flight").send_keys("02/01/2020")
time.sleep(2)
driver.find_element_by_id("flight-returning-hp-flight").clear()
time.sleep(2)
driver.find_element_by_id("flight-returning-hp-flight").send_keys("02/09/2020")
time.sleep(5)
driver.find_element_by_id("search-button-hp-package").click()

