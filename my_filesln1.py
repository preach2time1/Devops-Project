import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
# driver.get("https://github.com/Dgotlieb/PySelenium")
# driver.find_element(By.ID,value=':R55ab:').click()
# driver.find_element(By.LINK_TEXT,value='code').click()
# driver.find_element(By.PARTIAL_LINK_TEXT,value='co').click()
# driver.find_element(By.XPATH,value='/html/body/div[1]/div[4]/div/main/turbo-frame/div/div/div/div[2]/div[1]/react-partial/div/div/div[3]/div[2]').click()
# driver.find_element(By.ID,value='q').send_keys('Hello_Valentine')
# driver.find_element(By.ID,value='q').clear()
#
# # driver.find_element(By.NAME,value=':R55ab:').click()
# # driver.find_element(By.CLASS_NAME,value='types__StyledButton-sc-ws60qy-0').click()
#
# elements = driver.find_elements(By.ID,value=':R55ab:')
# print(len(elements))
# elements = driver.find_elements(By.TAG_NAME, value='div')
# print(len(elements))
# driver.get("https://youtube.com")
# driver.get("https://facebook.com")
# driver.get("https://gmail.com")
# print(driver.current_url)
# print(driver.title)
#
# assert driver.title == 'Google'
#
# if driver.title == 'Google':
#
#     print("Valentine")
driver.get("https://translate.google.com")
time.sleep(5)
driver.find_element(By.CLASS_NAME, value='er8xn').send_keys("Hello Valentine")
driver.find_element(By.CLASS_NAME, value='er8xn').send_keys(Keys.SPACE)

element = driver.find_element(By.CLASS_NAME, value='er8xn').send_keys()
print(element.get_attribute('jsname'))
# elements = driver.find_elements(By.CLASS_NAME, value='er8xn')
# print(len(elements))

if element.is_enabled():
    element.click()

time.sleep(5)

driver.quit()