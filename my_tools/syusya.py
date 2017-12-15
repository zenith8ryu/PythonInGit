import time
from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
from selenium import webdriver


def login():
    # Sign-in Training
    driver = webdriver.Firefox()
    driver.get("https://ckip.worksap.co.jp/cws/cws/srwtimerec")

    # Password & ID
    elem_user = driver.find_element_by_name("user_id")
    elem_user.send_keys("5651")
    elem_pwd = driver.find_element_by_name("password")
    elem_pwd.send_keys("Other1guy")
    elem_watch = driver.find_element_by_id("tokei")

    elem_syu_btn = driver.find_element_by_xpath("//td[input/@value=' 出 社 / Work start ']")
    elem_syu_btn.click()

    # time.sleep(5)
    # assert "google" in driver.title
    # driver.close()
    # driver.quit()


# Output datetime
def job():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


# Job Scheduler
def scheduler(func):
    # BlockingScheduler
    scheduler = BlockingScheduler()
    scheduler.add_job(func, 'cron', hour=9, minute=35, second=55)
    scheduler.start()


scheduler(login)
