from selenium import webdriver
import time

names = []
driver = webdriver.Chrome("/Users/sindhu/PycharmProjects/Chromedriver/chromedriver 2")
driver.get("https://www.seleniumeasy.com/test/table-search-filter-demo.html")



rows = len(driver.find_elements_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div/table/tbody/tr"))
print(rows)
for r in range(1, rows+1):
    name = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div/table/tbody/tr["+str(r)+"]/td[2]").text
    names.append(name)
print(names)

for i in range(len(names)):
    time.sleep(2)
    driver.find_element_by_id("task-table-filter").send_keys(names[i])
    time.sleep(2)
    print("Finished searching", names[i])
    driver.find_element_by_id("task-table-filter").clear()
    time.sleep(2)



