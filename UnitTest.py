import unittest
from selenium import webdriver

class SearchEngineTest(unittest.TestCase):
    def test_Google(self):
        self.driver = webdriver.Chrome("/Users/sindhu/PycharmProjects/Chromedriver/chromedriver 2")
        self.driver.get("https://www.google.com/")
        print(self.driver.title)
        self.driver.close()

    def test_bing(self):
        self.driver = webdriver.Chrome("/Users/sindhu/PycharmProjects/Chromedriver/chromedriver 2")
        self.driver.get("https://www.bing.com/")
        print(self.driver.title)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
