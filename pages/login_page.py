from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login is not presented"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        assert True

    def register_new_user(self):
        self.send_email()
        self.send_pass()
        self.send_pass2()
        self.send_register_button()

    def send_email(self):
        email = self.browser.find_element(*LoginPageLocators.EMAIL_FORM)
        form_email = str(time.time()) + "@fakemail.org"
        email.send_keys(form_email)

    def send_pass(self):
        password = self.browser.find_element(*LoginPageLocators.PASSWORD_FORM)
        password.send_keys("Don't hack me pls")

    def send_pass2(self):
        password_two = self.browser.find_element(*LoginPageLocators.PASSWORD_FORM2)
        password_two.send_keys("Don't hack me pls")

    def send_register_button(self):
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()

