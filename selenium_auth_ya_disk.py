import os
import time

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from dotenv import load_dotenv

load_dotenv()
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')


def wait_element(browser, delay_second=1, by=By.TAG_NAME, value=None):
    return WebDriverWait(browser, delay_second).until(
        expected_conditions.presence_of_element_located((by, value))
    )


path = ChromeDriverManager().install()
browser_service = Service(executable_path=path)
browser = Chrome(service=browser_service)
browser.get('https://passport.yandex.ru/auth/')


login_window = wait_element(browser, 1, By.CLASS_NAME, "layout_container")

login_input = wait_element(login_window, 1, By.ID, "passp-field-login")
time.sleep(3)

login_input.clear()
login_input.send_keys(LOGIN)
time.sleep(2)

wait_element(login_window, 1, By.ID, "passp:sign-in").click()
time.sleep(2)

passwd_window = wait_element(browser, 1, By.CLASS_NAME, "AuthPasswordForm")

passwrd_input = wait_element(passwd_window, 1, By.ID, "passp-field-passwd")
passwrd_input.clear()

passwrd_input.send_keys(PASSWORD)
time.sleep(2)

wait_element(passwd_window, 1, By.ID, "passp:sign-in").click()
time.sleep(10)
