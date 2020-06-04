from selenium import webdriver
import time

driver = webdriver.Chrome("/Users/sindhu/PycharmProjects/Chromedriver/chromedriver 2")
driver.get("https://selenium.dev/selenium/docs/api/java/index.html")

driver.switch_to.frame("packageListFrame")
driver.find_element_by_link_text("org.openqa.selenium").click()
time.sleep(3)

driver.switch_to.default_content()
time.sleep(3)
driver.switch_to.frame("packageFrame")
driver.find_element_by_link_text("WebDriver").click()
time.sleep(3)

driver.switch_to.default_content()
time.sleep(3)
driver.switch_to.frame("classFrame")
driver.find_element_by_xpath("//div[@class='topNav']//a[contains(text(),'Deprecated')]").click()