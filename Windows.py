from selenium import webdriver
import time

driver = webdriver.Chrome("/Users/sindhu/PycharmProjects/chromedriver")

driver.get("http://demo.automationtesting.in/Windows.html")
driver.find_element_by_xpath("//div[@id='Tabbed']//button[@class='btn btn-info'][contains(text(),'click')]").click()

print(driver.current_window_handle)
handles = driver.window_handles
for hand in handles:
    driver.switch_to.window(hand)
    print(driver.title)

driver.quit()

