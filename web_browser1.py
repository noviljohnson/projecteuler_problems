from selenium import webdriver
import time
driver=webdriver.Chrome("C:\webdrivers\chromedriver.exe")
driver.set_page_load_timeout(20)
driver.get('https://www.google.com/')
driver.find_element_by_class_name("q").send_keys("novil")
driver.find_element_by_class_name("dtnk").click()
time.sleep(4)
