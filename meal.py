
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

options = ChromeOptions()
options.add_argument("--start-maximized")

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "normal"
driver = Chrome("C:\Windows\chromedriver79.exe", chrome_options=options, desired_capabilities=caps)
driver.get("http://meal.khu.ac.ir/")

driver.find_element_by_name('username').clear()
driver.find_element_by_name('username').send_keys("USERNAME")
driver.find_element_by_name('password').clear()
driver.find_element_by_name('password').send_keys("PASSWORD")
driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/form/div/div/button').click()