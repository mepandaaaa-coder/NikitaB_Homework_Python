import pytest
from selenium import webdriver
from lesson_07.Pages.calculator_page import CalculatorPage


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.implicitly_wait(4)
    yield browser
    browser.quit()


def test_slow_calculator(driver):
    calculator = CalculatorPage(driver)

    # 1. Открыть страницу калькулятора
    calculator.open()

    # 2. Ввести значение 45 в поле задержки
    calculator.set_delay(45)

    # 3. Нажать кнопки 7, +, 8, =
    calculator.click_button("7")
    calculator.click_button("+")
    calculator.click_button("8")
    calculator.click_button("=")

    # 4. Проверить (assert), что результат 15 отобразился с учетом задержки
    result = calculator.get_result("15", timeout=50)
    assert result == "15"
