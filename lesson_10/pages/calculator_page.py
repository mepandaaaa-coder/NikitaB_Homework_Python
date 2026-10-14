from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """Класс страницы медленного калькулятора."""

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.url: str = (
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )
        self._delay_input = (By.CSS_SELECTOR, "#delay")
        self._screen = (By.CSS_SELECTOR, ".screen")
        self._button_locator: str = "//span[text()='{}']"

    def open(self) -> None:
        """Открывает страницу калькулятора."""
        self.driver.get(self.url)

    def set_delay(self, seconds: int | str) -> None:
        """Устанавливает задержку вычислений в секундах."""
        delay_field = self.driver.find_element(*self._delay_input)
        delay_field.clear()
        delay_field.send_keys(str(seconds))

    def click_button(self, text: str) -> None:
        """Нажимает на кнопку калькулятора по её символу или знаку."""
        button_xpath = self._button_locator.format(text)
        self.driver.find_element(By.XPATH, button_xpath).click()

    def get_result(self, expected_value: str, timeout: int = 50) -> str:
        """
        Ожидает появления ожидаемого значения на экране и возвращает текст.
        """
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self._screen, expected_value)
        )
        return self.driver.find_element(*self._screen).text
