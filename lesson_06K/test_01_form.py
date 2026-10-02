from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_fill_form():
    driver = webdriver.Edge()
    driver.maximize_window()

    try:
        wait = WebDriverWait(driver, 10)

        # 1. Открыть страницу
        url = (
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/data-types.html"
        )
        driver.get(url)

        # 2. Заполнить форму значениями
        driver.find_element(By.NAME, "first-name").send_keys("Иван")
        driver.find_element(By.NAME, "last-name").send_keys("Петров")
        driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
        driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
        driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
        # Zip code оставляем пустым
        driver.find_element(By.NAME, "city").send_keys("Москва")
        driver.find_element(By.NAME, "country").send_keys("Россия")
        driver.find_element(By.NAME, "job-position").send_keys("QA")
        driver.find_element(By.NAME, "company").send_keys("SkyPro")

        # 3. Нажать кнопку Submit
        submit_btn = driver.find_element(
            By.CSS_SELECTOR, "button[type='submit']"
        )
        submit_btn.click()

        # Ожидание изменения стилей (появления классов alert)
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".alert"))
        )

        # 4. Проверка: Zip code подсвечен красным (alert-danger)
        zip_code_alert = driver.find_element(By.ID, "zip-code")
        zip_class = zip_code_alert.get_attribute("class")
        assert "alert-danger" in zip_class

        # 5. Проверка: остальные поля подсвечены зеленым (alert-success)
        green_fields = [
            "first-name",
            "last-name",
            "address",
            "e-mail",
            "phone",
            "city",
            "country",
            "job-position",
            "company",
        ]

        for field_id in green_fields:
            field_element = driver.find_element(By.ID, field_id)
            field_class = field_element.get_attribute("class")
            assert "alert-success" in field_class

    finally:
        driver.quit()
