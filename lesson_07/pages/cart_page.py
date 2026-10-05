from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver

        self._checkout_button = (By.ID, "checkout")
        self._cart_item_names = (By.CLASS_NAME, "inventory_item_name")

    def click_checkout(self):
        self.driver.find_element(*self._checkout_button).click()

    def get_cart_item_names(self) -> list[str]:
        items = self.driver.find_elements(*self._cart_item_names)
        return [item.text for item in items]
