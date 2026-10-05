from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_saucedemo_shop():
    driver = webdriver.Firefox()
    driver.maximize_window()

    try:
        wait = WebDriverWait(driver, 10)

        # 1. Открыть сайт магазина
        driver.get("https://www.saucedemo.com/")

        # 2. Авторизоваться под standard_user
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # 3. Добавить в корзину указанные товары
        driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack"
        ).click()
        driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
        ).click()
        driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie"
        ).click()

        # 4. Перейти в корзину
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # 5. Нажать Checkout
        wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        ).click()

        # 6. Заполнить форму персональными данными
        driver.find_element(By.ID, "first-name").send_keys("Иван")
        driver.find_element(By.ID, "last-name").send_keys("Иванович")
        driver.find_element(By.ID, "postal-code").send_keys("190020")

        # 7. Нажать кнопку Continue
        driver.find_element(By.ID, "continue").click()

        # 8. Прочитать со страницы итоговую стоимость (Total)
        total_element = wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
                )
        )
        total_text = total_element.text

    finally:
        # 9. Закрыть браузер
        driver.quit()

    # 10. Проверить (assert), что итоговая сумма равна $58.29
    assert total_text == "Total: $58.29"
