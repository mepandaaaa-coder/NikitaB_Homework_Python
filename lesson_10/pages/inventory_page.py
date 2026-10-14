from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class InventoryPage:
    """Класс каталога товаров интернет-магазина."""

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self._cart_icon = (By.CLASS_NAME, "shopping_cart_link")
        self._add_to_cart_locator: str = (
            "//div[text()='{}']/ancestor::div[@class='inventory_item']//button"
        )

    def add_to_cart(self, item_name: str) -> None:
        """Добавляет указанный товар в корзину по его наименованию."""
        button_xpath = self._add_to_cart_locator.format(item_name)
        self.driver.find_element(By.XPATH, button_xpath).click()

    def go_to_cart(self) -> None:
        """Переходит в корзину с помощью иконки корзины."""
        self.driver.find_element(*self._cart_icon).click()
