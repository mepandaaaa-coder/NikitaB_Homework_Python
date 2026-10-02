from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_slow_calculator():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # 1. Открыть страницу
        url = (
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/slow-calculator.html"
        )
        driver.get(url)

        # 2. Ввести значение задержки 45 в поле #delay
        delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys("45")

        # 3. Нажать на кнопки: 7, +, 8, =
        driver.find_element(By.XPATH, "//span[text()='7']").click()
        driver.find_element(By.XPATH, "//span[text()='+']").click()
        driver.find_element(By.XPATH, "//span[text()='8']").click()
        driver.find_element(By.XPATH, "//span[text()='=']").click()

        # 4. Проверить (assert), что результат 15 появится через 45 секунд
        # Задаем таймаут 50 секунд, чтобы учлись 45 сек задержки + запас
        wait = WebDriverWait(driver, 50)
        wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), "15"
            )
        )

        result_text = driver.find_element(By.CSS_SELECTOR, ".screen").text
        assert result_text == "15"

    finally:
        driver.quit()
