from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket_and_message_about_it(self):
        self.should_be_empty_basket_massage()
        self.should_be_empty_basket()

    def should_be_empty_basket_massage(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_MASSAGE), \
            "Empty basket message is not presented"
        assert self.is_disappeared(*BasketPageLocators.EMPTY_MASSAGE), \
            "Empty basket message is not presented"

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEM_BASKET), \
            "Basket is not empty"
        assert self.is_disappeared(*BasketPageLocators.ITEM_BASKET), \
            "Basket is not empty"
