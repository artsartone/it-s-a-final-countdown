from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK_INVALID = (By.XPATH, "//div/span/a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    EMPTY_MASSAGE = (By.XPATH, "//h2[@class='col-sm-6 h3']")
    ITEM_BASKET = (By.XPATH, "//div[@class='basket-title hidden-xs']")


class MainPageLocators():
    LOGIN_LINK = (By.ID, "login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FORM = (By.XPATH, "//input[@id='id_registration-email'] ")
    PASSWORD_FORM = (By.XPATH, "//input[@id='id_registration-password1']")
    PASSWORD_FORM2 = (By.XPATH, "//input[@id='id_registration-password2']")
    REGISTER_BUTTON = (By.XPATH, "//form[@id='register_form']/button ")


class ProductPageLocators():
    BASKET_PRESS = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    BASKET_PRICE = (By.XPATH, "//div[@id='messages']/div[3]/div/p[1]/strong")
    PRODUCT_PRICE = (By.XPATH, "//article/div[1]/div[2]/p[1]")
    PRODUCT_NAME = (By.XPATH, "//article/div[1]/div[2]/h1")
    SUCCESS_MASSAGE = (By.XPATH, "//div[@id='messages']/div[1]/div/strong")
    PRICE_MASSAGE = (By.XPATH, "//div[@class='alert alert-safe alert-noicon alert-info  fade in']")
