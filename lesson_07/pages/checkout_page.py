from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

        # Поля формы первой страницы Checkout
        self._first_name_input = (By.ID, "first-name")
        self._last_name_input = (By.ID, "last-name")
        self._postal_code_input = (By.ID, "postal-code")
        self._continue_button = (By.ID, "continue")

        # Элементы второй страницы Checkout (Overview)
        self._total_label = (By.CLASS_NAME, "summary_total_label")

    def fill_form(self, first_name: str, last_name: str, postal_code: str):
        self.driver.find_element(*self._first_name_input).send_keys(first_name)
        self.driver.find_element(*self._last_name_input).send_keys(last_name)
        self.driver.find_element(*self._postal_code_input).send_keys(
            postal_code
            )
        self.driver.find_element(*self._continue_button).click()

    def get_total_price(self) -> str:
        return self.driver.find_element(*self._total_label).text
