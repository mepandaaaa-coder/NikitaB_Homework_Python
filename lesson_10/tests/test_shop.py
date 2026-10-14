import pytest
import allure
from selenium import webdriver
from lesson_07.pages.login_page import LoginPage
from lesson_07.pages.inventory_page import InventoryPage
from lesson_07.pages.cart_page import CartPage
from lesson_07.pages.checkout_page import CheckoutPage


@pytest.fixture
def driver():
    # Используем браузер Firefox согласно условию задачи
    browser = webdriver.Firefox()
    browser.implicitly_wait(4)
    yield browser
    browser.quit()


@allure.feature("Интернет-магазин SauceDemo")
@allure.story("Оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title(
    "Тест оформления заказа: добавление товаров и проверка итоговой суммы"
    )
@allure.description(
    "Тест проверяет полный цикл покупки: авторизацию standard_user, "
    "добавление трех товаров в корзину, проверку количества позиций, "
    "заполнение формы данными покупателя и сверку итоговой стоимости "
    "(Total: $58.29)."
)
def test_saucedemo_checkout(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    with allure.step("Открыть сайт магазина"):
        login_page.open()

    with allure.step("Авторизоваться как standard_user"):
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Добавить в корзину указанные товары"):
        items_to_add = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"
        ]
        for item in items_to_add:
            inventory_page.add_to_cart(item)

    with allure.step("Перейти в корзину и проверить состав"):
        inventory_page.go_to_cart()
        cart_items = cart_page.get_cart_item_names()
        assert len(cart_items) == 3, (
            f"Ожидалось 3 товара в корзине, но найдено: {len(cart_items)}"
            )

    with allure.step("Нажать кнопку Checkout"):
        cart_page.click_checkout()

    with allure.step("Заполнить форму персональными данными"):
        checkout_page.fill_form("Иван", "Иванов", "101000")

    with allure.step("Прочитать со страницы итоговую стоимость (Total)"):
        total_price = checkout_page.get_total_price()

    with allure.step("Проверить, что итоговая сумма равна $58.29"):
        assert total_price == "Total: $58.29", (
            f"Ожидалась сумма 'Total: $58.29', но получено: {total_price}"
        )
