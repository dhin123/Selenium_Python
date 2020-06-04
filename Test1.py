from selenium import webdriver
import time
driver = webdriver.Chrome("/Users/sindhu/PycharmProjects/chromedriver")
driver.get("https://www.linkedin.com/")
time.sleep(1)
driver.find_element_by_xpath("//input[@name='session_key']").send_keys("sindhus1305@gmail.com")
time.sleep(1)
driver.find_element_by_xpath("//input[@name='session_password']").send_keys("Linkedin@123")
driver.find_element_by_xpath("//button[@class='sign-in-form__submit-btn']").click()
time.sleep(1)
driver.find_element_by_xpath("//input[@placeholder='Search']").send_keys("Smitha Shamaprasad")
time.sleep(1)
driver.find_element_by_xpath("//li[@class='inline t-24 t-black t-normal break-words']").click()


