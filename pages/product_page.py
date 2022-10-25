from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_page_after_added_product(self):
        self.should_be_added_massage()
        self.should_be_price_massage()
        self.should_be_match_name()
        self.should_be_match_price()

    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.BASKET_PRESS)
        link.click()

    def should_be_added_massage(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MASSAGE), 'Added message is no present'

    def should_be_price_massage(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_MASSAGE), 'Price on basket is not present'

    def should_be_match_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        assert product_price.text == basket_price.text, 'Price is not match'

    def should_be_match_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        added_name = self.browser.find_element(*ProductPageLocators.SUCCESS_MASSAGE)
        assert added_name.text == product_name.text, 'Name is not match'

    def should_not_be_success_message(self):
        assert self.is_not_element_present\
            (*ProductPageLocators.SUCCESS_MASSAGE), "Success message is presented, but should not be"
    def should_be_dissapeared_success_message(self):
        assert self.is_disappeared\
            (*ProductPageLocators.SUCCESS_MASSAGE), "Success message is presented, but should not be"

