from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    """Класс корзины интернет-магазина."""

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self._checkout_button = (By.ID, "checkout")
        self._cart_item_names = (By.CLASS_NAME, "inventory_item_name")

    def click_checkout(self) -> None:
        """Нажимает кнопку оформления заказа (Checkout)."""
        self.driver.find_element(*self._checkout_button).click()

    def get_cart_item_names(self) -> list[str]:
        """Возвращает список названий товаров, находящихся в корзине."""
        items = self.driver.find_elements(*self._cart_item_names)
        return [item.text for item in items]
