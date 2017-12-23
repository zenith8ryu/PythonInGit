# Constant
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


LOGIN_ID = "liu_m@worksap.co.jp"
PASSWORD = "Other1guy"

# Sign-in Training
driver = webdriver.Chrome()
driver.get("https://mail.worksap.co.jp/webmail2/resources/mail#/all")

# Password & ID
elem_user = driver.find_element_by_id("loginId")
elem_user.send_keys(LOGIN_ID)
elem_pwd = driver.find_element_by_id("password")
elem_pwd.send_keys(PASSWORD)
elem_pwd.send_keys(Keys.RETURN)

# assert "google" in driver.title
# driver.close()
# driver.quit()
