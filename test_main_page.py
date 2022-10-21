from selenium.webdriver.common.by import By
import time
from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    time.sleep(5)
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()

