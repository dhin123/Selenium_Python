from selenium import webdriver

driver = webdriver.Chrome("/Users/sindhu/PycharmProjects/Chromedriver/chromedriver 2")
driver.get("https://www.amazon.in/")
driver.find_element_by_name("email").send_keys("sindhus1305@gmail.com")
driver.find_element_by_id("continue").click()
driver.find_element_by_name("password").send_keys("Amazon@123")
driver.find_element_by_id("signInSubmit").click()


actual_name = "Sindhu"
message = "Hello" + actual_name
var = driver.find_element_by_xpath("/html/body/div[1]/header/div/div[1]/div[2]/div/a[2]/div/span").text()
if message == "Hello" + var:
    print("Success")
else:
    print("fail")

