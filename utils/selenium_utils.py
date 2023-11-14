import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_driver():
    return webdriver.Edge()


def set_cookie(driver, key, value, path, domain):
    cookie = {
        'name': key,
        'value': value,
        'path': path,
        'domain': domain
    }
    driver.add_cookie(cookie)


def scroll_to_bottom(driver: webdriver, ele_id: str):
    # 设置一个等待时间，最多等待10秒
    WebDriverWait(driver, 10)

    # 加载页面，等待直到页面加载完成
    element = driver.find_element(By.ID, ele_id)
    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'end', inline: 'nearest' });", element)
    time.sleep(3)





