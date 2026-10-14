from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    """Класс страницы авторизации интернет-магазина SauceDemo."""

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.url: str = "https://www.saucedemo.com/"
        self._username_input = (By.ID, "user-name")
        self._password_input = (By.ID, "password")
        self._login_button = (By.ID, "login-button")

    def open(self) -> None:
        """Открывает страницу авторизации в браузере."""
        self.driver.get(self.url)

    def login(self, username: str, password: str) -> None:
        """Вводит логин, пароль и нажимает кнопку входа."""
        self.driver.find_element(*self._username_input).send_keys(username)
        self.driver.find_element(*self._password_input).send_keys(password)
        self.driver.find_element(*self._login_button).click()
