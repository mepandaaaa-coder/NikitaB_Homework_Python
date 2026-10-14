import pytest
import allure
from selenium import webdriver
from lesson_07.pages.calculator_page import CalculatorPage


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.implicitly_wait(4)
    yield browser
    browser.quit()


@allure.feature("Калькулятор")
@allure.story("Медленные вычисления с задержкой")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Тест калькулятора: сложение с задержкой")
@allure.description(
    "Тест проверяет корректность сложения чисел (7 + 8 = 15) "
    "на странице slow-calculator с установленной задержкой 45 секунд."
)
def test_slow_calculator(driver):
    calculator = CalculatorPage(driver)

    with allure.step("Открыть страницу калькулятора"):
        calculator.open()

    with allure.step("Установить задержку вычислений в 45 секунд"):
        calculator.set_delay(45)

    with allure.step("Нажать кнопки: 7, +, 8, ="):
        calculator.click_button("7")
        calculator.click_button("+")
        calculator.click_button("8")
        calculator.click_button("=")

    with allure.step("Проверить, что результат равен 15 с учетом задержки"):
        result = calculator.get_result("15", timeout=46)
        assert result == "15", f"Ожидался результат 15, но получен {result}"
