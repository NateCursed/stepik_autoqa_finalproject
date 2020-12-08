from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def test_guest_can_add_product_to_basket(self):
        bucket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        bucket_button.click(), "Button weren't found"
        BasePage.solve_quiz_and_get_code(self)
        time.sleep(5)

    def success_add_to_basket(self):
        added_product_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME)
        added_product_price = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_PRICE)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert product_name.text in added_product_name.text, "Invalid added product"
        assert product_price.text in added_product_price.text, "Invalid product price"
