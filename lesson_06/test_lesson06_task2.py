from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_session_cookie_for_user(email, password):
    """
    Вспомогательная функция: открывает страницу авторизации, вводит данные
    и возвращает свежую куку SESSION.
    """
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        # 1. Переходим на страницу авторизации
        driver.get("https://gitflic.ru/auth/login")

        # 2. Заполняем email
        email_input = wait.until(
            EC.visibility_of_element_located((By.NAME, "email"))
        )
        email_input.clear()
        email_input.send_keys(email)
        # 3. Заполняем пароль
        password_input = driver.find_element(By.NAME, "password")
        password_input.clear()
        password_input.send_keys(password)

        # 4. Нажимаем "Войти"
        submit_button = driver.find_element(
            By.CSS_SELECTOR, "input[type='submit']"
            )
        submit_button.click()

        # 5. Ждем ухода со страницы входа
        wait.until(lambda d: "/auth/login" not in d.current_url)
        # 6. Получаем куку
        session_cookie = driver.get_cookie("SESSION")
        return session_cookie
    finally:
        driver.quit()


def test_session_storage_auth():
    user1_email = "t07h1sjrlu@lnovic.com"
    user1_password = "klsdjfg;39847593jaf;lkdj"
    username_1 = "test01111"

    user2_email = "ejw9pwygdk@ozsaip.com"
    user2_password = "aksdjhfl89zxc7v0z82m3n4kj2l"
    username_2 = "test02222"

    # 1. Получаем свежие SESSION куки для обоих пользователей
    cookie_user1 = get_session_cookie_for_user(user1_email, user1_password)
    cookie_user2 = get_session_cookie_for_user(user2_email, user2_password)

    # 2. Основной тест
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        # --- Шаги для Пользователя 1 ---
        driver.get("https://gitflic.ru/")
        driver.add_cookie(cookie_user1)
        driver.refresh()
        driver.get(f"https://gitflic.ru/user/{username_1}")
        wait.until(EC.url_contains(f"/user/{username_1}"))
        url_user1 = driver.current_url

        # Разлогиниваемся (очищаем куки)
        driver.delete_all_cookies()

        # --- Шаги для Пользователя 2 ---
        driver.get("https://gitflic.ru/")
        driver.add_cookie(cookie_user2)
        driver.refresh()

        driver.get(f"https://gitflic.ru/user/{username_2}")
        wait.until(EC.url_contains(f"/user/{username_2}"))
        url_user2 = driver.current_url

        # Проверка различия URL
        assert url_user1 != url_user2

    finally:
        driver.quit()
