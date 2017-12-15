from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Sign-in Training
driver = webdriver.Firefox()
driver.get("https://mail.worksap.co.jp/webmail2/resources/mail#/inbox")

# Password & ID
elem_user = driver.find_element_by_name("loginId")
print(elem_user.get_attribute("type"))
elem_user.send_keys("liu_m@worksap.co.jp")
elem_pwd = driver.find_element_by_name("password")
elem_pwd.send_keys("Other1guy")
elem_pwd.send_keys(Keys.RETURN)
# time.sleep(1)
# assert "google" in driver.title
# driver.close()
# driver.quit()
