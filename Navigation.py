from selenium import webdriver
import time

driver = webdriver.Chrome("/Users/sindhu/PycharmProjects/Chromedriver/chromedriver 2")

driver.get("https://nirmalatravels.com/")
print(driver.title)
time.sleep(2)
driver.get("https://selenium.dev/")
print(driver.title)
time.sleep(2)
driver.back()
print(driver.title)
time.sleep(1)
driver.forward()
print(driver.title)
driver.close()

