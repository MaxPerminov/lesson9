from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# driver = webdriver.Chrome()
# driver.get("https://youtube.com")
# time.sleep(1)
# searcher = driver.find_element(by=By.NAME, value="search_query")
# time.sleep(2)
# searcher.send_keys("Hello world")

##################################################################
class Test:

  def __init__(self, driver):    
    self.driver = driver
  
  def move_to(self, url):
    self.driver.get(url)

  def finder_element(self, by, value):
    return self.driver.find_element(by, value)

  def send_data(self, by, text, value):
    self.driver.find_element(by, value).send_keys(text)

  def screen(self, name):
    self.driver.save_screenshot(name)


chrome_test = Test(webdriver.Chrome())

chrome_test.move_to("https://jsonplaceholder.typicode.com/")
chrome_test.finder_element(By.ID, "run-button").click()
chrome_test.move_to("https://youtube.com/")


chrome_test.send_data(By.NAME, "something", "search_query")
chrome_test.screen("screen1.png")
time.sleep(2)