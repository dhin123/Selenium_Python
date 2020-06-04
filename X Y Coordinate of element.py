from selenium import webdriver
import time

driver = webdriver.Chrome("/Users/sindhu/PycharmProjects/Chromedriver/chromedriver 2")
driver.get("https://www.google.com/")

img = driver.find_element_by_xpath("/html/body/div/div[6]/span/center/div[1]/img")

location = img.location
size = img.size

print("The location of the image is", location)
print("The size of the image is", size)