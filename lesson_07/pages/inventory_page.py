from selenium.webdriver.common.by import By


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

        self._cart_icon = (By.CLASS_NAME, "shopping_cart_link")
        # Локатор кнопки добавления по названию товара
        self._add_to_cart_locator = (
            "//div[text()='{}']/ancestor::div[@class='inventory_item']//button"
        )

    def add_to_cart(self, item_name: str):
        button_xpath = self._add_to_cart_locator.format(item_name)
        self.driver.find_element(By.XPATH, button_xpath).click()

    def go_to_cart(self):
        self.driver.find_element(*self._cart_icon).click()
